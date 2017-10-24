

def divideCheck(x):
    if x % 3 == 0 and x % 5 == 0:
        print('divisble by both 3 and 5')
    elif x % 3 == 0:
        print('divisble by 3')
    elif x % 5 == 0:
        print('divisble by 5')
    else:
        print('Number not divisble by 3 or 5')

def loopNum(x):
    if ',' in x:
        print('list')
        # convert to list
        x = x.split(',')
        for el in x:
            # convert to int
            el = int(el)
            divideCheck(el)
    else:
        x = int(x)
        divideCheck(x)
        
num = input('Enter a single number or a list of numbers: ')
loopNum(num)
