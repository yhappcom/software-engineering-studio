import 'dart:io';

Never _fail(String message) => throw StateError(message);

void main() {
  // Identity + mutable aliasing: two bindings designate the same mutable object.
  final original = <String, Object>{
    'nested': <int>[100],
  };
  final alias = original;
  if (!identical(alias, original)) _fail('direct alias lost object identity');
  (alias['nested']! as List<int>)[0] = 101;
  if ((original['nested']! as List<int>)[0] != 101) {
    _fail('alias mutation was not visible through original');
  }

  // final constrains rebinding, not mutation of the designated mutable object.
  final mutable = <int>[1];
  mutable.add(2);
  if (mutable.length != 2) _fail('final-bound mutable list did not mutate');

  // Shallow structural copy is a distinct outer object but retains nested aliasing.
  final shallow = Map<String, Object>.from(original);
  if (identical(shallow, original)) _fail('shallow copy reused outer map identity');
  if (!identical(shallow['nested'], original['nested'])) {
    _fail('bounded shallow-copy oracle expected nested aliasing');
  }
  (shallow['nested']! as List<int>)[0] = 102;
  if ((original['nested']! as List<int>)[0] != 102) {
    _fail('shallow nested mutation did not reach original');
  }

  // Explicit graph copy isolates this deliberately simple nested graph.
  final isolated = <String, Object>{
    'nested': List<int>.from(original['nested']! as List<int>),
  };
  (isolated['nested']! as List<int>)[0] = 999;
  if ((original['nested']! as List<int>)[0] == 999) {
    _fail('explicit nested copy failed to isolate bounded graph');
  }

  // Resource lifetime: explicit close is an observable contract independent of GC.
  final temp = File('${Directory.systemTemp.path}/f002_${pid}_${DateTime.now().microsecondsSinceEpoch}.txt');
  final handle = temp.openSync(mode: FileMode.write);
  handle.writeStringSync('owned');
  handle.closeSync();
  var closeRejected = false;
  try {
    handle.writeStringSync('after-close');
  } on FileSystemException {
    closeRejected = true;
  } on StateError {
    closeRejected = true;
  }
  if (!closeRejected) _fail('write after explicit close was not rejected');
  if (temp.readAsStringSync() != 'owned') _fail('explicit-close file content mismatch');
  temp.deleteSync();

  print('F002_DART_IDENTITY_LIFETIME_PASS '
      'alias=true finalMutable=true shallowNestedAlias=true '
      'explicitCopyIsolation=true explicitClose=true');
}
