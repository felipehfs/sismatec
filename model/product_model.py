class Product(object):

    def __init__(self, name, price, qtd, code=None):
        self.name = name
        self.price = price
        self.qtd = qtd
        self.code = code

    def __str__(self):
        return "{} {} {} {}".format(self.code, self.name, self.price, self.qtd)
