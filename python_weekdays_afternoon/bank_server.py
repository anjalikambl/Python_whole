balance_amount=100000  #global variable

def credit(amount):
    global balance_amount
    balance_amount+=amount
    return balance_amount


