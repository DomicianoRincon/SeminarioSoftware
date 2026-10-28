import 'package:flutter/material.dart';
import 'package:my_app/components/product_form.dart';
import 'package:my_app/components/product_list.dart';
import 'package:my_app/models/product.dart';

/// Screen that owns the shopping list.
class ShoppingScreen extends StatefulWidget {
  const ShoppingScreen({super.key});

  @override
  State<ShoppingScreen> createState() => _ShoppingScreenState();
}

class _ShoppingScreenState extends State<ShoppingScreen> {
  final List<Product> _products = [];

  void _addProduct(Product product) {
    setState(() {
      _products.add(product);
    });
  }

  void _toggleBought(Product product) {
    setState(() {
      final index = _products.indexOf(product);
      _products[index] = product.copyWith(isBought: !product.isBought);
    });
  }

  void _deleteProduct(Product product) {
    setState(() {
      _products.remove(product);
    });
  }

  void _openProduct(Product product) {
    Navigator.pushNamed(context, '/product', arguments: product);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Lista de compras')),
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(16),
          child: Column(
            children: [
              ProductForm(onAdd: (product) => _addProduct(product)),
              ProductList(
                products: _products,
                onOpen: (product) => _openProduct(product),
                onToggleBought: (product) => _toggleBought(product),
                onDelete: (product) => _deleteProduct(product),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
