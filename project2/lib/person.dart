import 'dart:convert';

List<Welcome> welcomeFromJson(String str) => List<Welcome>.from(json.decode(str).map((x) => Welcome.fromJson(x)));

String welcomeToJson(List<Welcome> data) => json.encode(List<dynamic>.from(data.map((x) => x.toJson())));

class Welcome {
    Welcome({
        this.id,
        this.login,
        this.password,
        this.stepsNum,
    });

    int id;
    String login;
    String password;
    int stepsNum;

    factory Welcome.fromJson(Map<String, dynamic> json) => Welcome(
        id: json["id"],
        login: json["login"],
        password: json["password"],
        stepsNum: json["stepsNum"],
    );

    Map<String, dynamic> toJson() => {
        "id": id,
        "login": login,
        "password": password,
        "stepsNum": stepsNum,
    };
}
