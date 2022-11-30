import itertools as iter
  

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
        
