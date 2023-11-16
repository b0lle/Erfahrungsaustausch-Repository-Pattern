class ProductService:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_all_products(self):
        return self.products

product_service = ProductService()
product_service.add_product('Product 1')
product_service.add_product('Product 2')
print(product_service.get_all_products())
