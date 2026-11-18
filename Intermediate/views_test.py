import head as h
import pandas as pd

pCadastro = h.pointerCadastro
pCompras = h.pointerCompras
pPerdas = h.pointerPerdas
pVendas = h.pointerVendas


# Attach the Compras database
attached = [
    row[1]
    for row in pVendas.execute("PRAGMA database_list")
]

if 'db_compras' not in attached:
    pVendas.execute("""
        ATTACH DATABASE 'DB/silver_Compras.db' AS db_compras;
    """)

#create an index on the PDV_CAIXA
pVendas.execute("""
    CREATE INDEX IF NOT EXISTS idx_vendas_status_operador
    ON Vendas(STATUS_VENDA, OPERADOR);
""")




pVendas.execute("""
    DROP VIEW IF EXISTS v_venda;
""")

#VIEWS CONCLUIDAS
pVendas.execute("""
    CREATE VIEW views_vendas AS
    SELECT
        OPERADOR,
        SUM(TOTAL_PAGO) AS FATURAMENTO,
        COUNT(*) AS QTD_VENDIDA,
        SUM(QTD_VENDIDA) AS QTD_TOTAL_VENDIDA,
        avg(TOTAL_PAGO) AS MEDIA_FATURAMENTO

    FROM Vendas

    WHERE STATUS_VENDA = 'CONCLUIDA'

    GROUP BY OPERADOR;
""")


#called the view concluidas
views_vendas_concluidas = pVendas.execute("""
    SELECT * FROM views_vendas;
""")


print('--------------CONCLUIDAS-------------------')

views_concluidas = pd.DataFrame(
    views_vendas_concluidas.fetchmany(5),
    columns=[col[0] for col in views_vendas_concluidas.description]
)

print(views_concluidas)


