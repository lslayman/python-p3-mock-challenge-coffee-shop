class Coffee:
    all = []

    # Coffee should be initialized with a name, as a string
    def __init__(self, name):
        self.name = name
        self._customers = []
        self._orders = []


    # Coffee property name
    # Returns name which should not be able to change after being created
    # Hint: use hasattr()
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and not hasattr(self, 'name'):
            self._name = name
        else:
            raise Exception
        
    name = property(get_name, set_name)

    # Adds new orders to coffee & returns list of all orders for that coffee
    def orders(self, new_order=None):
        from classes.order import Order
        if new_order and isinstance(new_order, Order):
            self._orders.append(new_order)
        return self._orders
    
    # Adds new customers and returns UNIQUE list of customers who have ordered a particular coffee
    def customers(self, new_customer=None):
        from classes.customer import Customer
        if new_customer and isinstance(new_customer, Customer) and new_customer not in self._customers:
            self._customers.append(new_customer)
        return self._customers
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        return sum([order.price for order in self._orders]) / len(self._orders)
        