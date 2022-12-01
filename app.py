# Matches and Stadiums Management

###imports#############################################################

import os
import pickle
import random
import itertools as iter
from colorama import init, Back, Fore, Style
from EDD import objects
from Match import Match
from Team import Team
from Stadium import Stadium
from Client import Client, Ticket
from map import map
from data import clients_db, clients_VIP_db, ticket_list
from Product import Product, Food, Beverage
from Restaurant import Restaurant


#functions#############################################################

clear_screen = lambda: os.system ("cls")

def getParts(num_str):
    num_iter = iter.permutations(num_str, len(num_str))
    for num_list in num_iter:
        z = ''.join(num_list)
        x, y = z[:int(len(z)/2)], z[int(len(z)/2):]
        if x[-1] == '0' and y[-1] == '0':
            continue
        if int(x) * int(y) == int(num_str):
            return x,y
    return False
def is_vampire(m_int):
    n_str = str(m_int)
    if len(n_str) % 2 == 1:
        return False
    parts = getParts(n_str)
    if not parts:
        return False 
    return True

def numero_perfecto(numero, divisor, acum):
    while divisor > 1:
        if numero % divisor == 0:
            acum += divisor
        divisor -= 1
    if acum == numero:
        'Numero perfecto'
    else:
        return None

#functions module1#####################################################
def display_countries(team_list):
  print('\nAVAILABLE COUNTRIES:\n')
  for team in team_list:
    print(f'{team_list.index(team)}. {team.country}')

def display_stadiums(stadium_list):
  print('\nAVAILABLE STADIUMS:\n')
  for stadium in stadium_list:
    Stadium.show_stadium(stadium)

def display_dates(match_list):
  printed_list = []
  print('\nAVAILABLE DATES:\n')
  for match in match_list:
    if match.date_time[:10] not in printed_list:
      printed_list.append(match.date_time[:10])
      print(f'{printed_list.index(match.date_time[:10])}. {match.date_time[:10]}')
  return printed_list
      
  
def get_per_country(match_list, home_or_away, selected_team, available, team_list):

  for team in team_list:
    if team.country == selected_team:
        print('\nSELECTED TEAM:')
        Team.show_team(team)
        break
  print('\nAVAILABLE MATCHES:\n')  
  if home_or_away == '1': 
    for item in match_list: 
      if item.home_team == selected_team:
        Match.show_match(item)
        available = True
    if not available:
      print('\nThe country you are looking for is not available.')
    else:
      available = False

  elif home_or_away == '2':
    for item in match_list: 
      if item.away_team == selected_team:
        Match.show_match(item)
        available = True
    if not available:
      print('\nThe country you are looking for is not available.')
    else:
      available = False

def get_per_stadium(selection, match_list, available):
  for item in match_list:
    if selection == item.stadium_id:
      Match.show_match(item)
      available = True
  if not available:
    print('\nThe stadium you are looking for is not available.')
  else:
    available = False
      
      
def get_per_date_time(selection, match_list, available):
  for item in match_list:
    if item.date_time[:10] == selection[:10]:
      Match.show_match(item)
      available = True
  if not available:
    print('\nThe date & time you are looking for are not available')
  else:
    available = False
#######################################################################

#functions module2#####################################################
def display_matches(match_list):
  for match in match_list:
    Match.show_match(match)

def get_discount1(client, ticket):
  discount = 0
  if is_vampire(client.id):
    discount = ticket.cost * 0.50
  return round(discount,2)

def print_receipt1(ticket, discount, total):
  if discount != 0:
    print(f'''
                    {Back.MAGENTA} CONGRATULATIONS! YOU GOT A 50% DISCOUNT''')
  Ticket.show_receipt(ticket)
  print(f'''
      Discount: {discount}
  
      TOTAL: {round(total,2)} $
    ''')

def get_qrcode():
  characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
  qrcode = random.choices(characters, k=10)
  qrcode = ''.join(qrcode)
  return qrcode
#######################################################################

#functions module3#####################################################
None
#######################################################################

#functions module4#####################################################
def show_restaurants1(restaurant_list):
  for restaurant in restaurant_list:
    Restaurant.show_restaurant(restaurant, restaurant_list)

def get_by_name(selection, product_list, available):
  for item in product_list:
    if item.name == selection:
      available = True
      if item.type == 'food':
        Food.show_food(item)
      elif item.type == 'beverages':
        Beverage.show_beverage(item)
  if not available:
    print('\nThe product you are looking for is not available.')
  else:
    available = False

def get_by_type(selection, product_list, available):
  for item in product_list: 
    if item.type == selection:
      if item.type == 'food':
        Food.show_food(item)
      elif item.type == 'beverages':
        Beverage.show_beverage(item)
      available = True
  if not available:
    print('\nThe type you selected is not available.')
  else:
    available = False

def get_by_range(min, max, product_list, available):
  for item in product_list: 
    if min <= item.price and item.price <= max:
      if item.type == 'food':
        Food.show_food(item)
      elif item.type == 'beverages':
        Beverage.show_beverage(item)
      available = True
  if not available:
    print('\nThere are no products available in the price range you selected.')
  else:
    available = False
#######################################################################

#functions module5#####################################################
def show_restaurants2(match_list, current_match, stadium_list):
  print()
  for match in match_list:
    if match == current_match:
      break
  for stadium in stadium_list:
    if stadium.id == match.stadium_id:
      available_restaurants = stadium.restaurants
      break
  for restaurant in available_restaurants:
    print(f'{available_restaurants.index(restaurant)}. {restaurant}')
  print()
  return available_restaurants
    
def show_products(product_list, age):
  print()
  printed_list = []
  for item in product_list:
    if item.type == 'food':
      print(f'    ID: {product_list.index(item)}')
      printed_list.append(product_list.index(item))
      Food.show_food(item)
    elif item.type == 'beverages':
      if age < 18 and item.is_alcoholic == 'non-alcoholic':
        print(f'    ID: {product_list.index(item)}')
        printed_list.append(product_list.index(item))
        Beverage.show_beverage(item)
      elif age >= 18:
        print(f'    ID: {product_list.index(item)}')
        printed_list.append(product_list.index(item))
        Beverage.show_beverage(item)
  return printed_list

def get_discount2(id, total):
  discount = 0
  if numero_perfecto(id,id-1,0):
    discount = total*0.15
  return discount

def print_preliminary_receipt(shopping_cart, total):
  print()
  for product, amount in shopping_cart.items():
    print(f'{amount} - {product}')
  print(f'\nTotal: {total} $')

def print_receipt2(shopping_cart, discount, subtotal, total, id):
  print('\n************** RECEIPT **************\n')
  print(f'Client ID: {id}\n')
  for k,v in shopping_cart.items():
    print(f'{v} - {k.name}')
  print(f'\nDiscount: {discount}')
  print(f'Subotal: {subtotal}')
  print(f'\nTOTAL: {total} $')
  print('\nSUCCESSFUL PAYMENT.\n')
#######################################################################

#functions module6#####################################################
def get_attendance(match):
    attendance = match.attendance
    return attendance
def show_matches(match_list):
    print(f'''
    {Back.BLUE}     MATCHES SORTED FROM MOST TO LEAST ATTENDANCE:''')
        
    if match_list[0].attendance == 0:
        print('\nData not available.')
    else:
        for match in match_list:
        
            Match.show_match(match)\
                
            try:
                ratio = match.attendance/match.sold_tickets
            except:
                ratio = 0

            try:
                average_spent = match.total_spent/match.VIP_clients
            except:
                average_spent = 0


            print(f'''
        - Attendance: {match.attendance}
        - Sold Tickets: {match.sold_tickets}
        - Attendance/Sale Ratio: {round(ratio, 2)}
        - Average spent per VIP client: {average_spent} $
            ''')
def get_best_attendance(match_list):
    print(f'''
    {Back.BLUE}     BEST ATTENDANCE:''')
    match = match_list[0]
    if match.attendance == 0:
        print('\nData not available.')
    else:
        Match.show_match(match)
        try:
            ratio = match.attendance/match.sold_tickets
        except:
            ratio = 0
        print(f'''
        - Attendance: {match.attendance}
        - Sold Tickets: {match.sold_tickets}
        - Attendance/Sale Ratio: {round(ratio, 2)}
        ''')

def get_sold_tickets(match):
    sold_tickets = match.sold_tickets
    return sold_tickets

def get_best_sales(match_list):
    print(f'''
    {Back.BLUE}     BEST SALES:\n''')
    match = match_list[0]
    if match.sold_tickets == 0:
        print('Data not available.')
    else:
        Match.show_match(match)
        try:
            ratio = match.attendance/match.sold_tickets
        except:
            ratio = 0
            print(f'''
        - Attendance: {match.attendance}
        - Sold Tickets: {match.sold_tickets}
        - Attendance/Sale Ratio: {round(ratio, 2)}
        ''')

def get_sales_product(product):
    sales_product = product.sold
    return sales_product

def get_best_sales_products(product_list):
    print(f'''
    {Back.BLUE}     TOP 3 SOLD PRODUCTS PER RESTAURANT:\n''')
    for restaurant, products in product_list.items():
        print(f'{Back.LIGHTBLACK_EX}{restaurant}: ')
        if products[0].sold == 0:
            print('\nData not available.\n')
        else:
            for product in products[:3]:
                Product.show_product(product)

def get_sold_tickets_per_client(client):
    sold_tickets = client.sold_tickets
    return sold_tickets

def get_top_clients(clients_db):
    print(f'''
    {Back.BLUE}     TOP 3 CLIENTS:\n''')
    if clients_db == []:
        print('Data not available.\n')
    else:
        for client in clients_db[:3]: 
            Client.show_client(client)
###################################################################################


def start():
  team_list, stadium_list, product_list, match_list, restaurant_list = objects()


#def descarga de datos#############################################################
def download(clients_db, clients_VIP_db, match_list, stadium_list, ticket_list):
  while True:
    option = input('''
        Upload the previous data or reset?
        1. Upload saved data
        2. Reset
        -> ''')
    if option == '1':
      start() 
      break
    elif option == '2':
      read(clients_db, clients_VIP_db, match_list, stadium_list, ticket_list)
      break
    else:
      print('\nPlease enter a valid option.')
###################################################################################

def read(clients, clients_db_VIP, matches, stadiums, tickets):
  client_empty = False
  client_VIP_empty = False
  match_empty = False
  stadium_empty = False
  tickets_empty = False 


  if os.path.exists('clients_db.txt'):
    if os.path.getsize('clients_db.txt') != 0:
      with open('clients_db.txt','rb') as a:
        clients_db = pickle.load(a)
    else:
      client_empty = True

  else:
    with open('clients_db.txt', 'x'):
      pass
    client_empty = True

  if client_empty == True:
    print('\nNo client data')

  if os.path.exists('clients_db_VIP.txt'):
    if os.path.getsize('clients_db_VIP.txt') != 0:
      with open('clients_db_VIP.txt','rb') as a:
        clients_db_VIP = pickle.load(a)
    else:
      client_VIP_empty = True

  else:
    with open('clients_db_VIP.txt', 'x'):
      pass
    client_VIP_empty = True

  if client_empty == True:
    print('\nNo client data')
  
  if os.path.exists('match.txt'):
    if os.path.getsize('match.txt') != 0:
      with open('match.txt','rb') as a:
        matches = pickle.load(a)
    else:
      match_empty = True

  else:
    with open('match.txt', 'x'):
      pass
    match_empty = True

  if match_empty == True:
    print('\nNo match data')

  if os.path.exists('stadium.txt'):
    if os.path.getsize('stadium.txt') != 0:
      with open('stadium.txt','rb') as a:
        stadiums = pickle.load(a)
    else:
      stadium_empty = True

  else:
    with open('stadium.txt', 'x'):
      pass
    stadium_empty = True

  if stadium_empty == True:
    print('\nNo stadium data')

  if os.path.exists('tickets.txt'):
    if os.path.getsize('tickets.txt') != 0:
      with open('tickets.txt','rb') as a:
        tickets = pickle.load(a)
    else:
      tickets_empty = True



  if client_empty == True and client_VIP_empty == True and match_empty == True and tickets_empty == True and stadium_empty == True:
    print('\nThere\'s no available data. The data will be taken from the api')
    start()



  

#guardado de datos#################################################################
def save(clients_db, clients_db_VIP, matches, stadiums, products, tickets):
  with open('clients_db.txt','wb') as i:
    pickle.dump(clients_db,i)

  with open('clients_db_VIP.txt','wb') as i:
    pickle.dump(clients_db_VIP,i)

  with open('match.txt','wb') as i:
    pickle.dump(matches,i)

  with open('stadium.txt','wb') as i:
    pickle.dump(stadiums,i)

  with open('products.txt','wb') as i:
    pickle.dump(products,i)

  with open('tickets.txt','wb') as i:
    pickle.dump(tickets,i)

###################################################################################

##main#############################################################################
def app():
    #transforma la edd de la api en objetos
    team_list, stadium_list, product_list, match_list, restaurant_list = objects() 

    download(clients_db, clients_VIP_db, match_list, stadium_list, ticket_list)

    ###############################################################################

    while True: 
        init(autoreset=True)
        
        print('''

        
                    ██████╗  █████╗ ████████╗ █████╗ ██████╗     ██████╗  ██████╗ ██████╗ ██████╗ 
                   ██╔═══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗    ╚════██╗██╔═████╗╚════██╗╚════██╗
                   ██║   ██║███████║   ██║   ███████║██████╔╝     █████╔╝██║██╔██║ █████╔╝ █████╔╝
                   ██║▄▄ ██║██╔══██║   ██║   ██╔══██║██╔══██╗    ██╔═══╝ ████╔╝██║██╔═══╝ ██╔═══╝ 
                   ╚██████╔╝██║  ██║   ██║   ██║  ██║██║  ██║    ███████╗╚██████╔╝███████╗███████╗
                    ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝ ╚══════╝╚══════╝
                                                             
        
        ''')


        main_option = input('''
    --------------------------------- WELCOME TO QATAR'S 2022 MANAGEMENT SYSTEM! ------------------------------------
    
    Enter an option:

        1. Matches and Stadiums Management
        2. Tickets Sale Management
        3. Matches Attendance Management
        4. Restaurant Management
        5. Restaurant Sales Management
        6. Management Tracking
        7. Exit

    -> '''
        )
        
        if main_option == '1':###################module1#######################
          option = 0
          home_or_away = 0
          selection = ''
          available = False
          
          while option != '4':
            option = input(
            '''\nMATCHES AND STADIUM MANAGEMENT:
            
            1. Search match per country
            2. Search match per stadium
            3. Search match per date & time
            4. Return to Homepage
            
            -> '''
            )
            print('a')
            clear_screen()

            if option == '1':
              
              while True:
                home_or_away = input('\n Search by:\n\n1. Home Team\n2. Away Team\n\n-> ')
                if home_or_away == '1' or home_or_away == '2':
                  break
                else: print('\nInvalid option.') 

              clear_screen()
              display_countries(team_list)

              while True:
                try:
                  selection = int(input('\nPlease enter the country: '))
                  get_per_country(match_list, home_or_away, team_list[selection].country, available, team_list)
                  break
                except:
                  print('\nPlease enter a valid option.')
              

            elif option == '2':
              display_stadiums(stadium_list)

              while True: ##acomodar 
                try:
                  selection = int(input('Stadium ID: ')) #pasa al exception si el ID no es un integer
                  get_per_stadium(selection, match_list, available)
                  break
                except:
                  print('\nPlease enter the ID number only.') 

            elif option == '3':
              printed_list = display_dates(match_list)
              while True:
                try:
                  selection = int(input('\nDate: ')) #pasa al exception si la seleccion no es un int
                  get_per_date_time(printed_list[selection], match_list, available)
                  break
                except:
                  print('\nPlease enter a valid option.')
              
              

            elif option == '4':
              break

            else:
              print('\nPlease enter a valid option.')            
        #########################################################################

        elif main_option == '2':###################module2#######################
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
              
              string = '!@#$%^&*()_-+.= |"' #caracteres especiales

              while not valid:
                valid = True
                try:
                    id = int(input('ID: '))
                    if len(str(id)) < 6: #longitud de la id como string
                        print('\nThe ID must be at least 6 characters long.\n')
                        valid = False
                except:
                    print('\nInvalid input. The ID must only consist of numbers.\n')
                    valid = False
              valid = False

              
              try:
                for client in clients_db:
                  if id == client.id:
                    previous_client = client
                    client_registered = True
                    raise Exception #si el cliente ya esta registrado no se registra de nuevo nombre y edad
              
                while not valid:
                  valid = True
                  first_name = input('\nFirst Name: ')
                  for letter in first_name:
                    if letter.isnumeric() or letter in string:
                      valid = False
                      print('\nInvalid input. Please don\'t use numbers or special characters.\n')
                      break
                valid = False

                while not valid:
                  valid = True
                  last_name = input('Last Name: ')
                  for letter in last_name:
                    if letter.isnumeric() or letter in string:
                      valid = False
                      print('\nInvalid input. Please don\'t use numbers or special characters.\n')
                      break
                valid = False

                name = first_name.title() + ' ' + last_name.title()


                while not valid:
                  valid = True
                  try:
                    age = int(input('Age: '))
                    break
                  except:
                    valid = False
                    print('\nInvalid input. The age must only consist of numbers.\n')        
                valid = False

                clear_screen()

              except: #try de arriba
                print('\nYou\'re already on the system.\n')

              display_matches(match_list)

              while not valid:
                selected_match = input('Match ID: ') 
                for match in match_list:
                  if selected_match == match.match_id:
                    match_object = match
                    stadium_id = match.stadium_id
                    stadium_object = stadium_list[stadium_id+1]
                    valid = True
                    break
                if not valid:
                  print('\nPlease choose an available match.\n') 
              valid = False

              clear_screen()

              while key != '1' and key != '2':
                ticket_option = {'1':'General', '2':'VIP'}
                key = input('\nTicket: \n\n1. General (50$)\n2. VIP (120$)\n\n-> ')
                if key == '1' or key == '2':
                  selected_ticket = ticket_option[key]
                else:
                  print('\nPlease choose a valid option.\n')
                
              if selected_ticket == 'General' and match_object.general_clients == stadium_object.capacity[0]: #de acuerdo a la capacidad del estadio
                print('\nWe\'re sorry. The general tickets are sold-out for the match you selected.\n') ##VER SI SIRVE
                break
              elif selected_ticket == 'VIP' and match_object.VIP_clients == stadium_object.capacity[1]: #de acuerdo a la capacidad del estadio 
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
                  seat_a = int(seat[0]) #toma la coordenada x del asiento
                  seat_b = int(seat[1]) #toma la coordenada y
                  if seat_a <= a and seat_b <= b: #verifica que el asiento exista y que no este tomado
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
              discount = get_discount1(client, ticket)
              total = ticket.cost + ticket.iva - discount

              clear_screen()

              print_receipt1(ticket, discount, total)

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

                ticket_list.append(ticket) 
                print('\n\nSuccesful Payment.\n')

                qrcode = get_qrcode()
               
                print(f'''
                  
                              Your QR Code is:
                          ************************* 
                          *       {qrcode}      *
                          *************************
                          
                          ''')
                ticket.qrcode = qrcode
                

                if selected_ticket == 'General':
                  match_object.general_clients += 1
                  ticket_list.append(ticket)
                elif selected_ticket == 'VIP':
                  match_object.VIP_clients += 1
                  match_object.total_spent += total
                  if not client_registered:
                    clients_VIP_db.append(client)
                  ticket_list.append(ticket)

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
        #########################################################################

        elif main_option == '3':###################module3#######################
          valid = False
          attemps = 0
          
          while True:

            option = input(
            '''\nMATCHES ATTENDANCE MANAGEMENT:
            
            1. Enter a match
            2. Return to Homepage
            
            -> '''
            )
            if option == '1':
              qrcode = input('''
              WELCOME TO TODAY\'s MATCH

              Please enter your ticket\'s code

              -> '''
              )

              while not valid:

                  for ticket in ticket_list:
                    if ticket.qrcode == qrcode and ticket.used == False:
                      

                      ticket.used = True

                      for match in match_list:
                        if ticket.match == match.match_id:
                          break

                      match.attendance += 1
                      valid = True
                        

                      print('''
                        
                          🎉⚽️ACCESS GRANTED. ENJOY THE MATCH!⚽️🎉
                            
                            ''')

                      break
                  
                  if valid == True:
                    break
                  
                  qrcode = input('\nCode not valid. Please try again.\n-> ')
                  attemps += 1 
                  ###puede ser

                  if attemps == 5: #a los 5 intentos fallidos da la opcion del volver al menu anterior
                    return_menu = input('\nReturn to menu?\n1.Yes\n2.No\n-> ')
                    if return_menu == '1':
                      break
                    elif return_menu == '2':
                      attemps = 0
                      continue
                    else:
                      print('\nPlease enter a valid option.')
                    attemps = 0
              valid = False
            
            elif option == '2':
              break
                
            else:
              print('\nPlease enter a valid option.')
        #########################################################################

        elif main_option == '4':###################module4#######################
          
          available = False
          valid = False
            

          while True:
            option = input(
            '''
            RESTAURANTS MANAGEMENT:
              
            1. Search product by name
            2. Search by type
            3. Search by price rage
            4. Return to Homepage
              
            -> '''
            )

            if option == '4':
                break
            
            show_restaurants1(restaurant_list)
            while not valid:
              try:
                selected_restaurant = int(input('\nPlease enter the ID of the restaurant: '))
                if selected_restaurant <= len(restaurant_list)-1: #verifica que el numero de opcion este dentro de las opciones disponibles
                  valid = True
                else: 
                  print('\nThe restaurant you selected is not available')
              except:
                print('The ID must only consist of numbers.')
            valid = False

            restaurant_name = restaurant_list[selected_restaurant].name #guarda el nombre del rest. en una variable

            if option == '1':

              while not valid:
                try:
                  selection = input('\nPlease enter the name of the product: ').title()
                  valid = True
                  break
                except:
                  print('The name must not contain numbers or special characters.')
              valid = False
              get_by_name(selection, product_list[restaurant_name], available)
                
            elif option == '2':
              type = {'1':'food', '2':'beverages'}
              while not valid:
                selection = input('\nPlease enter the type of product:\n1. Food\n2. Beverage\n-> ')
                if selection == '1' or selection == '2':
                  valid = True
                else: print('\nInvalid option.\n')
              valid = False
              get_by_type(type[selection], product_list[restaurant_name], available)
                
            elif option == '3':
              print('\nPlease enter the price range: ')

              while not valid:
                try:
                  min, max = int(input('\nMin: ')), int(input('Max: '))
                  valid = True
                  get_by_range(min, max, product_list[restaurant_name], available)
                except:
                  print('\nPlease enter only numeric characters.')
              valid = False
                  
            else:
                print('\nPlease enter a valid option.')
        #########################################################################        

        elif main_option == '5':###################module5#######################                  
          
          shopping_cart = {}
          access_granted = False
          valid = False
          proceed = False
          subtotal = 0
          total_amount = 0
          
          while not access_granted: 
            
            client_match = input('\nPlease enter your current match: ')
            client_id = input('\nPlease enter your ID: ')

            for ticket in tickets:
              if str(ticket.match) == client_match and str(ticket.id) == client_id:
                print(f'''
                                {Back.GREEN}ACCESS GRANTED''')
                access_granted = True
                break

            if not access_granted:
              print('\nYou don\'t have access to this service.\n')
              return_homepage = input('''
            Return to Homepage?
            1. Yes
            2. No
            -> ''')
              if return_homepage == '1':
                break

          while True and access_granted:

            option = input(
            '''
            RESTAURANTS MANAGEMENT:
            
            1. Make a purchase
            2. Return to Homepage
            
            -> '''
            )
            
            if option == '1':

              available_restaurants = show_restaurants2(match_list, client_match, stadium_list)
              
              while not valid:
                  try:
                    selected_restaurant = int(input('-> '))
                    if selected_restaurant <= len(available_restaurants)-1:
                      valid = True
                    else:
                      print('\nPlease choose a valid option.\n')
                  except:
                    print('Please choose a valid option.')
              valid = False

              restaurant_name = available_restaurants[selected_restaurant]

              while True: ####ciclo cliente varios productos 

                printed_list = show_products(product_list[restaurant_name], ticket.age)
                
                while not valid:
                  try:
                    selected_product = int(input('\nEnter the ID of the product you\'d like to purchase: '))
                    if selected_product <= len(product_list[restaurant_name])-1 and selected_product in printed_list:
                      valid = True
                    else: raise Exception
                  except:
                    print('\nPlease choose a valid option.')
                valid = False

                while not valid:
                  try:
                    amount = int(input('\nEnter the amount you\'d like to purchase: '))
                    price = product_list[restaurant_name][selected_product].price
              
                    if amount > 0 and amount <= product_list[restaurant_name][selected_product].quantity:
                      product_list[restaurant_name][selected_product].sold += amount ##########
                      product_list[restaurant_name][selected_product].quantity -= amount #########
                      total_amount += amount
                      valid = True
                    elif product_list[restaurant_name][selected_product].quantity > 0: 
                      raise Exception
                    else:
                      print('\nThe product you selected is out of stock')
                      break
                  except:
                    print('\n The option you selected is not valid or there\'s not enough stock.')
                valid = False

                shopping_cart[product_list[restaurant_name][selected_product].name] = total_amount
                
                subtotal += (amount * price)

                while not valid: 
                  proceed = input('''
              Would you like to purchase another product?
              1. Yes
              2. No
              -> ''')
                  if proceed == '1' or proceed == '2':
                    break
                  else: print('\nPlease enter a valid option.\n')
                valid = False
                

                if proceed == '1':
                  continue
                elif proceed == '2':

                  discount = get_discount2(ticket.id, subtotal)
                  total = subtotal - discount
                  print_preliminary_receipt(shopping_cart, total)

                  while not valid: 
                    proceed = input('''
                Would you like to proceed with your purchase?
                1. Yes
                2. No
                -> ''')
                    if proceed == '1' or proceed == '2':
                      for product, amount in shopping_cart.items(): ###por si el cliente cancela
                        product.quantity += amount
                        product.sold -= amount
                      break
                    else: print('\nPlease enter a valid option.\n')
                  valid = False

                  if proceed == '1':
                    match_list[client_match].total_spent += total
                    print_receipt2(shopping_cart, discount, subtotal, total, ticket.id)
                  elif proceed == '2':

                    break
                  break

            elif option == '2':
              break

            else:
              print('\nPlease enter a valid option.')
          access_granted = False
        #########################################################################  

        elif main_option == '6':###################module6#######################

                    match_list.sort(reverse=True, key=get_attendance)
                    show_matches(match_list)
                    get_best_attendance(match_list)
                    match_list.sort(reverse=True, key=get_sold_tickets)
                    get_best_sales(match_list)

                    for restaurant, products in product_list.items():
                        products.sort(reverse=True, key=get_sales_product)

                    get_best_sales_products(product_list)
                    clients_db.sort(reverse=True, key=get_sold_tickets_per_client)

                    get_top_clients(clients_db)
        ##########################################################################
        elif main_option == '7':
            print('''
                        Thank you for using Qatar 2022: Management System
                        Have a good day!
                        ''')
            
            save(clients_db, clients_VIP_db, match_list, stadium_list, product_list, ticket_list)
            
            break
            
        else: print('\nPlease enter a valid option.')      

app()