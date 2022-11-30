# Matches and Stadiums Management

###imports

from EDD import objects
from Match import Match
from Team import Team
from Stadium import Stadium
import os

clear_screen = lambda: os.system ("cls")

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
      
  
def get_per_country(match_list, home_or_away, selected_team, available):
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
      

def module1():

  team_list, stadium_list, products_list, match_list, restaurant_list = objects()
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
          get_per_country(match_list, home_or_away, team_list[selection].country, available)
          break
        except:
          print('\nPlease enter a valid option.')
      

    elif option == '2':
      display_stadiums(stadium_list)

      while True: ##acomodar 
        try:
          selection = int(input('Stadium ID: ')) ##c
          get_per_stadium(selection, match_list, available)
          break
        except:
          print('\nPlease enter the ID number only.') ##acomodar esta validacion

    elif option == '3':
      display_dates(match_list)
      while True:
        try:
          selection = int(input('\nDate & time: '))
          get_per_date_time(match_list[selection].date_time, match_list, available)
          break
        except:
          print('\nPlease enter a valid option.')
      
      

    elif option == '4':
      break

    else:
      print('\nPlease enter a valid option.')
      

module1()