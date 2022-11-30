class Team:
  def __init__(self, country, flag, code, group, id): ### colocar el id del equipo probs
    self.country = country
    self.flag = flag
    self.code = code
    self.group = group
    self.id = id
  def show_team(self):
    print(f'''
      ID: {self.id}
      Country: {self.country}
      Flag: {self.flag}
      FIFA Code: {self.code}
      Group: {self.group}
      '''
    )