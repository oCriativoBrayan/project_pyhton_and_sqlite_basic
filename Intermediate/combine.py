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
    SELECT 
        operador,
        total_pago,
        status_venda,
        SUM(total_pago) OVER (PARTITION BY status_venda == 'concluida' ORDER BY total_pago DESC) AS total_operador,
        AVG(total_pago) OVER (PARTITION BY operador) AS media_operador,
        LAG(total_pago, 1) OVER (PARTITION BY operador ORDER BY total_pago DESC) as vendas_anterior,
        LEAD(total_pago, 1) OVER (PARTITION BY operador ORDER BY total_pago DESC) as vendas_seguinte,
        SUM(total_pago) OVER (ORDER BY total_pago) AS soma_acumulada
    FROM Vendas;
    """)

av = pd.DataFrame(
    analise_vendas.fetchmany(20),
    columns=[col[0] for col in analise_vendas.description]
)

print(av)

