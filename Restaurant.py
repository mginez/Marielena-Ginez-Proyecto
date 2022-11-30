class Restaurant:
  def __init__(self, name):
    self.name = name
    
  def show_restaurant(self, list):
    print(f'''
    ID: {list.index(self)}
    Name: {self.name}''')