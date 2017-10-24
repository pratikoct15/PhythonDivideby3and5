
def function(x):
    if x % 3 == 0 and x % 5 == 0:
        print("divisible by both")
    elif x % 3 == 0:
        print("fish")
    elif x % 5 == 0:
        print("buzz")
    else:
        print("Number not divisble by 3 or 5")
    
function(int(input("Enter the number")))