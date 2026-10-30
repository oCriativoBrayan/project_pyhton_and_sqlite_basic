# import de head with the module name
import head as module_head

# initialize the pointer 
pointer = module_head.pointer 

# create function insertData

def updateData(id,name,size,price,dateBuy,quantity,dateSell):

        idVerify = pointer.execute("SELECT * from salesNov WHERE cupom = ?", (id,)).fetchone()

        if idVerify is None:
              print(f"Not identify id = {id}, confim the id number!")
              return

        else:
            # Create CTEs and insert data into the table
            with module_head.conection:
                pointer.execute("""
                UPDATE salesNov
                SET name = ?,
                    size = ?,
                    price = ?,
                    dateBuy = ?,
                    quantity = ?,
                    dateSell = ?
                WHERE cupom = ?

                """, (name, size, price, dateBuy, quantity, dateSell, id))
                print(f"ID {id} updated sucessfully!")
        

