#Tip Tax Total
#Willie Young
#Chapter2_8

#prompt user to enter menu price for meal

menu_price = float(input('What is the menu price for the meal? '))

#calculate 7% sales tax

sales_tax = menu_price * .07

#calculate 18% tip

tip_amt = (menu_price + sales_tax) * .18

#calulate total price

tot_amt = menu_price + sales_tax + tip_amt

#display menu price, sales tax, tip amount, & total

print('Menu Price: $', format(menu_price, ',.2f'))
print('Sales Tax: $', format(sales_tax, ',.2f'))
print('Tip Amount: $', format(tip_amt, ',.2f'))
print('Total Amount: $', format(tot_amt, ',.2f'))
