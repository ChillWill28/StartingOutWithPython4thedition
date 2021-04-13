#NUM_DAYS constant holds the number of 
#days that we will gater sales data for.
NUM_DAYS = 5

def main():
    #create a list to hold the sale
    #for each day
    sales = [0] * NUM_DAYS

    # create variable to hold an index
    index = 0

    print('Enter the sales for each day.')

    #Get the sales for each day.
    while index < NUM_DAYS:
        print('Day #', index + 1, ': ', sep='', end='')
        sales [index] = float(input())
        index += 1

    #Display the values entered.
    print('Here are the values you entered:')
    for value in sales:
        print(value)

#Call the main function
main()