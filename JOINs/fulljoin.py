import head as h
import pandas as pd

pCadastro = h.pointerCadastro
pVendas = h.pointerVendas

#set database cadastro the vendas database
pVendas.execute("ATTACH DATABASE 'DB/silver_Cadastro.db' AS db_cadastro;")

union = pVendas.execute("""
            SELECT v.COD_PRODUTO, c.CATEGORIA_BRUTA, c.NOME_PRODUTO, v.QTD_VENDIDA, v.TOTAL_PAGO
            FROM Vendas as v
            FULL JOIN db_cadastro.Cadastro as c
            ON c.COD_PROD = v.COD_PRODUTO
        """)


# create dataframe show data
df = pd.DataFrame(
    union.fetchmany(5),
    columns=[col[0] for col in union.description]
)

print(df)


resultado = union.fetchall()

print(len(resultado))