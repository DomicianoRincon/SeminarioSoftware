import 'package:flutter/material.dart';

/// Card that summarizes a contact.
class ContactCard extends StatelessWidget {
  final String image;
  final String name;
  final String username;

  const ContactCard({
    super.key,
    required this.image,
    required this.name,
    required this.username,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 8,
      color: Colors.white,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(10),
        side: const BorderSide(color: Color(0xFFDCDDE6), width: 1.5),
      ),
      child: Padding(
        padding: EdgeInsets.all(8),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          spacing: 4,
          children: [
            CircleAvatar(radius: 28, backgroundImage: NetworkImage(image)),
            Text(
              name,
              style: const TextStyle(
                fontSize: 15,
                fontWeight: FontWeight.w600,
                color: Color(0xFF1B1B2A),
              ),
            ),
            Text(
              '@$username',
              style: const TextStyle(fontSize: 13, color: Color(0xFF5B5E72)),
            ),
          ],
        ),
      ),
    );
  }
}
