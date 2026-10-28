import 'package:flutter/material.dart';
import 'package:my_app/models/product.dart';

/// Form that builds a product and hands it to whoever uses it.
class ProductForm extends StatefulWidget {
  final Function(Product) onAdd;

  const ProductForm({super.key, required this.onAdd});

  @override
  State<ProductForm> createState() => _ProductFormState();
}

class _ProductFormState extends State<ProductForm> {
  final _nameController = TextEditingController();
  final _quantityController = TextEditingController();
  bool _showError = false;

  void _submit() {
    final quantity = int.tryParse(_quantityController.text);
    if (_nameController.text.isEmpty || quantity == null) {
      setState(() {
        _showError = true;
      });
      return;
    }
    widget.onAdd(Product(name: _nameController.text, quantity: quantity));
    _nameController.clear();
    _quantityController.clear();
    setState(() {
      _showError = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        TextField(
          controller: _nameController,
          decoration: const InputDecoration(labelText: 'Producto'),
        ),
        TextField(
          controller: _quantityController,
          keyboardType: TextInputType.number,
          decoration: const InputDecoration(labelText: 'Cantidad'),
        ),
        if (_showError)
          const Text(
            'Escribe el producto y una cantidad',
            style: TextStyle(color: Colors.red),
          ),
        FilledButton(onPressed: () => _submit(), child: const Text('Agregar')),
      ],
    );
  }

  @override
  void dispose() {
    _nameController.dispose();
    _quantityController.dispose();
    super.dispose();
  }
}
