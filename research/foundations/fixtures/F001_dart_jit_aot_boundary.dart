import 'dart:io';

// F001 hosted validation: exercise the same process/I/O contract under Dart JIT and AOT.
Future<void> main(List<String> args) async {
  final mode = args.isEmpty ? 'parent' : args.first;
  if (mode == 'child') {
    stdout.writeln('child:${pid}:stdout');
    stderr.writeln('child:${pid}:stderr');
    exitCode = 7;
    return;
  }

  final executable = Platform.resolvedExecutable;
  final script = Platform.script.toFilePath();

  // Under JIT, resolvedExecutable is the Dart VM and the script path must be
  // supplied. In an AOT executable, Platform.script resolves to the executable
  // itself, so supplying it as argv[0] would recursively re-enter parent mode.
  final childArgs = executable == script ? <String>['child'] : <String>[script, 'child'];
  final result = await Process.run(executable, childArgs);

  if (result.exitCode != 7) throw StateError('exit=${result.exitCode}');
  if (!result.stdout.toString().contains(':stdout')) {
    throw StateError('stdout boundary missing');
  }
  if (!result.stderr.toString().contains(':stderr')) {
    throw StateError('stderr boundary missing');
  }
  stdout.writeln(
    'F001_OK runtime=${Platform.version.split(' ').first} parent=$pid childExit=${result.exitCode}',
  );
}
