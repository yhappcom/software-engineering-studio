import 'dart:collection';

int expectedChecksum(int n) => n * (n - 1) ~/ 2;

({int checksum, int micros}) drainList(int n) {
  final values = List<int>.generate(n, (i) => i, growable: true);
  var checksum = 0;
  final sw = Stopwatch()..start();
  while (values.isNotEmpty) {
    checksum += values.removeAt(0);
  }
  sw.stop();
  return (checksum: checksum, micros: sw.elapsedMicroseconds);
}

({int checksum, int micros}) drainQueue(int n) {
  final values = ListQueue<int>.from(Iterable<int>.generate(n));
  var checksum = 0;
  final sw = Stopwatch()..start();
  while (values.isNotEmpty) {
    checksum += values.removeFirst();
  }
  sw.stop();
  return (checksum: checksum, micros: sw.elapsedMicroseconds);
}

void main() {
  const sizes = [5000, 10000, 20000, 40000];
  final rows = <String>[];

  for (final n in sizes) {
    final list = drainList(n);
    final queue = drainQueue(n);
    final expected = expectedChecksum(n);

    if (list.checksum != expected || queue.checksum != expected) {
      throw StateError(
        'FIFO semantic oracle failed for n=$n: '
        'list=${list.checksum}, queue=${queue.checksum}, expected=$expected',
      );
    }

    rows.add(
      'n=$n list_us=${list.micros} queue_us=${queue.micros} '
      'checksum=$expected',
    );
  }

  // Failure-boundary oracle: List.removeAt(0) changes every later index,
  // while ListQueue.removeFirst() advances the queue head while preserving FIFO.
  final list = <int>[0, 1, 2, 3];
  final queue = ListQueue<int>.from(list);
  final listFirst = list.removeAt(0);
  final queueFirst = queue.removeFirst();
  if (listFirst != 0 || queueFirst != 0 ||
      list.join(',') != '1,2,3' || queue.join(',') != '1,2,3') {
    throw StateError('front-removal semantic boundary failed');
  }

  print('F003_DART_QUEUE_PASS');
  for (final row in rows) {
    print(row);
  }
  print('NOTE timing observations are diagnostic only; complexity verdict comes '
      'from the documented operation contracts, not a timing threshold.');
}
