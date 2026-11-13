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

        SELECT COD_PRODUTO, PDV_CAIXA, OPERADOR, TOTAL_PAGO
        FROM Vendas as v
        WHERE EXISTS (
            SELECT *
            FROM db_compras.Compras as c2
            WHERE c2.COD_PROD = v.COD_PRODUTO
        );
    
    """)

union2 = pVendas.execute("""

        SELECT COD_PRODUTO, PDV_CAIXA, TOTAL_PAGO
        FROM Vendas as v
        WHERE NOT EXISTS (
            SELECT *
            FROM db_compras.Compras as c2
            WHERE c2.COD_PROD = v.COD_PRODUTO
        );
    
    """)


df = pd.DataFrame(
    union.fetchmany(5),
    columns=[col[0] for col in union.description]
)
print(df)

print("---------------------------------------------------")

df2 = pd.DataFrame(
    union2.fetchmany(5),
    columns=[col[0] for col in union2.description]
)

print(df2)
