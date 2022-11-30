class Stadium:
  def __init__(self, id, name, capacity, location, restaurants): ### colocar el id del estadio
    self.id = id
    self.name = name
    self.capacity = capacity
    self.location = location
    self.restaurants = restaurants

  def get_capacity(self): ##acomodar por el ajuste
    capacity = self.capacity
    total = capacity[0]+capacity[1]
    x = total//10
    y = 10
    return x, y
    
  def show_stadium(self):
    print(f'''
    ID: {self.id}
    Name: {self.name}
    Location: {self.location}
    '''
    )
    