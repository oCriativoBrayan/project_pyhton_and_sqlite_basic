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

#front
lead = pVendas.execute("""
    SELECT
        DATA_HORA_VENDA,
        TOTAL_PAGO,
        LEAD(TOTAL_PAGO) OVER (
            ORDER BY COD_PRODUTO
        ) AS TOTAL_PAGO_PROXIMO
    FROM Vendas;
    """)

lead = pd.DataFrame(
    lead.fetchmany(15),
    columns=[col[0] for col in lead.description]
)
print(lead)


print('---------------------------------------------------')

#behind
leg = pVendas.execute("""
    SELECT
        DATA_HORA_VENDA,
        TOTAL_PAGO,
        LAG(TOTAL_PAGO) OVER (
            ORDER BY COD_PRODUTO
        ) AS TOTAL_PAGO_ANTERIOR
    FROM Vendas;
    """)

leg = pd.DataFrame(
    leg.fetchmany(15),
    columns=[col[0] for col in leg.description]
)

print(leg)

print('---------------------------------------------------')

#behind
lag = pVendas.execute("""
    SELECT
        DATA_HORA_VENDA,
        TOTAL_PAGO,
        LAG(TOTAL_PAGO) OVER (
            ORDER BY COD_PRODUTO
        ) AS TOTAL_PAGO_ANTERIOR,

        TOTAL_PAGO - LAG(TOTAL_PAGO) OVER (
            ORDER BY COD_PRODUTO
        ) AS DIFERENCA_TOTAL_PAGO

    FROM Vendas;
    """)

lag = pd.DataFrame(
    lag.fetchmany(5),
    columns=[col[0] for col in lag.description]
)

print(lag)