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

    WITH 
    Sales AS
    (
        SELECT *
        FROM Vendas
        WHERE COD_PRODUTO IS NOT NULL
    ), 
    
    All_Sales_Up_100 AS
    (
        SELECT
            s.COD_PRODUTO,
            s.PDV_CAIXA,
            s.TOTAL_PAGO
        FROM Sales AS s
        WHERE s.TOTAL_PAGO > 100
    
    ),

    All_Sales_Down_165 AS
    (
        SELECT
            s.COD_PRODUTO,
            s.PDV_CAIXA,
            s.TOTAL_PAGO
        FROM All_Sales_Up_100 AS s
        WHERE s.TOTAL_PAGO < 165
        
    )

    SELECT
        s.COD_PRODUTO,
        s.PDV_CAIXA,
        s.TOTAL_PAGO
    FROM All_Sales_Down_165 AS s
    GROUP BY s.COD_PRODUTO;
    
    """)


df = pd.DataFrame(
    union.fetchmany(10),
    columns=[col[0] for col in union.description]
)

print(df)
