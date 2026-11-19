import head as h
import pandas as pd

print("ARQUIVO EXECUTADO:", __file__)

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

#create an index on the STATUS_VENDA
pVendas.execute("""
    CREATE INDEX IF NOT EXISTS idx_vendas_status_operador
    ON Vendas(STATUS_VENDA, OPERADOR)
    WHERE STATUS_VENDA = 'ESTORNADA';
""")

#Create and index on te ID_TRANSACAO
pVendas.execute("""
    CREATE UNIQUE INDEX idx_vendas_cod_prod
    ON Vendas(ID_TRANSACAO)
    WHERE STATUS_VENDA = 'CONCLUIDA';
""")

print('------------------ INDEX ID_TRANSACAO --------------')


print('-- IDX PRAGMA --')
print(pVendas.execute("""
    PRAGMA index_info('idx_vendas_status_operador');
""").fetchall())

print('-- IDX ID_TRANSACAO = 9****5 --')
print(pVendas.execute("""
    EXPLAIN QUERY PLAN
    SELECT *
    FROM Vendas
    WHERE ID_TRANSACAO = 900005;
""").fetchall())




print('------------------DROP--------------')
pVendas.execute("""
    DROP VIEW IF EXISTS vendas_estornada;
""")

pVendas.execute("""
    DROP VIEW IF EXISTS vendas_em_aberto;
""")

pVendas.execute("""
    DROP VIEW IF EXISTS v_venda;
""")

pVendas.execute("""
    DROP VIEW IF EXISTS v_vendas;
""")


existing_views = pVendas.execute("""
    SELECT name
    FROM main.sqlite_master
    WHERE type = 'view';
""").fetchall()

print(existing_views)

print('drop doing')


print('------------------VIEWS--------------')

#VIEWS CONCLUIDAS
pVendas.execute("""
    CREATE VIEW v_vendas AS
    SELECT
        OPERADOR,
        SUM(TOTAL_PAGO) AS FATURAMENTO,
        SUM(QTD_VENDIDA) AS QTD_TOTAL_VENDIDA,
        COUNT(*) AS QTD_VENDIDA,
        avg(TOTAL_PAGO) AS MEDIA_FATURAMENTO

    FROM Vendas

    WHERE STATUS_VENDA = 'CONCLUIDA'

    GROUP BY OPERADOR;
""")



#VIEWS ESTORNADAS

pVendas.execute("""
    CREATE VIEW vendas_estornada AS
        SELECT
            
            COUNT(*) AS QTD_VENDIDA,
            OPERADOR
    
        FROM Vendas
    
        WHERE STATUS_VENDA = 'ESTORNADA'
        GROUP BY OPERADOR;

""")



#VIEWS EM_ABERTO
pVendas.execute("""
        CREATE VIEW vendas_em_aberto AS
                SELECT
                    OPERADOR,
                    COUNT(*) AS QTD_VENDIDA,
                    SUM(PRECO_UNIT_COBRADO * QTD_VENDIDA) AS FATURAMENTO
            
                FROM Vendas
            
                WHERE STATUS_VENDA = 'EM_ABERTO'
            
                GROUP BY OPERADOR;

""")

print('consult doing')


print('------------------CONSULT DATA--------------')

#create connection
conn = pVendas.connection


#called the view concluidas
views_vendas_concluidas = pd.read_sql_query("SELECT * FROM v_vendas;", conn)

#called the view estornadas
views_vendas_estornadas = pd.read_sql_query("SELECT * FROM vendas_estornada;", conn)

#called the view em_aberto
views_vendas_em_aberto = pd.read_sql_query("SELECT * FROM vendas_em_aberto;", conn)


print('--------------CONCLUIDAS-------------------')

print(views_vendas_concluidas)

print('--------------ESTORNADAS-------------------')

print(views_vendas_estornadas)

print('--------------ABERTO-------------------')

print(views_vendas_em_aberto)