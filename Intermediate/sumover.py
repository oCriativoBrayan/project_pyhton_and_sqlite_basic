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

#SUM OVER
s_over = pVendas.execute("""
    SELECT
        COD_PRODUTO,
        TOTAL_PAGO,
        SUM(TOTAL_PAGO) OVER (
            ORDER BY TOTAL_PAGO DESC
        ) AS TOTAL_ACUMULADO
    FROM Vendas;
    """)

all = pd.DataFrame(
    s_over.fetchmany(5),
    columns=[col[0] for col in s_over.description]
)

print(all)

