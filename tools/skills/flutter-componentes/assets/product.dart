/// A product in the shopping list.
class Product {
  final String name;
  final int quantity;
  final bool isBought;

  const Product({
    required this.name,
    required this.quantity,
    this.isBought = false,
  });

  Product copyWith({String? name, int? quantity, bool? isBought}) {
    return Product(
      name: name ?? this.name,
      quantity: quantity ?? this.quantity,
      isBought: isBought ?? this.isBought,
    );
  }
}
