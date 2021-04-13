#Ask employee how many hours worked
hrs_wrked = float(input('How many hours did you work? '))

#Ask employee rate of pay
hrly_pay = float(input('What is you pay rate? '))

#define pay period
print('Pay Period of 1/5-1/19:')

#display hours worked
print('Hours Worked: ', hrs_wrked)

#display hourly pay
print('Hourly Pay: ', hrly_pay)

#display gross pay
print('Gross Pay:', (hrs_wrked*hrly_pay))

                  
