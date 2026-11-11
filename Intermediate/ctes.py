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

    WITH Total_Sales (COD_PRODUTO, PDV_CAIXA, TOTAL_PAGO)
    AS
    (
        SELECT
            v.COD_PRODUTO,
            v.PDV_CAIXA,
            v.TOTAL_PAGO
        FROM Vendas AS v
        WHERE v.COD_PRODUTO IS NOT NULL
    ), Compras (COD_PROD, QTD_COMPRADA, VALOR_TOTAL_NOTA)
    AS
    (
        SELECT
            c.COD_PROD,
            c.QTD_COMPRADA,
            c.VALOR_TOTAL_NOTA
        FROM db_compras.Compras AS c
        WHERE c.COD_PROD IS NOT NULL
    
    )

    SELECT
        ts.COD_PRODUTO,
        ts.PDV_CAIXA,
        ts.TOTAL_PAGO,
        c.QTD_COMPRADA,
        c.VALOR_TOTAL_NOTA
    FROM Total_Sales AS ts
    LEFT JOIN Compras AS c ON ts.COD_PRODUTO = c.COD_PROD
    GROUP BY ts.COD_PRODUTO;
               """)


df = pd.DataFrame(
    union.fetchmany(10),
    columns=[col[0] for col in union.description]
)

print(df)
