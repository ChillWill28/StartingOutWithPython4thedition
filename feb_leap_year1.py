#February Leap Year
#Willie Young
#Chapter3_16

#prompt user to enter year
year = int(input('Enter a year: '))

message = ''
# if and else statement


if year > 0:

      

    #statement 1: can number be divided by 100
     #statement 2: if yes, can it also be divided by 400
        #if yes, print stmt 1
    if year % 100 == 0 and year % 400 == 0:

        print('In', year,',', 'February has 29 days.')

       
#can number be divided by 4
        #if yes, day = 29
       
    else:
        if year % 4 == 0:
            
            print('In', year,',', 'February has 29 days.')
        else:
            
            print('In', year,',', 'February has 28 days.')
    
#error message if  year <= 0

else:
    message = "Year must be greater than 0."

print(message)
    

    
            
