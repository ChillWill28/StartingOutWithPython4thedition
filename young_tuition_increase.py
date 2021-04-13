#Tuition Increase
#Willie Young
#Chapter4_Homework


#set constants: tuition, percentage
TUITION = 8000
PCT = .03

#Projected Tuition for 5 years
for year in range(1,6):
        yr_inc = TUITION + (TUITION * PCT)
        print('Year: ', format(year))
        print('Projected annual tuition increase per semester: $', format(yr_inc, ',.2f'))
        TUITION += TUITION * PCT
