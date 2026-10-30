from head import pointer


def selectData(first,second):
        rangeDate = pointer.execute(f'SELECT * FROM salesNov WHERE cupom BETWEEN {first} and {second}')
        print(rangeDate.fetchmany(3))

def selectDataId(id):
        row = pointer.execute(f'SELECT * FROM salesNov WHERE cupom = {id}')
        print(row.fetchmany(0))



"""
jul_out = '''SELECT * FROM salesNov 
                    WHERE datebuy BETWEEN 20260701 AND 20260730
                    
                    UNION ALL

                    SELECT * FROM salesNov 
                    WHERE datebuy BETWEEN 20260801 AND 20260830
'''

pointer.execute(jul_out)

salesJulyOut = pointer.fetchall()

print(salesJulyOut)

"""