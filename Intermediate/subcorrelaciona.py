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

#create an index on the PDV_CAIXA
pVendas.execute("""
    CREATE INDEX IF NOT EXISTS idx_vendas_pdv_caixa 
    ON Vendas(PDV_CAIXA);
""")

union = pVendas.execute("""
                EXPLAIN
                SELECT v1.OPERADOR, V1.TOTAL_PAGO, V1.PDV_CAIXA
                FROM Vendas v1
                WHERE v1.TOTAL_PAGO > (
                    SELECT AVG(v2.TOTAL_PAGO)
                    FROM Vendas v2
                    WHERE v2.PDV_CAIXA = v1.PDV_CAIXA
                )
                ORDER BY v1.PDV_CAIXA, v1.TOTAL_PAGO DESC;
               """)


df = pd.DataFrame(
    union.fetchmany(10),
    columns=[col[0] for col in union.description]
)

print(df)
