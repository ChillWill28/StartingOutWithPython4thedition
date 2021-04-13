
#base pay constant
BASE_PAY = 900


def main():
    #prompt user for total sales
    info()
    userSales = sales()
    userSalary = salary(sales)
    userPay = pay(sales , salary)
    userDeduct = (pay)
    userNet = net(gross, deduct)
    userBudget = budget(net)
    printInfo(userSales, userSalary, userPay, userDeduct, userNet, userBudget)


def sales():
    sales = int(input('Please enter your total amount of sales: $'))
    return sales
#prompt user for first and last name and gender
def info():
    fname = input('Please enter your first name: ')
    lname = input('Please enter your last name: ')
    gender = input('Please enter whether male or female: ')
    
    if gender != 'male':
        print('Ms.', fname, lname)
    else:
        print('Mr.', fname, lname)

def salary(sales):
    comm = sales * .06
    return comm

def pay(salary , sales):
    BASE_PAY = 900
    gross = comm + BASE_PAY
    return gross

def deduct(pay):
    deduct = gross * .18
    return deduct

def net(pay, deduct):
    net = gross - deduct
    return net

def budget(net): 
    housing = net * .45
    food_clothes = net * .2
    entertainment = net * .25
    misc = net * .1
    return housing
    return food_clothes
    return entertainment
    return misc

def printInfo(userSales, userGross, userPay, userDeduct, userNet, userBudget):


    print('Sales: $', format(userSales, ',.2f'))    
    print('Commission: $', format(userSalary, ',.2f'))
    print('Gross Pay: $', format(userGross, ',.2f'))
    print('Deductions: $', format(userDeduct, ',.2f'))
    print('Net Pay: $', format(userNet, ',.2f'))
    print('Housing & Utilities: $', format(housing, ',.2f'))
    print('Food & Clothing: $', format(food_clothes, ',.2f'))
    print('Entertainment: $', format(entertainment, ',.2f'))
    print('Miscellaneous: $', format(misc, ',.2f'))

main()
    


