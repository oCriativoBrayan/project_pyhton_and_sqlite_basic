
# import de head with the module name
import head as module_head

# initialize the pointer 
pointer = module_head.pointer 

"""
# create variable with many sales data
many_sales = [
    (11,'Camiseta Nike','LL','35.99',3,20260515,20260929),
    (22,'Camiseta Adidas','L','55.99',1,20260806,20260928),
    (23,'Camiseta Umbro','S','31.79',5,20260510,20260927),
    (24,'tenis nike','40','128.98',2,20260815,20260929),
    (25,'Bota Cartepila','40','235.99',1,20260419,20260928),
    (26,'Cueca Boxer','S','18.97',10,20260730,20260930),
]

# Create CTEs and insert data into the table
with module_head.conection:
    pointer.executemany("INSERT INTO salesNov VALUES(?,?,?,?,?,?,?)", many_sales)
    print("data insert with success")

"""

# create function insertData

def insertData(id,name,size,price,dateBuy,quant,dateSell):

        # Create CTEs and insert data into the table
        with module_head.conection:
            pointer.executemany("INSERT INTO salesNov VALUES(?,?,?,?,?,?,?)", [(id,name,size,price,dateBuy,quant, dateSell)])
            print("data insert with function insertData with success")
    

