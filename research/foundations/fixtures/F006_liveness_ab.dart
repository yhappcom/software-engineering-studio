import 'dart:io';
import 'dart:typed_data';

Future<void> main(List<String> args) async {
  if (args.length != 1) {
    stderr.writeln('usage: F006_liveness_ab.dart <server-close|accepted-close|truncated-eof|refused-connect>');
    exitCode = 64;
    return;
  }
  final mode = args.single;
  stdout.writeln('F006_AB_START mode=$mode');
  switch (mode) {
    case 'server-close':
      final server = await ServerSocket.bind(InternetAddress.loopbackIPv4, 0);
      await server.close().timeout(const Duration(seconds: 3));
      break;
    case 'accepted-close':
      final server = await ServerSocket.bind(InternetAddress.loopbackIPv4, 0);
      final accepted = server.first.timeout(const Duration(seconds: 3));
      final client = await Socket.connect(InternetAddress.loopbackIPv4, server.port);
      final peer = await accepted;
      await server.close().timeout(const Duration(seconds: 3));
      await client.close().timeout(const Duration(seconds: 3));
      peer.destroy();
      break;
    case 'truncated-eof':
      final server = await ServerSocket.bind(InternetAddress.loopbackIPv4, 0);
      final accepted = server.first.timeout(const Duration(seconds: 3));
      final client = await Socket.connect(InternetAddress.loopbackIPv4, server.port);
      final peer = await accepted;
      await server.close().timeout(const Duration(seconds: 3));
      client.add(Uint8List.fromList([0, 5, 72, 69]));
      await client.flush();
      final clientClosed = client.close();
      final bytes = <int>[];
      await for (final chunk in peer.timeout(const Duration(seconds: 3))) {
        bytes.addAll(chunk);
      }
      peer.destroy();
      await clientClosed.timeout(const Duration(seconds: 3));
      if (bytes.length != 4) throw StateError('unexpected byte count ${bytes.length}');
      break;
    case 'refused-connect':
      final temporary = await ServerSocket.bind(InternetAddress.loopbackIPv4, 0);
      final port = temporary.port;
      await temporary.close().timeout(const Duration(seconds: 3));
      var refused = false;
      try {
        final unexpected = await Socket.connect(
          InternetAddress.loopbackIPv4,
          port,
          timeout: const Duration(seconds: 2),
        );
        unexpected.destroy();
      } on SocketException {
        refused = true;
      }
      if (!refused) throw StateError('expected refused connection');
      break;
    default:
      throw ArgumentError.value(mode, 'mode', 'unknown diagnostic mode');
  }
  stdout.writeln('F006_AB_BODY_DONE mode=$mode natural_exit_expected=true');
}
