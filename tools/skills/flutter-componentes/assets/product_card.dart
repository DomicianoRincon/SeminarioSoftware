import 'package:flutter/material.dart';
import 'package:my_app/models/product.dart';

/// Card for a product: name, quantity and its actions.
class ProductCard extends StatelessWidget {
  final Product product;
  final Function() onTap;
  final Function() onToggleBought;
  final Function() onDelete;

  const ProductCard({
    super.key,
    required this.product,
    required this.onTap,
    required this.onToggleBought,
    required this.onDelete,
  });

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => onTap(),
      child: Container(
        margin: const EdgeInsets.only(bottom: 12),
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: const Color(0xFFDCDDE6)),
        ),
        child: Row(
          children: [
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    product.name,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    style: const TextStyle(
                      fontSize: 16,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  Text(
                    'Cantidad: ${product.quantity}',
                    style: const TextStyle(color: Colors.black54),
                  ),
                ],
              ),
            ),
            IconButton(
              onPressed: () => onToggleBought(),
              icon: Icon(
                product.isBought
                    ? Icons.check_circle
                    : Icons.radio_button_unchecked,
                color: Colors.green,
              ),
            ),
            IconButton(
              onPressed: () => onDelete(),
              icon: const Icon(Icons.delete_outline),
            ),
          ],
        ),
      ),
    );
  }
}
