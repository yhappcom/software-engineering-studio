import AuthenticationServices
import Flutter
import UIKit

final class OfficialAppleSignInButtonFactory: NSObject, FlutterPlatformViewFactory {
  private let messenger: FlutterBinaryMessenger

  init(messenger: FlutterBinaryMessenger) {
    self.messenger = messenger
    super.init()
  }

  func createArgsCodec() -> FlutterMessageCodec & NSObjectProtocol {
    FlutterStandardMessageCodec.sharedInstance()
  }

  func create(
    withFrame frame: CGRect,
    viewIdentifier viewId: Int64,
    arguments args: Any?
  ) -> FlutterPlatformView {
    OfficialAppleSignInButtonView(
      frame: frame,
      viewIdentifier: viewId,
      arguments: args,
      messenger: messenger
    )
  }
}

final class OfficialAppleSignInButtonView: NSObject, FlutterPlatformView {
  private let container: UIView
  private let button: ASAuthorizationAppleIDButton
  private let channel: FlutterMethodChannel

  init(
    frame: CGRect,
    viewIdentifier viewId: Int64,
    arguments args: Any?,
    messenger: FlutterBinaryMessenger
  ) {
    let params = args as? [String: Any]
    let typeName = params?["type"] as? String ?? "continue"
    let styleName = params?["style"] as? String ?? "black"
    let cornerRadius = params?["cornerRadius"] as? CGFloat ?? 12

    let buttonType: ASAuthorizationAppleIDButton.ButtonType
    switch typeName {
    case "signIn":
      buttonType = .signIn
    case "signUp":
      buttonType = .signUp
    default:
      buttonType = .continue
    }

    let buttonStyle: ASAuthorizationAppleIDButton.Style
    switch styleName {
    case "white":
      buttonStyle = .white
    case "whiteOutline":
      buttonStyle = .whiteOutline
    default:
      buttonStyle = .black
    }

    self.container = UIView(frame: frame)
    self.button = ASAuthorizationAppleIDButton(
      authorizationButtonType: buttonType,
      authorizationButtonStyle: buttonStyle
    )
    self.channel = FlutterMethodChannel(
      name: "logmate/apple-sign-in-button/\(viewId)",
      binaryMessenger: messenger
    )

    super.init()

    button.cornerRadius = cornerRadius
    button.translatesAutoresizingMaskIntoConstraints = false
    container.addSubview(button)
    NSLayoutConstraint.activate([
      button.leadingAnchor.constraint(equalTo: container.leadingAnchor),
      button.trailingAnchor.constraint(equalTo: container.trailingAnchor),
      button.topAnchor.constraint(equalTo: container.topAnchor),
      button.bottomAnchor.constraint(equalTo: container.bottomAnchor),
    ])
    button.addTarget(self, action: #selector(pressed), for: .touchUpInside)
  }

  func view() -> UIView {
    container
  }

  @objc private func pressed() {
    channel.invokeMethod("pressed", arguments: nil)
  }
}
