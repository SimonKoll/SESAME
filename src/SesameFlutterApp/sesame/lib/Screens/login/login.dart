import 'package:Sesame/Screens/home/home.dart';
import 'package:flutter/material.dart';
import 'package:Sesame/Screens/register/register.dart';
import 'package:Sesame/components/background.dart';

class LoginScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;

    return Scaffold(
      body: Background(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Container(
              alignment: Alignment.centerLeft,
              padding: EdgeInsets.symmetric(horizontal: 40),
              child: Text(
                "LOGIN",
                style: TextStyle(
                    fontFamily: "BigJohn",
                    color: Color.fromRGBO(93, 173, 226, 1),
                    fontSize: 36),
                textAlign: TextAlign.left,
              ),
            ),
            SizedBox(height: size.height * 0.03),
            Container(
                alignment: Alignment.center,
                margin: EdgeInsets.symmetric(horizontal: 40),
                child: TextField(
                  keyboardType: TextInputType.emailAddress,
                  decoration: InputDecoration(labelText: "Email"),
                  style: TextStyle(
                    fontFamily: "SlimJoe",
                    fontWeight: FontWeight.bold,
                  ),
                )),
            SizedBox(height: size.height * 0.03),
            Container(
                alignment: Alignment.center,
                margin: EdgeInsets.symmetric(horizontal: 40),
                child: TextField(
                  decoration: InputDecoration(labelText: "Password"),
                  obscureText: true,
                  style: TextStyle(
                    fontFamily: "SlimJoe",
                    fontWeight: FontWeight.bold,
                  ),
                )),
            Container(
              alignment: Alignment.centerRight,
              margin: EdgeInsets.symmetric(horizontal: 40, vertical: 10),
              child: Text(
                "Forgot your password?",
                style: TextStyle(
                    fontSize: 12,
                    color: Color.fromRGBO(93, 173, 226, 1),
                    decoration: TextDecoration.underline,
                    fontFamily: "BigJohn"),
              ),
            ),
            SizedBox(height: size.height * 0.05),
            Container(
              alignment: Alignment.centerRight,
              margin: EdgeInsets.symmetric(horizontal: 40, vertical: 10),
              child: RaisedButton(
                onPressed: () {},
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(80.0)),
                textColor: Colors.white,
                padding: const EdgeInsets.all(0),
                child: Container(
                  alignment: Alignment.center,
                  height: 50.0,
                  width: size.width * 0.5,
                  decoration: new BoxDecoration(
                      borderRadius: BorderRadius.circular(80.0),
                      gradient: new LinearGradient(colors: [
                        Color.fromRGBO(93, 173, 226, 1),
                        Color.fromRGBO(93, 221, 226, 1),
                      ])),
                  padding: const EdgeInsets.all(0),
                  child: GestureDetector(
                    onTap: () => {
                      Navigator.push(context,
                          MaterialPageRoute(builder: (context) => Home()))
                    },
                    child: Text(
                      "LOGIN",
                      textAlign: TextAlign.center,
                      style: TextStyle(
                          fontWeight: FontWeight.bold, fontFamily: "BigJohn"),
                    ),
                  ),
                ),
              ),
            ),
            Container(
              alignment: Alignment.centerRight,
              margin: EdgeInsets.symmetric(horizontal: 40, vertical: 10),
              child: GestureDetector(
                onTap: () => {
                  Navigator.push(context,
                      MaterialPageRoute(builder: (context) => RegisterScreen()))
                },
                child: Text(
                  "New to Sesame?",
                  style: TextStyle(
                      fontSize: 12,
                      fontWeight: FontWeight.bold,
                      color: Color.fromRGBO(93, 173, 226, 1),
                      fontFamily: "BigJohn"),
                ),
              ),
            )
          ],
        ),
      ),
    );
  }
}
