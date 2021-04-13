#Land Calculation

#Prompt user for land in square fee
sq_ft = float(input('What is the total square feet of land? '))
#calculate acre
acre = sq_ft/43560
#display total
print('Total acres of land: ',format(acre, ',.2f'))

