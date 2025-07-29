import 'package:flutter/material.dart';
import 'package:camera/camera.dart';
import 'voice_helper.dart';

class ScannerScreen extends StatefulWidget {
  @override
  _ScannerScreenState createState() => _ScannerScreenState();
}

class _ScannerScreenState extends State<ScannerScreen> {
  CameraController? _controller;
  late List<CameraDescription> cameras;

  @override
  void initState() {
    super.initState();
    initCamera();
  }

  void initCamera() async {
    cameras = await availableCameras();
    _controller = CameraController(cameras[0], ResolutionPreset.medium);
    await _controller!.initialize();
    setState(() {});
  }

  void captureAndRecognize() async {
    final image = await _controller!.takePicture();
   
    String prediction = "Pikachu";
    String type = "Electric";

    VoiceHelper.speak("This is $prediction. Type: $type.");
  }

  @override
  Widget build(BuildContext context) {
    if (_controller == null || !_controller!.value.isInitialized) {
      return Center(child: CircularProgressIndicator());
    }
    return Scaffold(
      appBar: AppBar(title: Text("Pokédex Scanner")),
      body: Column(
        children: [
          AspectRatio(
            aspectRatio: _controller!.value.aspectRatio,
            child: CameraPreview(_controller!),
          ),
          ElevatedButton(
            onPressed: captureAndRecognize,
            child: Text("Scan Pokémon"),
          ),
        ],
      ),
    );
  }
}
