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
analise_vendas = pVendas.execute("""
    WITH sum_per_operator AS (
        SELECT 
            COD_PRODUTO,
            TOTAL_PAGO,
            QTD_VENDIDA,
            OPERADOR,
            SUM(TOTAL_PAGO) OVER (PARTITION BY OPERADOR ORDER BY COD_PRODUTO DESC) AS TOTAL_ACUMULADO
        FROM Vendas
    ),

    sum_per_produto AS (
        SELECT 
            COD_PRODUTO,
            QTD_VENDIDA,
            TOTAL_ACUMULADO,
            SUM(QTD_VENDIDA) OVER (PARTITION BY COD_PRODUTO ORDER BY COD_PRODUTO) AS TOTAL_ACUMULADO_QT
        FROM sum_per_operator
        GROUP BY COD_PRODUTO
    )

    
    SELECT
        COD_PRODUTO,
        TOTAL_ACUMULADO,
        TOTAL_ACUMULADO_QT,

        RANK() OVER (
            ORDER BY TOTAL_ACUMULADO DESC
        ) AS RK
        
    FROM sum_per_produto;
        
    """)

av = pd.DataFrame(
    analise_vendas.fetchmany(5),
    columns=[col[0] for col in analise_vendas.description]
)

print(av)

