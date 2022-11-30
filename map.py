import emoji
from colorama import init, Back

init(autoreset=True)
def map(x, y, taken):
  count = 0
  print('\nSTADIUM MAP:\n')
  print('   ', end='')
  for b in range(y):
    print(Back.BLUE + f'  {b}  ', end='')
  print()
  for a in range(x):
    fila = [Back.RED + f"|{emoji.emojize(':cross_mark:')}|" if f'{a}{b}' in taken else Back.GREEN + f"|{emoji.emojize(':bust_in_silhouette:')}|" for b in range(y)]
    print(Back.BLUE + f' {str(count)}  ' + ' '.join(fila))
    count += 1
    print()
  return a, b

