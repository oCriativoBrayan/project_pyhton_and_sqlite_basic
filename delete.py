from head import pointer, conection


def deleteData(id):
    if not id:
        print('id is required to delete data')
        return
    if not isinstance(id, int):
        print('id must be an integer')
        return
    
    # Create CTEs and delete data from the table
    with conection:
        pointer.execute("DELETE FROM salesNov WHERE cupom=?", (id,))
        print("data delete with function deleteData with success")