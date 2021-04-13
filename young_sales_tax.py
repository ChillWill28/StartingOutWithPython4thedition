#Sales Tax
#Willie Young
#Chapter2_6


#Prompt user to enter the amount of a purchase

purch_price = float(input('What is the purchase price? $'))
                    
#Compute State Sales Tax

state_tax = (purch_price*.05)
#Compute County Sales Tax

county_tax = (purch_price*.025)
              
#Compute Total Sales Tax

tot_tax = (state_tax+county_tax)
#Compute Total amount of purchase

tot_price = (purch_price+tot_tax)
#Display purchase price

print('Purchase Price: $', (format(purch_price, ',.2f')))
                                  
#Display state sales tax

print('State Sales Tax: $', (format(state_tax, ',.2f')))
              
#Display county sales tax

print('County Sales Tax: $', (format(county_tax, ',.2f')))
              
#Display total sales tax

print('Total Sales Tax: $', (format(tot_tax, ',.2f')))
              
#Display total purchase price

print('Total Price: $', (format(tot_price, ',.2f')))
