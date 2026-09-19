import 'dart:io';

Future<void> main(List<String> args) async {
  final mode = args.isEmpty ? 'parent' : args.first;
  if (mode == 'child') {
    stdout.writeln('child:${pid}:stdout');
    stderr.writeln('child:${pid}:stderr');
    exitCode = 7;
    return;
  }

  final self = Platform.resolvedExecutable;
  final script = Platform.script.toFilePath();
  final result = await Process.run(self, [script, 'child']);
  if (result.exitCode != 7) throw StateError('exit=${result.exitCode}');
  if (!result.stdout.toString().contains(':stdout')) throw StateError('stdout boundary missing');
  if (!result.stderr.toString().contains(':stderr')) throw StateError('stderr boundary missing');
  stdout.writeln('F001_OK runtime=${Platform.version.split(' ').first} parent=$pid childExit=${result.exitCode}');
}
