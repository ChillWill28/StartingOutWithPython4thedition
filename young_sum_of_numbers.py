#Sum of Numbers
#Willie Young
#Chapter4_8


#establish accumulator
total = 0

#Prompt user for number

user_num = float(input('Please enter the first number: '))

#create loop conditionally based on the number user provides is a positive number
#any negative number should stop loop
#create formula to add up all numbers entered
while user_num > -1:
    total = total + user_num  #formula to calculate 
    user_num = float(input('Please enter the next number: ')) #prompt user to enter another positive number

#print sum of all numbers
print( 'The sum of all numbers is: ', format(total, ',.1f'))
