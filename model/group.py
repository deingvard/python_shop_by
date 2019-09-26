class Group:

    def __init__(self, baseUrl=None, Lenovo=None, Dell=None, HP=None,
                 diagonal_from=None, diagonal_to=None, menu=None, sub_menu=None,
                 price_from=None, price_to=None):
        self.baseUrl = baseUrl
        self.Lenovo = Lenovo
        self.Dell = Dell
        self.HP = HP
        self.diagonal_from = diagonal_from
        self.diagonal_to = diagonal_to
        self.sub_menu = sub_menu
        self.menu = menu
        self.price_from = price_from
        self.price_to = price_to


    def __repr__(self):
        return "%s:%s;%s;" % self.baseUrl, \
               self.Lenovo, self.Dell, self.HP,\
               self.diagonal_from, self.diagonal_to, \
               self.menu, self.sub_menu, \
               self.price_from, self.price_to

