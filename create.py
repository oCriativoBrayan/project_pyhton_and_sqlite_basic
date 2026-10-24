#import de module head
import head as module_head

pointer = module_head.pointer

# create a new table
create_new_table = pointer.execute(
                        """
                        CREATE TABLE IF NOT EXISTS salesNov(
                            cupom INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            size TEXT NOT NULL,
                            price REAL NOT NULL,
                            quantity INTEGER NOT NULL,
                            dateBuy INTEGER NOT NULL,
                            dateSell INTEGER NOT NULL
                        )
                        """
                    )


print('command execute with success', create_new_table)