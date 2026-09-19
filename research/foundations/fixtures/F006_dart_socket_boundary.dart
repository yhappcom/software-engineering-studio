import 'dart:async';
import 'dart:io';
import 'dart:typed_data';

Future<void> main() async {
  final server = await ServerSocket.bind(InternetAddress.loopbackIPv4, 0);
  final serverDone = Completer<void>();
  Object? serverError;

  server.listen((socket) async {
    try {
      final bytes = <int>[];
      await for (final chunk in socket) {
        bytes.addAll(chunk);
      }
      if (bytes.length != 4 || bytes[0] != 0 || bytes[1] != 5 || bytes[2] != 72 || bytes[3] != 69) {
        throw StateError('expected truncated frame 00054845, got ${bytes.map((b) => b.toRadixString(16).padLeft(2, '0')).join()}');
      }
      final declared = (bytes[0] << 8) | bytes[1];
      final bodyLength = bytes.length - 2;
      if (declared != 5 || bodyLength >= declared) {
        throw StateError('EOF must not make incomplete frame valid: declared=$declared body=$bodyLength');
      }
      serverDone.complete();
    } catch (e, st) {
      serverError = '$e\n$st';
      if (!serverDone.isCompleted) serverDone.complete();
    } finally {
      socket.destroy();
    }
  });

  final client = await Socket.connect(InternetAddress.loopbackIPv4, server.port);
  client.add(Uint8List.fromList([0, 5, 72, 69])); // declared 5-byte body, only "HE"
  await client.flush();
  // Socket.close() closes the IOSink/send side, but awaiting its Future before
  // the peer consumes EOF can create an unnecessary wait cycle. Start close,
  // let the peer observe EOF, then await close completion.
  final closeFuture = client.close();
  await serverDone.future.timeout(const Duration(seconds: 5));
  await closeFuture.timeout(const Duration(seconds: 5));
  await server.close();
  if (serverError != null) throw StateError('$serverError');

  final temporary = await ServerSocket.bind(InternetAddress.loopbackIPv4, 0);
  final unusedPort = temporary.port;
  await temporary.close();
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
  if (!refused) throw StateError('expected connection failure on released loopback port');

  stdout.writeln('F006_DART_SOCKET_PASS truncated_eof_rejected=true connect_failure_observed=true');
}
