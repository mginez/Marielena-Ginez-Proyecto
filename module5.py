# Restaurant Sales Management


#imports
from data import tickets
from EDD import edd_matches, objects_matches, edd_stadiums, objects_stadiums, objects_products
from Product import Food, Beverage
from functions import numero_perfecto
from colorama import Back, init
##def client

def show_restaurants(match_list, current_match, stadium_list):
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

def get_discount(id, total):
  discount = 0
  if numero_perfecto(id,id-1,0):
    discount = total*0.15
  return discount

def print_preliminary_receipt(shopping_cart, total):
  print()
  for product, amount in shopping_cart.items():
    print(f'{amount} - {product}')
  print(f'\nTotal: {total} $')

def print_receipt(shopping_cart, discount, subtotal, total, id):
  print('\n************** RECEIPT **************\n')
  print(f'Client ID: {id}\n')
  for k,v in shopping_cart.items():
    print(f'{v} - {k.name}')
  print(f'\nDiscount: {discount}')
  print(f'Subotal: {subtotal}')
  print(f'\nTOTAL: {total} $')
  print('\nSUCCESSFUL PAYMENT.\n')


def module5():
  
  init(autoreset=True)
  shopping_cart = {}
  match_list = objects_matches(edd_matches)
  stadium_list = objects_stadiums(edd_stadiums)
  product_list = objects_products(edd_stadiums)
  access_granted = False
  valid = False
  proceed = False
  subtotal = 0
  total_amount = 0
  
  while not access_granted: ###indentar
    
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

      available_restaurants = show_restaurants(match_list, client_match, stadium_list)
      
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

        while not valid: ####ARREGLAR ESTA MIERDA
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

          discount = get_discount(ticket.id, subtotal)
          total = subtotal - discount
          print_preliminary_receipt(shopping_cart, total)

          while not valid: ####ARREGLAR ESTA MIERDA
            proceed = input('''
        Would you like to proceed with your purchase?
        1. Yes
        2. No
        -> ''')
            if proceed == '1' or proceed == '2':
              for product, amount in shopping_cart.items(): ###por si cancela
                product.quantity += amount
                product.sold -= amount
              break
            else: print('\nPlease enter a valid option.\n')
          valid = False

          if proceed == '1':
            match_list[client_match].total_spent += total
            print_receipt(shopping_cart, discount, subtotal, total, ticket.id)
          elif proceed == '2':

            break
          break

    elif option == '2':
      break

    else:
      print('\nPlease enter a valid option.')
  access_granted = False

module5()