class Customer:

    # Customer should be initialized with a name
    def __init__(self, name):
        self.name = name
        self._orders = []
        self._coffees = []

    # Customer property name
    # Return name as a str between 1 and 15 char, inc
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <=15:
            self._name = name
        else:
            raise Exception("Name length must be between 1 and 15 characters.")
        
    name = property(get_name, set_name)

    # Adds new orders to customer & returns a list of all orders a customer has ordered
    def orders(self, new_order=None):
        from classes.order import Order
        if new_order and isinstance(new_order, Order):
            self._orders.append(new_order)
        return self._orders
    
    # Adds new coffees to customer & returns UNIQUE list of all coffees customer has ordered
    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        if new_coffee and isinstance(new_coffee, Coffee) and new_coffee not in self._coffees:
            self._coffees.append(new_coffee)
        return self._coffees
    
    def create_order(self, coffee, price):
        order_details = {coffee, price}
        self.create_order.append(order_details)