import 'package:http/http.dart' as http;
import 'person.dart';

class PostsRepository {
  Future<List<Welcome>> getPosts() async {
    final response = await http.get("http://192.168.0.103:8000/api/patients");
    return welcomeFromJson(response.body);
  }
}