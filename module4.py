# Restaurants Management


#imports
from Product import Product, Food, Beverage
from Restaurant import Restaurant
from EDD import edd_stadiums, objects_products, objects_restaurants

###el restaurante debe ser acorde al cliente que lo escoja

def show_restaurants(restaurant_list):
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

def module4(): ###crear lista de objetos

  product_list = objects_products(edd_stadiums)
  restaurant_list = objects_restaurants(edd_stadiums)
  
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
    show_restaurants(restaurant_list)
    while not valid:
      try:
        selected_restaurant = int(input('\nPlease enter the ID of the restaurant: '))
        if selected_restaurant <= len(restaurant_list)-1:
          valid = True
        else: 
          print('\nThe restaurant you selected is not available')
      except:
        print('The ID must only consist of numbers.')
    valid = False

    restaurant_name = restaurant_list[selected_restaurant].name

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

    elif option == '4':
        break
          
    else:
        print('\nPlease enter a valid option.')

module4()