import head as h
import pandas as pd

pCadastro = h.pointerCadastro
pCompras = h.pointerCompras
pPerdas = h.pointerPerdas
pVendas = h.pointerVendas


# Attach the Cadastro database
pVendas.execute("""
    ATTACH DATABASE 'DB/silver_Cadastro.db' AS db_cadastro;
""")

id103 = pCadastro.execute('SELECT * FROM Cadastro WHERE COD_PROD = 103')
print(id103.fetchmany(2))


# PRINT COLUMM CAD
#colunas = pCadastro.execute("PRAGMA table_info(Cadastro)")

#for coluna in colunas.fetchall():
#    print(coluna)


#colunas = pVendas.execute("PRAGMA table_info(Vendas)")

#for coluna in colunas.fetchall():
#    print(coluna)

union = pVendas.execute("""
                SELECT v.COD_PRODUTO, c.CATEGORIA_BRUTA, c.NOME_PRODUTO, v.QTD_VENDIDA, v.TOTAL_PAGO
                FROM Vendas as v
                CROSS JOIN db_cadastro.Cadastro as c
                    ON c.COD_PROD = v.COD_PRODUTO
               """)


df = pd.DataFrame(
    union.fetchmany(5),
    columns=[col[0] for col in union.description]
)

print(df)


resultado = union.fetchall()

print(len(resultado))
