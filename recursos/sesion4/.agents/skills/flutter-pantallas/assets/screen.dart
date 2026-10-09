import 'package:flutter/material.dart';
import 'package:mi_app_1/components/profile_info.dart';
import 'package:mi_app_1/components/stats_row.dart';

/// Profile of a person.
class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Perfil')),
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(16),
          child: Column(
            spacing: 16,
            children: [
              ProfileInfo(
                image: 'https://picsum.photos/400',
                name: 'Mariana Valenzuela',
                username: 'marianav',
                role: 'Diseñadora de Producto',
                email: 'm.val@estudio.com',
                location: 'Cali, CO',
              ),
              StatsRow(posts: '128', followers: '2.4k', following: '310'),
            ],
          ),
        ),
      ),
    );
  }
}
