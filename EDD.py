import requests
from Team import Team
from Stadium import Stadium
from Product import Food, Beverage
from Match import Match
from Restaurant import Restaurant

url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json'
r = requests.get(url)
edd_teams = r.json()

url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json'
r = requests.get(url)
edd_stadiums = r.json()

url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json'
r = requests.get(url)
edd_matches = r.json()

def objects_teams(edd):
    team_list = []
    for item in edd:
        team = Team(
            item['name'],
            item['flag'],
            item['fifa_code'],
            item['group'],
            item['id']
        )
        team_list.append(team)
    return team_list

def objects_stadiums(edd):
    stadium_list = []
    for item in edd:
        restaurant_names = []
        for restaurant in item['restaurants']: ##no se
            for k, v in restaurant.items():
                if k == 'name':
                    restaurant_names.append(v)

        stadium = Stadium(
            item['id'],
            item['name'],
            item['capacity'],
            item['location'],
            restaurant_names
        )
        stadium_list.append(stadium)
    return stadium_list

def objects_restaurants(edd):
    restaurant_list = []
    for item in edd:
        for rest in item['restaurants']: ##no se
            restaurant = Restaurant(rest['name'])
            restaurant_list.append(restaurant)
    return restaurant_list

def objects_products(edd):
    products_dict = {}
    for item in edd:
        for restaurant in item['restaurants']: ##no se // lista ##no se // acc. dict ??
            item_list = []
            for i in restaurant['products']: ##no se // dict. este for may be unnecessary
                if i['type'] == 'food':
                    product = Food(
                        i['name'],
                        i['quantity'],
                        i['price'],
                        i['type'],
                        i['adicional']
                    )        
                elif i['type'] == 'beverages':
                    product = Beverage(
                        i['name'],
                        i['quantity'],
                        i['price'],
                        i['type'],
                        i['adicional']
                    )
                item_list.append(product)
            products_dict[restaurant['name']] = item_list
    return products_dict
    
def objects_matches(edd):
    match_list = []
    for item in edd:
        match = Match(
            item['home_team'],
            item['away_team'],
            item['date'],
            item['stadium_id'],
            item['id']
        )
        match_list.append(match)
    return match_list

def objects():

    team_list = objects_teams(edd_teams)
    stadium_list = objects_stadiums(edd_stadiums)
    product_list = objects_products(edd_stadiums)
    match_list = objects_matches(edd_matches)
    restaurant_list = objects_restaurants(edd_stadiums) 

    return team_list, stadium_list, product_list, match_list, restaurant_list


''' #itertools

import itertools

#TXT

import json

file_name = 'edd.json'

with open(file_name, 'r', encoding = 'utf-8') as f:
    my_data = f.read() 

my_data = f.read()

my = json.loads(my_data) '''