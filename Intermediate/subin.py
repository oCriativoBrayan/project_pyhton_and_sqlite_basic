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
                    ID_TRANSACAO, TOTAL_PAGO
                From Vendas
                WHERE ID_TRANSACAO IN(
                    SELECT DISTINCT ID_TRANSACAO
                    FROM Vendas
                );
               """)


df = pd.DataFrame(
    union.fetchmany(10),
    columns=[col[0] for col in union.description]
)

print(df)
