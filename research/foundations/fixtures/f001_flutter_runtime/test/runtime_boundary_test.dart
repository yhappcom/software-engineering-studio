import 'package:flutter/widgets.dart';
import 'package:flutter_test/flutter_test.dart';

class BoundaryProbe extends StatefulWidget {
  const BoundaryProbe({super.key});

  @override
  State<BoundaryProbe> createState() => _BoundaryProbeState();
}

class _BoundaryProbeState extends State<BoundaryProbe> {
  int count = 0;

  @override
  Widget build(BuildContext context) {
    return Directionality(
      textDirection: TextDirection.ltr,
      child: GestureDetector(
        onTap: () => setState(() => count++),
        child: Text('count=$count', key: const Key('counter')),
      ),
    );
  }
}

void main() {
  testWidgets('framework state transition crosses pump boundary', (tester) async {
    await tester.pumpWidget(const BoundaryProbe());
    expect(find.text('count=0'), findsOneWidget);

    await tester.tap(find.byKey(const Key('counter')));
    // setState marks the element dirty; the observable rendered widget tree does
    // not advance until the test binding pumps the next frame.
    expect(find.text('count=0'), findsOneWidget);

    await tester.pump();
    expect(find.text('count=1'), findsOneWidget);
  });
}
