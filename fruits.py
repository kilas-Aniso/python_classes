class Fruits:
    taste="sweet"
    def __init__(self,name,price,color):
        self.name=name
        self.price=price
        self.color=color
    def fruit_name(self):
        return f'{self.name}'
    def fruit_price(self):
        return f'{self.price}'
    def fruit_color(self):
        return f'{self.color}'

