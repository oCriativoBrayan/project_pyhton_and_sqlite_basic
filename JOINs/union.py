import head as h
import pandas as pd

pCadastro = h.pointerCadastro
pCompras = h.pointerCompras
pPerdas = h.pointerPerdas
pVendas = h.pointerVendas


# Attach the Compras database
pVendas.execute("""
    ATTACH DATABASE 'DB/silver_Compras.db' AS Compras;
""")


union = pVendas.execute("""
                SELECT COD_PRODUTO, OPERADOR, TOTAL_PAGO
                FROM Vendas
                UNION
                SELECT COD_PROD, RESPONSAVEL_RECEBIMENTO, VALOR_TOTAL_NOTA
                FROM Compras;
               """)


df = pd.DataFrame(
    union.fetchmany(50),
    columns=[col[0] for col in union.description]
)

print(df)
