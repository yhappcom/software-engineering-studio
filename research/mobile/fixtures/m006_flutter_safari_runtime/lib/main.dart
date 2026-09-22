import 'dart:async';
import 'dart:html' as html;
import 'package:flutter/material.dart';

void main() {
  html.document.title = 'M006_BOOT';
  runApp(const RuntimeProbe());
  Timer(const Duration(milliseconds: 750), () {
    html.document.title = 'M006_ASYNC_READY';
  });
}

class RuntimeProbe extends StatelessWidget {
  const RuntimeProbe({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: Scaffold(
        body: Center(child: Text('Flutter Safari runtime probe')),
      ),
    );
  }
}
