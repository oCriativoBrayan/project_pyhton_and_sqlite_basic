from insert import insertData
from delete import deleteData
from update import updateData
import select

choosefuncition = input('write name of function: ')

if choosefuncition == 'create':
        # Create variable data test
        insert = []

        #create camps with the data in the list insert
        id = int(input('Write the number id: '))
        name = input('Write the name item: ')
        size = input('Write the size: ')
        price = float(input('Write the price: '))
        quant = int(input('Write the quant: '))
        dateBuy = input('Write the datebuy: ')
        dateSell = input('Write the datesell: ')

        # call the function insertData with the data in the list insert
        insertData(id, name, size, price, quant, dateBuy, dateSell)

elif choosefuncition == 'update':
        # Create variable data test
        up = []

        #create camps with the data in the list insert
        id = int(input('Write the number id: '))
        name = input('Write the name item: ')
        size = input('Write the size: ')
        price = float(input('Write the price: '))
        quantity = int(input('Write the quant: '))
        dateBuy = input('Write the datebuy: ')
        dateSell = input('Write the datesell: ')

        # call the function insertData with the data in the list insert
        updateData(id, name, size, price, quantity, dateBuy, dateSell)



elif choosefuncition == 'selectRange':
    first = int(input('Write the first number: '))
    second = int(input('Write the second number: '))

    select.selectData(first, second)

elif choosefuncition == 'selectId':
    id = int(input('Write the ID: '))

    select.selectDataId(id)


elif choosefuncition == 'delete':
    id = input('Enter the id to delete:')
    id = int(id)

    deleteData(id)
else:
    print("not look the function")

