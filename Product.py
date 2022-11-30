class Product:
  def __init__(self, name, quantity, price, type):
    self.name = name
    self.quantity = quantity
    self.price = price + (price*0.16)
    self.type = type
    self.sold = 0
  def show_product(self):
    print(f'''
  - Name: {self.name}
  - Price: {self.price}
  - Sold: {self.sold}
    ''')
    
    
class Food(Product):
  def __init__(self, name, quantity, price, type, packaging): ### ''
    super().__init__(name, quantity, price, type) 
    self.packaging = packaging
  def show_food(self):
    print(f'''
  - Name: {self.name}
  - Price: {self.price}
  - Packaging: {self.packaging}
    ''')

class Beverage(Product):
  def __init__(self, name, quantity, price, type, is_alcoholic):
    super().__init__(name, quantity, price, type)
    self.is_alcoholic = is_alcoholic
  def show_beverage(self):
    print(f'''
  - Name: {self.name}
  - Price: {self.price}
  - Is Alcoholic: {self.is_alcoholic}
    ''')
