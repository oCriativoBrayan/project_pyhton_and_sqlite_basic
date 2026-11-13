import head as h
import pandas as pd

pCadastro = h.pointerCadastro
pCompras = h.pointerCompras
pPerdas = h.pointerPerdas
pVendas = h.pointerVendas


# Attach the Compras database
pVendas.execute("""
    ATTACH DATABASE 'DB/silver_Compras.db' AS db_compras;
""")

#create an index on the PDV_CAIXA
pVendas.execute("""
    CREATE INDEX IF NOT EXISTS idx_vendas_pdv_caixa 
    ON Vendas(COD_PRODUTO, PDV_CAIXA);
""")

union = pVendas.execute("""

        SELECT
        RANK() OVER(
            PARTITION BY PDV_CAIXA
            ORDER BY TOTAL_PAGO DESC
        ) AS RK,
        PDV_CAIXA,
        TOTAL_PAGO

        FROM Vendas;
    
    """)
df = pd.DataFrame(
    union.fetchmany(15),
    columns=[col[0] for col in union.description]
)
print(df)

print('---------------------------------------------------')


dense = pVendas.execute("""

        SELECT
        DENSE_RANK() OVER(
            PARTITION BY PDV_CAIXA
            ORDER BY TOTAL_PAGO DESC
        ) AS RK,
        PDV_CAIXA,
        TOTAL_PAGO

        FROM Vendas;
    
    """)
dense = pd.DataFrame(
    dense.fetchmany(15),
    columns=[col[0] for col in dense.description]
)
print(dense)

print('---------------------------------------------------')



union2 = pVendas.execute("""

        SELECT
        RANK() OVER(
            ORDER BY VALOR_TOTAL_NOTA DESC
        ) AS RK,
        COD_PROD,
        RESPONSAVEL_RECEBIMENTO,
        VALOR_TOTAL_NOTA

        FROM db_compras.Compras;
    
    """)

df2 = pd.DataFrame(
    union2.fetchmany(5),
    columns=[col[0] for col in union2.description]
)
print(df2)


print('---------------------------------------------------')


row = pVendas.execute("""

        SELECT
        ROW_NUMBER() OVER(
            PARTITION BY PDV_CAIXA
            ORDER BY TOTAL_PAGO DESC
        ) AS RK,
        PDV_CAIXA,
        TOTAL_PAGO

        FROM Vendas;
    
    """)

rownumber = pd.DataFrame(
    row.fetchmany(15),
    columns=[col[0] for col in row.description]
)
print(rownumber)