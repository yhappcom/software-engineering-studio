import 'dart:convert';
import 'dart:io';

Future<void> main(List<String> args) async {
  if (args.length == 2 && args[0] == '--child') {
    await childMain(Directory(args[1]));
    return;
  }

  final root = await Directory.systemTemp.createTemp('d005_dart_publish_');
  try {
    final published = File('${root.path}/published.json');
    final candidate = File('${root.path}/candidate.tmp');
    final marker = File('${root.path}/candidate-ready');

    await published.writeAsString(jsonEncode({'generation': 1, 'rows': 10}), flush: true);
    final before = await published.readAsString();

    final child = await Process.start(
      Platform.resolvedExecutable,
      [Platform.script.toFilePath(), '--child', root.path],
    );

    final deadline = DateTime.now().add(const Duration(seconds: 10));
    while (!await marker.exists()) {
      if (DateTime.now().isAfter(deadline)) {
        child.kill(ProcessSignal.sigkill);
        throw StateError('child did not reach candidate-ready boundary');
      }
      await Future<void>.delayed(const Duration(milliseconds: 20));
    }

    if (!await candidate.exists()) throw StateError('candidate missing');
    final candidateState = jsonDecode(await candidate.readAsString()) as Map<String, dynamic>;
    if (candidateState['generation'] != 2 || candidateState['rows'] != 200) {
      throw StateError('candidate semantic state invalid: $candidateState');
    }

    child.kill(ProcessSignal.sigkill);
    final exitCode = await child.exitCode;
    if (exitCode == 0) throw StateError('failure injection did not terminate child');

    final afterKill = await published.readAsString();
    if (afterKill != before) {
      throw StateError('published artifact changed before publication boundary');
    }
    final oldState = jsonDecode(afterKill) as Map<String, dynamic>;
    if (oldState['generation'] != 1 || oldState['rows'] != 10) {
      throw StateError('old publication semantic state invalid: $oldState');
    }

    await candidate.rename(published.path);
    if (await candidate.exists()) throw StateError('candidate still exists after rename');
    final newState = jsonDecode(await published.readAsString()) as Map<String, dynamic>;
    if (newState['generation'] != 2 || newState['rows'] != 200) {
      throw StateError('published replacement semantic state invalid: $newState');
    }

    stdout.writeln('D005_DART_CANDIDATE_PUBLICATION_TRANSFER_PASS');
    stdout.writeln('child_exit=$exitCode');
    stdout.writeln('old_generation=${oldState['generation']} old_rows=${oldState['rows']}');
    stdout.writeln('new_generation=${newState['generation']} new_rows=${newState['rows']}');
  } finally {
    if (await root.exists()) await root.delete(recursive: true);
  }
}

Future<void> childMain(Directory root) async {
  final candidate = File('${root.path}/candidate.tmp');
  final marker = File('${root.path}/candidate-ready');
  await candidate.writeAsString(jsonEncode({'generation': 2, 'rows': 200}), flush: true);
  await marker.writeAsString('ready', flush: true);
  // Hold the process after a complete private candidate exists but before publication.
  await Future<void>.delayed(const Duration(minutes: 5));
}
