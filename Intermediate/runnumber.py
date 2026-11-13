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
        ROW_NUMBER() OVER(
            ORDER BY COD_PRODUTO DESC
        ) AS RN,
        PDV_CAIXA,
        TOTAL_PAGO

        FROM Vendas;
    
    """)
df = pd.DataFrame(
    union.fetchmany(5),
    columns=[col[0] for col in union.description]
)
print(df)

print('---------------------------------------------------')



union2 = pVendas.execute("""

        SELECT
        ROW_NUMBER() OVER(
            ORDER BY VALOR_TOTAL_NOTA DESC
        ) AS RN,
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


union3 = pVendas.execute("""

        SELECT
        ROW_NUMBER() OVER(
            PARTITION BY PDV_CAIXA
            ORDER BY TOTAL_PAGO DESC
        ) AS RN,
        COD_PRODUTO,
        PDV_CAIXA,
        TOTAL_PAGO

        FROM Vendas;
    
    """)

df3 = pd.DataFrame(
    union3.fetchmany(15),
    columns=[col[0] for col in union3.description]
)
print(df3)