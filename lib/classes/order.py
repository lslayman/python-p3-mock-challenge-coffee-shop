class Order:
    all = []

    # Coffee should be initialized with a customer, coffee, and a price (num)
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
        customer.orders(self)
        coffee.orders(self)
        customer.coffees(self.coffee)
        coffee.customers(self.customer)

    # Order property price
    # Returns coffee price, must be num between 1-10, inc
    @property
    def get_price(self):
        return self._price
    @get_price.setter
    def set_price(self, price):
        if isinstance(price, float) and 0 < price <= 10:
            self._price = price
        else:
            raise Exception("Price must be a number between 1 and 10.")
        