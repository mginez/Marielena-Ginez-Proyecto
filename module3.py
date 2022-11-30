#Matches Attendance Management

###imports##################################
from data import unused_qrcodes, used_qrcodes, clients_db, matches_attendance, tickets
from EDD import edd_matches, objects_matches
###funciones##################################
###module###################################################################
def module3():
  
  
  valid = False
  attemps = 0
  
  while True:

    matches_list = objects_matches(edd_matches)

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

          for qr in unused_qrcodes:
            if qrcode == qr:
              valid = True
              break

          if valid:
            for ticket in tickets:
              if ticket.qrcode == qrcode:
                break

            used_qrcodes.append(qrcode) ###hacer este pocoton de listas equisde
            unused_qrcodes.remove(qrcode)

            for match in matches_list:
              if ticket.match == match.match_id:
                break

            match.attendance += 1
            valid = True
              

            print('''
              
                🎉⚽️ACCESS GRANTED. ENJOY THE MATCH!⚽️🎉
                  
                  ''')
            break

          
          qrcode = input('\nCode not valid. Please try again.\n-> ')
          attemps += 1
          ###puede ser

          if attemps == 5:
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
      

module3()