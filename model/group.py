class Group:

    def __init__(self, baseUrl=None, lenovo=None, dell=None, hp=None,
                 diagonal_from=None, diagonal_to=None, menu=None, sub_menu=None,
                 price_from=None, price_to=None):
        self.baseUrl = baseUrl
        self.lenovo = lenovo
        self.dell = dell
        self.hp = hp
        self.diagonal_from = diagonal_from
        self.diagonal_to = diagonal_to
        self.sub_menu = sub_menu
        self.menu = menu
        self.price_from = price_from
        self.price_to = price_to


    def __repr__(self):
        return "%s:%s;%s;" % self.baseUrl, \
               self.lenovo, self.dell, self.hp,\
               self.diagonal_from, self.diagonal_to, \
               self.menu, self.sub_menu, \
               self.price_from, self.price_to

