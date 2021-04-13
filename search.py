prod_nums = ['V475', 'F987', 'Q143', 'R688']


#get product number to search for
search = input('Enter a product number: ')

#determine whether the product number is in the list
if search in prod_nums:
    print(search, 'was found in the list.')
else:
    print(search, ' was not found in the list.')