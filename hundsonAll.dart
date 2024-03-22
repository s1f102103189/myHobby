import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Home(),
    );
  }
}

class Home extends StatelessWidget {
  Home({
    Key? key,
  }) : super(key: key);

  final List<Map<String, String>> item = [
    {'title': '出身地', 'description': '埼玉県八潮市'},
    {'title': '経歴', 'description': '八潮市立大原中学校　昌平高校　東洋大学'},
    {'title': '好きなゲーム', 'description': '鉄拳'},
    {'title': '使用言語', 'description': 'Python PHP C Dart'},
    {'title': '好きなタイプ', 'description': '明るい人'},
    {'title': '一言', 'description': 'インターンシップ募集中！'},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: CustomScrollView(
        slivers: [
          SliverAppBar(
            title: const Text('★小山翔矢★', style: TextStyle(color: Colors.white)),
            backgroundColor: Colors.purple,
            expandedHeight: 400.0,
            flexibleSpace: FlexibleSpaceBar(
              background: Image.network(
                'https://1.bp.blogspot.com/-VACf4WfKNOk/X-Fcx7DWraI/AAAAAAABdE8/KT0UudaIHrMtbFvjC02yLuPLNBZurGYpQCNcBGAsYHQ/s1103/onepiece17_doflamingo.png',
                fit: BoxFit.cover,
              ),
            ),
            pinned: true,
          ),
          SliverGrid(
            gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
              crossAxisCount: 2,
              mainAxisSpacing: 10.0,
              crossAxisSpacing: 10.0,
            ),
            delegate: SliverChildBuilderDelegate(
              (BuildContext context, int index) {
                final cardColor = index % 2 == 0 ? 0xfffce4ec : 0xfff3e5f5;
                return InkWell(
                  onTap: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (context) => CreatePage(item: item[index])),
                    );
                  },
                  child: Card(
                    color: Color(cardColor),
                    child: Padding(
                      padding: const EdgeInsets.all(10.0),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            item[index]['title']!,
                            style: const TextStyle(
                              fontSize: 12,
                            ),
                          ),
                          const Divider(),
                          Text(item[index]['description']!),
                        ],
                      ),
                    ),
                  ),
                );
              },
              childCount: item.length,
            ),
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {},
        heroTag: 'next',
        backgroundColor: Colors.purple,
        child: const Icon(Icons.person_add),
      ),
      bottomNavigationBar: BottomNavigationBar(
        backgroundColor: Colors.purple,
        selectedItemColor: Colors.white,
        items: const [
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: 'ホーム',
          ),
          BottomNavigationBarItem(icon: Icon(Icons.people), label: 'Friends'),
          BottomNavigationBarItem(icon: Icon(Icons.settings), label: '設定'),
        ],
      ),
    );
  }
}

class CreatePage extends StatelessWidget {
  CreatePage({Key? key, required this.item}) : super(key: key);
  Map<String, String> item;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(item['title']!),
      ),
      body: Center(
        child: ElevatedButton(
          child: Text('戻る'),
          onPressed: () {
            Navigator.pop(context);
          },
        ),
      ),
    );
  }
}



