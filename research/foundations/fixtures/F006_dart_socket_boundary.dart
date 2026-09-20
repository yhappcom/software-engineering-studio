import 'dart:async';
import 'dart:io';
import 'dart:typed_data';

Future<void> main() async {
  stdout.writeln('F006_PHASE bind_server');
  final server = await ServerSocket.bind(InternetAddress.loopbackIPv4, 0);

  // Use a one-shot stream consumption rather than leaving a ServerSocket.listen
  // subscription active. The previous fixture printed its semantic PASS oracle
  // and then remained alive until the outer CI timeout, so this variant changes
  // only the listener lifecycle while retaining the same transport oracle.
  final acceptedFuture = server.first.timeout(const Duration(seconds: 5));

  stdout.writeln('F006_PHASE connect_client');
  final client = await Socket.connect(InternetAddress.loopbackIPv4, server.port);
  final peer = await acceptedFuture;
  await server.close().timeout(const Duration(seconds: 5));

  stdout.writeln('F006_PHASE send_truncated_frame');
  client.add(Uint8List.fromList([0, 5, 72, 69])); // declared 5-byte body, only "HE"
  await client.flush();
  final closeFuture = client.close();

  stdout.writeln('F006_PHASE consume_peer_eof');
  final bytes = <int>[];
  await for (final chunk in peer.timeout(const Duration(seconds: 5))) {
    bytes.addAll(chunk);
  }
  peer.destroy();
  await closeFuture.timeout(const Duration(seconds: 5));

  if (bytes.length != 4 ||
      bytes[0] != 0 ||
      bytes[1] != 5 ||
      bytes[2] != 72 ||
      bytes[3] != 69) {
    throw StateError(
      'expected truncated frame 00054845, got '
      '${bytes.map((b) => b.toRadixString(16).padLeft(2, '0')).join()}',
    );
  }
  final declared = (bytes[0] << 8) | bytes[1];
  final bodyLength = bytes.length - 2;
  if (declared != 5 || bodyLength >= declared) {
    throw StateError(
      'EOF must not make incomplete frame valid: '
      'declared=$declared body=$bodyLength',
    );
  }

  stdout.writeln('F006_PHASE connect_failure_probe');
  final temporary = await ServerSocket.bind(InternetAddress.loopbackIPv4, 0);
  final unusedPort = temporary.port;
  await temporary.close().timeout(const Duration(seconds: 5));
  var refused = false;
  try {
    final unexpected = await Socket.connect(
      InternetAddress.loopbackIPv4,
      unusedPort,
      timeout: const Duration(seconds: 2),
    );
    unexpected.destroy();
  } on SocketException {
    refused = true;
  }
  if (!refused) {
    throw StateError('expected connection failure on released loopback port');
  }

  stdout.writeln(
    'F006_DART_SOCKET_PASS '
    'truncated_eof_rejected=true connect_failure_observed=true',
  );
  stdout.writeln('F006_PHASE natural_process_exit_expected');
}
