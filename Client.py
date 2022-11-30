class Client:
  def __init__(self, name, id, age):
    self.name = name
    self.id = id
    self.age = age
    self.sold_tickets = 0

  def show_client(self):
    print(
      f'''
      Name: {self.name}
      ID: {self.id}
      Purchased Tickets: {self.sold_tickets}''')
    

class Ticket(Client):
  def __init__(self, name, id, age, match, ticket_type, seat, cost):
    super().__init__(name, id, age)
    self.match = match
    self.ticket_type = ticket_type
    self.seat = seat
    self.cost = cost
    self.iva = cost * 0.16
    self.qrcode = ''
    self.total = 0
    
  def show_receipt(self):
    
    print(
      f'''
      
      ************ RECEIPT ************
    
      Client Data:
      Name: {self.name}
      ID: {self.id}
      Age: {self.age}
      '''
    )
    print(
      f'''
      Ticket:
      - Type: {self.ticket_type}
      - Match: {self.match}
      - Seat: {self.seat}
      '''
    )
    
    print(
      f'''
      ------------------------------
      Subtotal: {self.cost}
      IVA: {self.iva}'''
    )
    