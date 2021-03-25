import 'package:flutter/material.dart';
import '/posts_repo.dart';
import 'person.dart';
void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: HomeScreen(),
    );
  }
}
class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('test'),
      ),
      body: FutureBuilder<List<Welcome>>(
        future: PostsRepository().getPosts(),
        builder: (context, snapshot) {
          if (snapshot.hasError) {
            showDialog(
              builder: (context) => AlertDialog(
                title: Text("Error"),
                content: Text(snapshot.error.toString()),
              ), context: context,
            );
          } else if (snapshot.hasData) {
            return ListView.builder(
              itemCount: snapshot.data.length,
              itemBuilder: (context, index) => ListTile(
                title: Text(snapshot.data[index].login),
                subtitle: Text(
                  snapshot.data[index].password,
                  softWrap: false,
                  overflow: TextOverflow.ellipsis,
                ),
              ),
            );
          }
          return Center(
            child: CircularProgressIndicator(),
          );
        },
      ),
    );
  }
}