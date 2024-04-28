class Shop:
    def __init__(self, shop_name, shop_type, number_of_units=0, increment=0):
        self.name = shop_name
        self.type = shop_type
        self.units = number_of_units
        self.number_of_units = number_of_units
        self.increment = increment

    def __describe_shop__(self):
        print(f'Shop name: {self.name}')
        print(f'Shop type: {self.type}')
        print(f'Shop units: {self.units}')

    def __open_shop__(self):
        print(f'The {self.type} shop {self.name} has been opened.')

    def __set_number_of_units__(self):
        print(f"Number of units is: {self.number_of_units}")

    def __increment_number_of_unit__(self):
        print(f"Increment number of units is: {self.number_of_units + self.increment}")


store = Shop('Apple', 'Online')
print(store.__describe_shop__())
print(store.__open_shop__())
print(store.__describe_shop__(), store.__open_shop__())
shop_1 = Shop('Samsung', 'Offline')
shop_2 = Shop('Xiaomi', 'Online')
shop_3 = Shop('HTC', 'Offline')

print(shop_1.__describe_shop__())
print(shop_2.__describe_shop__())
print(shop_3.__describe_shop__())

storee = Shop('PlayStation', 'Online', 20, 20)
print(storee.__describe_shop__())
storee = Shop('PlayStation', 'Online', 50, 20)
print(storee.__describe_shop__())
print(storee.__set_number_of_units__())
print(storee.__increment_number_of_unit__())


class Discount(Shop):
    def __init__(self, shop_name, shop_type, discount_products):
        super().__init__(shop_name, shop_type)
        self.discount_products = discount_products

    def __get_discount_products__(self):
        print(self.discount_products)


store_discount = Discount('Hello', 'Samsung', ['watermelons', 'bananas', 'apples'])
print(store_discount.__get_discount_products__())
