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
                SELECT
                    COD_PRODUTO,
                    SUM(QTD_VENDIDA) AS SUM_QTD_VENDIDA,

                    CASE
                        WHEN SUM(QTD_VENDIDA) > 2000 THEN 'More than 2000'
                        WHEN SUM(QTD_VENDIDA) > 1000 THEN 'More than 1000'
                        ELSE 'Less than 1000'
                    END AS QTD_VENDIDA_CATEGORY
                From Vendas
                GROUP BY COD_PRODUTO
                ORDER BY SUM_QTD_VENDIDA DESC;
               """)


df = pd.DataFrame(
    union.fetchmany(10),
    columns=[col[0] for col in union.description]
)

print(df)
