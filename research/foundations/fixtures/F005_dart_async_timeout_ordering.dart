import 'dart:async';

void expect(bool condition, String message) {
  if (!condition) throw StateError(message);
}

Future<void> main() async {
  // Property 1: a scheduled microtask runs before a zero-delay event.
  final ordering = <String>[];
  scheduleMicrotask(() => ordering.add('microtask'));
  Future<void>.delayed(Duration.zero, () => ordering.add('event'));
  await Future<void>.delayed(const Duration(milliseconds: 20));
  expect(ordering.length == 2, 'ordering trace incomplete: $ordering');
  expect(ordering[0] == 'microtask' && ordering[1] == 'event',
      'documented microtask/event relation violated: $ordering');

  // Property 2: Future.timeout stops waiting on the timeout future; it does
  // not cancel the source future. The source must still complete its effect.
  var sourceEffect = false;
  final source = Future<String>.delayed(const Duration(milliseconds: 80), () {
    sourceEffect = true;
    return 'source-complete';
  });

  var timedOut = false;
  try {
    await source.timeout(const Duration(milliseconds: 10));
  } on TimeoutException {
    timedOut = true;
  }
  expect(timedOut, 'timeout future did not time out');
  expect(!sourceEffect, 'source completed before timeout observation');
  final sourceResult = await source;
  expect(sourceResult == 'source-complete' && sourceEffect,
      'source future did not complete after waiter timeout');

  // Property 3: cancellation semantics belong to the concrete API. For a
  // StreamSubscription, await cancel() and assert that later controller adds
  // are not delivered to this subscription.
  final controller = StreamController<int>();
  final seen = <int>[];
  final subscription = controller.stream.listen(seen.add);
  controller.add(1);
  await Future<void>.delayed(Duration.zero);
  await subscription.cancel();
  controller.add(2);
  await Future<void>.delayed(Duration.zero);
  await controller.close();
  expect(seen.length == 1 && seen.single == 1,
      'cancelled subscription received later events: $seen');

  print('F005_DART_ASYNC_PASS ordering=$ordering timeout=$timedOut '
      'sourceEffect=$sourceEffect seen=$seen');
}
