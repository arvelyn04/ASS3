def getApple():
    apple_func = int(input("The price of an apple is: "))
    return apple_func

def getOrder():
    order_func = int(input("How many apples do you want to buy? "))
    return  order_func

def multiply():
    result = apple*order
    return result

def getMoney():
    money_func = int(input("Your money here: "))    
    return money_func

def subtract():
    result = money-order
    return result

def getTotal():
    total_func = input("The total amount is {multiply}")
    return total_func

def displayOutput(orderF, totalF):
    print(f"You can buy {order} apples and your change is {total}")   






#STEPS
# 1. Ask for the price of an apple and save it to variable.
apple = getApple()
# 2. Ask how many apples they want to buy and save it to variable. 
order = getOrder()
# 3. Multiply the apples with theier orders.
multiply = apple*order
# 4. Ask for their moneyand save it to variable.
money = getMoney()
# 5. Compute the total amount.
total = money-apple*order
# 6. Display You can buy {order} and your change is {total} pesos. 
displayOutput(order, total)