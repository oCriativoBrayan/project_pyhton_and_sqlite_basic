from insert import insertData
from delete import deleteData
import select

choosefuncition = input('write name of function: ')

if choosefuncition == 'create':
        # Create variable data test
        insert = [102,'Camiseta lacoste','XL','99.97',1,20260901,20260929]

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

