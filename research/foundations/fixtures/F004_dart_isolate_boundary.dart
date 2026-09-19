import 'dart:async';
import 'dart:isolate';

void worker(SendPort parent) {
  final commands = ReceivePort();
  var counter = 0;
  parent.send(commands.sendPort);
  commands.listen((message) {
    final m = message as List<Object?>;
    final reply = m[0] as SendPort;
    final op = m[1] as String;
    if (op == 'inc') {
      counter++;
      reply.send(counter);
    } else if (op == 'get') {
      reply.send(counter);
    } else if (op == 'stop') {
      commands.close();
      reply.send(counter);
    }
  });
}

Future<Object?> request(SendPort workerPort, String op) async {
  final reply = ReceivePort();
  workerPort.send(<Object?>[reply.sendPort, op]);
  final result = await reply.first.timeout(const Duration(seconds: 2));
  reply.close();
  return result;
}

Future<void> main() async {
  final bootstrap = ReceivePort();
  final isolate = await Isolate.spawn(worker, bootstrap.sendPort,
      debugName: 'f004-worker');
  final workerPort = await bootstrap.first.timeout(const Duration(seconds: 2))
      as SendPort;
  bootstrap.close();

  final results = await Future.wait<Object?>([
    request(workerPort, 'inc'),
    request(workerPort, 'inc'),
    request(workerPort, 'inc'),
  ]);
  final finalCount = await request(workerPort, 'get');

  if (results.toSet().length != 3 ||
      !results.every((v) => v is int && v >= 1 && v <= 3) ||
      finalCount != 3) {
    isolate.kill(priority: Isolate.immediate);
    throw StateError('serialized owner invariant failed: results=$results final=$finalCount');
  }

  // Failure boundary: a ReceivePort is explicitly unsendable. This should
  // fail at the message boundary rather than silently creating shared mutable
  // port state across isolates.
  final unsendable = ReceivePort();
  var rejected = false;
  try {
    workerPort.send(<Object?>[unsendable]);
  } catch (_) {
    rejected = true;
  } finally {
    unsendable.close();
  }
  if (!rejected) {
    isolate.kill(priority: Isolate.immediate);
    throw StateError('expected unsendable ReceivePort rejection');
  }

  final stoppedAt = await request(workerPort, 'stop');
  if (stoppedAt != 3) {
    isolate.kill(priority: Isolate.immediate);
    throw StateError('unexpected stop state: $stoppedAt');
  }

  print('F004_DART_ISOLATE_PASS results=$results final=$finalCount unsendableRejected=$rejected');
}
