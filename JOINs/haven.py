import head as h
import pandas as pd

pCadastro = h.pointerCadastro
pCompras = h.pointerCompras
pPerdas = h.pointerPerdas
pVendas = h.pointerVendas


# Attach the Cadastro database
pVendas.execute("""
    ATTACH DATABASE 'DB/silver_Cadastro.db' AS db_cadastro;
""")


union = pVendas.execute("""
                SELECT OPERADOR, TOTAL_PAGO, STATUS_VENDA, SUM(QTD_VENDIDA) AS SUM_QTD_VENDIDA
                FROM Vendas
                GROUP BY OPERADOR
                HAVING SUM_QTD_VENDIDA > 1000
                ORDER BY SUM_QTD_VENDIDA DESC;
               """)


df = pd.DataFrame(
    union.fetchmany(5),
    columns=[col[0] for col in union.description]
)

print(df)
