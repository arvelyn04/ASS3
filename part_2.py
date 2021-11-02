def getApple():
    apple_func = int(input("The price of the apple is: "))
    return apple_func

def getOrange():
    orange_func = int(input("The price of the orange is: "))   
    return orange_func

def add():
    result = apple+orange
    return result

def getTotal():
    total_func = input("The total amount is" ,add) 
    return total_func

def displayOutput(appleF, orangeF):
    print(f"The total amount is" ,add)    

#STEPS
# 1. Ask for the price of apple and save to variable
apple = getApple()
# 2. Ask for the price of orange and save to variable
orange = getOrange()
# 3. Add the apple and orange
add = apple+orange
# 4. Display apple+orange
displayOutput(apple, orange)