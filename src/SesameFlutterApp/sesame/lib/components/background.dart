import 'package:flutter/material.dart';

class Background extends StatelessWidget {
  final Widget child;

  const Background({
    Key key,
    @required this.child,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;

    return Container(
      width: double.infinity,
      height: size.height,
      child: Stack(
        alignment: Alignment.center,
        children: <Widget>[
          Align(
            alignment: Alignment.topRight,
            child: Image.asset("assets/images/top1.png", width: size.width),
          ),
          Align(
            alignment: Alignment.topRight,
            child: Image.asset("assets/images/top2.png", width: size.width),
          ),
          Positioned(
            top: 50,
            right: 30,
            child: Image.asset("assets/images/main.png",
                width: size.width / (5.5)),
          ),
          Align(
            alignment: Alignment.bottomLeft,
            child: Image.asset("assets/images/bottom1.png", width: size.width),
          ),
          Align(
            alignment: Alignment.bottomLeft,
            child: Image.asset("assets/images/bottom2.png", width: size.width),
          ),
          child
        ],
      ),
    );
  }
}
