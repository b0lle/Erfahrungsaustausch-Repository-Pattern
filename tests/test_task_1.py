from erfahrungsaustasuch_repository_pattern.task_1 import ProductService

class TestProductService:
    def test_add_product(self):
        product_service = ProductService()
        product_service.add_product('Product 1')
        product_service.add_product('Product 2')
        assert product_service.get_all_products() == ['Product 1', 'Product 2']
