#Tickets Sale Management

###imports##################################
import random
from colorama import init, Back
from EDD import edd_matches, objects_matches, edd_stadiums, objects_restaurants, objects_products
from Match import Match
from Product import Product
from Client import Client
from data import clients_db

###funciones##################################
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
        - Attendance/Sale Ratio: {ratio}
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
        - Attendance/Sale Ratio: {ratio}
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
        - Attendance/Sale Ratio: {ratio}
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
    


###module###################################################################
def module6():

    init(autoreset=True)

    match_list = objects_matches(edd_matches)
    match_list.sort(reverse=True, key=get_attendance)
    show_matches(match_list)
    get_best_attendance(match_list)
    match_list.sort(reverse=True, key=get_sold_tickets)
    get_best_sales(match_list)
    
    product_list = objects_products(edd_stadiums)

    for restaurant, products in product_list.items():
        products.sort(reverse=True, key=get_sales_product)

    get_best_sales_products(product_list)
    clients_db.sort(reverse=True, key=get_sold_tickets_per_client)

    get_top_clients(clients_db)

module6()