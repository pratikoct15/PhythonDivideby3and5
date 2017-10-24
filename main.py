

def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        print('fizzbuzz')
    elif x % 3 == 0:
        print('fizz')
    elif x % 5 == 0:
        print('buzz')
    else:
        print('Not divisble by 3 or 5')

def loop_it(x):
    # check if list or int
    # we check if a comma is in x to see if its a list
    if ',' in x:
        print('list')
        # turn to list
        x = x.split(',')
        for el in x:
            # turn to int
            el = int(el)
            fizzbuzz(el)
    else:
        x = int(x)
        fizzbuzz(x)
        
num = input('Enter a single number or a list of numbers: ')
loop_it(num)
