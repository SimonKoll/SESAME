import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    return Scaffold(
        body: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: <Widget>[
          //Center(
          //child:
          Container(
            //margin: EdgeInsets.only(top: 100, left: 0, right: 0),
            child: Container(
              child: Text(
                "Livestream",
                style: TextStyle(
                  fontFamily: "SlimJoe",
                  color: Color.fromRGBO(93, 173, 226, 1),
                  fontSize: 36,
                ),
                textAlign: TextAlign.center,
                //TextAlign: TextAlign.center,
              ),
            ),
          ),
          SizedBox(height: size.height * 0.03),
          Container(
              child: Center(
            child: Container(
              height: 250.0,
              width: 350.0,
              alignment: Alignment.center,
              decoration: BoxDecoration(
                image: DecorationImage(
                  image: AssetImage('assets/images/streamNA.png'),
                  fit: BoxFit.fill,
                ),
              ),
            ),
          )),
          SizedBox(height: size.height * 0.03),
          Container(
            //margin: EdgeInsets.only(top: 100, left: 0, right: 0),
            child: Container(
              child: Text(
                "Latest Snapshots",
                style: TextStyle(
                  fontFamily: "SlimJoe",
                  color: Color.fromRGBO(93, 173, 226, 1),
                  fontSize: 32,
                ),
                textAlign: TextAlign.center,
                //TextAlign: TextAlign.center,
              ),
            ),
          ),
          SizedBox(height: size.height * 0.03),
          Container(
              child: Center(
            child: Container(
              height: 250.0,
              width: 350.0,
              alignment: Alignment.center,
              decoration: BoxDecoration(
                image: DecorationImage(
                  image: AssetImage('assets/images/snaps.png'),
                  fit: BoxFit.fill,
                ),
              ),
            ),
          )),
        ]));
  }
}
