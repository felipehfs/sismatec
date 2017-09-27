class Product(object):

    def __init__(self, name, price, quatity, code=None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.code = code

    def __str__(self):
        return "{} {} {} {}".format(self.code, self.name, self.price, self.quantity)
