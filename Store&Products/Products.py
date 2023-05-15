class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += self.price*percent_change
            return self
        else:
            self.price -= self.price*percent_change
            return self

    def print_info(self):
        print("name:", self.name, ",price:",
              self.price, ",category:", self.category)
        return self
