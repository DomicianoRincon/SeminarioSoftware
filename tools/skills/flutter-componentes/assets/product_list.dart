import 'package:flutter/material.dart';
import 'package:my_app/components/product_card.dart';
import 'package:my_app/models/product.dart';

/// List of products, or a message when there are none.
class ProductList extends StatelessWidget {
  final List<Product> products;
  final Function(Product) onOpen;
  final Function(Product) onToggleBought;
  final Function(Product) onDelete;

  const ProductList({
    super.key,
    required this.products,
    required this.onOpen,
    required this.onToggleBought,
    required this.onDelete,
  });

  @override
  Widget build(BuildContext context) {
    if (products.isEmpty) {
      return const Padding(
        padding: EdgeInsets.all(24),
        child: Text(
          'Todavía no hay productos',
          style: TextStyle(color: Colors.grey),
        ),
      );
    }
    return Column(
      children: [
        for (final product in products)
          ProductCard(
            product: product,
            onTap: () => onOpen(product),
            onToggleBought: () => onToggleBought(product),
            onDelete: () => onDelete(product),
          ),
      ],
    );
  }
}
