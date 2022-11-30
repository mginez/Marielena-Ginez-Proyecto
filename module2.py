#Tickets Sale Management

###imports##################################
import random
from colorama import init, Back
from EDD import objects_matches, edd_matches, objects_stadiums, edd_stadiums
from Match import Match
from Stadium import Stadium
from Client import Client, Ticket
from map import map
from functions import is_vampire
import os
from data import unused_qrcodes, clients_db, clients_VIP_db, tickets

###funciones##################################
clear_screen = lambda: os.system ("cls")

def display_matches(match_list):
  for match in match_list:
    Match.show_match(match)

def get_discount(client, ticket):
  discount = 0
  if is_vampire(client.id):
    discount = ticket.cost * 0.50
  return round(discount,2)

def print_receipt(ticket, discount, total):
  if discount != 0:
    print(f'''
                    {Back.MAGENTA} CONGRATULATIONS! YOU GOT A 50% DISCOUNT''')
  Ticket.show_receipt(ticket)
  print(f'''
      Discount: {discount}
  
      TOTAL: {round(total,2)}
    ''')

def get_qrcode():
  characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
  qrcode = random.choices(characters, k=10)
  qrcode = ''.join(qrcode)
  return qrcode

###module###################################################################
def module2():
  
  init(autoreset=True)
  match_list = objects_matches(edd_matches)
  stadium_list = objects_stadiums(edd_stadiums)
  valid = False
  client_registered = False
  key = ''
  selected_match = ''
  proceed = ''
  
  while True:

    option = input(
    '''\nTICKETS SALE MANAGEMENT:
    
    1. Buy a ticket
    2. Return to Homepage
    
    -> '''
    )
    if option == '1':
      clear_screen()

      print('\nCLIENT REGISTRATION:\n')
      
      str = '!@#$%^&*()_-+.= |"'

      while not valid:
        valid = True
        id = input('ID: ')
        if len(id) < 6:
          print('\nThe ID must be at least 6 characters long.\n')
          valid = False
        else:
          for number in id:
            if number.isalpha() or number in str:
              valid = False
              print('\nInvalid input. The ID must only consist of numbers.\n')
              break
      valid = False

      
      try:
        for client in clients_db:
          if id == client.id:
            previous_client = client
            client_registered = True
            raise Exception
      
        while not valid:
          valid = True
          first_name = input('\nFirst Name: ')
          for letter in first_name:
            if letter.isnumeric() or letter in str:
              valid = False
              print('\nInvalid input. Please don\'t use numbers or special characters.\n')
              break
        valid = False

        while not valid:
          valid = True
          last_name = input('Last Name: ')
          for letter in last_name:
            if letter.isnumeric() or letter in str:
              valid = False
              print('\nInvalid input. Please don\'t use numbers or special characters.\n')
              break
        valid = False

        name = first_name.title() + ' ' + last_name.title()


        while not valid:
          valid = True
          age = input('Age: ')
          for number in age:
            if number.isalpha() or number in str:
              valid = False
              print('\nInvalid input. The age must only consist of numbers.\n')
              break
        valid = False
        clear_screen()
      except:
        print('\nYou\'re already on the system.\n')

      display_matches(match_list)

      while not valid:
        selected_match = input('Match ID: ') ##c
        for match in match_list:
          if selected_match == match.match_id:
            match_object = match
            stadium_id = match.stadium_id
            valid = True
            break
        if not valid:
          print('\nPlease choose an available match.\n') ##dont like it
      valid = False

      clear_screen()

      while key != '1' and key != '2':
        ticket_option = {'1':'General', '2':'VIP'}
        key = input('\nTicket: \n1. General (50$)\n2. VIP (120$)\n-> ')
        if key == '1' or key == '2':
          selected_ticket = ticket_option[key]
        else:
          print('\nPlease choose a valid option.\n')
        
      if selected_ticket == 'General' and match_object.general_clients == 40:
        print('\nWe\'re sorry. The general tickets are sold-out for the match you selected.\n')
        break
      elif selected_ticket == 'VIP' and match_object.VIP_clients == 20:
        print('\nWe\'re sorry. The VIP tickets are sold-out for the match you selected.\n')
        break  
      
      if not client_registered:
        client = Client(
          name,
          id,
          age 
        )
      else:
        client = Client(
          previous_client.name,
          previous_client.id,
          previous_client.age 
        )

      clear_screen()

      for stadium in stadium_list:
        if stadium_id == stadium.id:
          x, y = Stadium.get_capacity(stadium) 
          a, b = map(x, y, match_object.taken_seats)
          break
      
      while not valid:
        seat = input('\nPlease choose an available seat: ')
        try:
          seat_a = int(seat[0])
          seat_b = int(seat[1])
          if seat_a <= a and seat_b <= b:
            if seat not in match_object.taken_seats: 
              valid = True
        except: continue
      valid = False

      ticket_price = {'General':50, 'VIP':120}

      ticket = Ticket(
        client.name,
        client.id,
        client.age,
        selected_match,
        selected_ticket,
        seat,
        ticket_price[selected_ticket]
      )
      discount = get_discount(client, ticket)
      total = ticket.cost + ticket.iva - discount

      clear_screen()

      print_receipt(ticket, discount, total)

      while proceed !='1' and proceed != '2':
        proceed = input('''
      Would you like to proceed?
      1. Yes
      2. No
      -> ''')
        
      if proceed == '2':
        print('\n\nPurchase cancelled.\n\n')
        break
      else: 
        print('\n\nSuccesful Payment.\n')

        while not valid:
          qrcode = get_qrcode()
          if qrcode not in unused_qrcodes:
            valid = True
        valid = False

        print(f'''
          
                       Your QR Code is:
                  ************************* 
                          {qrcode}
                  *************************
                  
                  ''')
        ticket.qrcode = qrcode
        unused_qrcodes.append(qrcode)

        if selected_ticket == 'General':
          match_object.general_clients += 1
          tickets.append(ticket)
        elif selected_ticket == 'VIP':
          match_object.VIP_clients += 1
          match_object.total_spent += total
          if not client_registered:
            clients_VIP_db.append(client)
          tickets.append(ticket)

        if not client_registered:##########
          clients_db.append(client)
          client.sold_tickets += 1
        else:
          previous_client.sold_tickets += 1

        ticket.total = total
        match_object.taken_seats.append(seat) 
        match_object.sold_tickets +=1

        client_registered = False

    elif option == '2':
      break
                
    else:
      print('\nPlease enter a valid option.')
      

module2()