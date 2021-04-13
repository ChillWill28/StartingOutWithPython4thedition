#Get desired future value
desired_val = float(input('What is the desired future value of your current account? $'))

#Get annual interest rate
int_rate = float(input('What is the interest rate on your current account? '))
#Get number of years of appreciation
years = int(input('How many years do you plan to save? '))
#Calcuate necessary deposit amount
current_val = desired_val/ (1.0 +int_rate)**years
                  
#Display Necessary deposit amount
print("Here's the information you requested: ")
print('Desired future balance: ', desired_val)
print('Annual interest rate: ', int_rate)
print('Years of appreciation: ', years)
print('Amount needed to achieve goal: $', format(current_val, ",.2f"))
