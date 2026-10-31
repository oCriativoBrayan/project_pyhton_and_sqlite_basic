# Estudo de Joins em SQLite com Python

Este projeto tem como objetivo praticar e demonstrar o funcionamento de diferentes tipos de junções (`JOINS`) em bases de dados relacionais utilizando **Python** e **SQLite**.

## 📂 Estrutura do Projeto

Na pasta CRUD do projeto, encontram-se vários scripts que executam consultas específicas:
* `head.py` - Instancia conexão com banco de dados via SQLite3.
* `create.py` - Cria a tabela com dados.
* `update.py` - Realiza à atualização dos dados, usando informações incluidas pelo input.
* `select.py` - Seleciona dados da tabela.
* `insert.py` - Insere dados na tabela, utilizando input.
* `delete.py` - Deleta dados da tabela.
* `base.py` - Chama a função desejada.


Na pasta JOINs do projeto, encontram-se vários scripts que executam consultas específicas:
* `innerjoin.py` - Retorna apenas os registos que possuem correspondência exata em ambas as tabelas[cite: 1].
* `leftjoin.py` - Retorna todos os registos da tabela da esquerda e os correspondentes da tabela da direita.
* `rightjoin.py` - Retorna todos os registos da tabela da direita e os correspondentes da tabela da esquerda.
* `fulljoin.py` - Retorna todos os registos quando há uma correspondência em qualquer uma das tabelas.
* `crossjoin.py` - Produz o produto cartesiano entre as tabelas envolvidas.

## ⚙️ Tecnologias Utilizadas
* **Python**
* **SQLite** (Base de dados relacional leve)
* **Pandas** (Para manipulação e exibição dos DataFrames no terminal)

## 🚀 Como Executar

1. Certifique-se de que tem o Python instalado juntamente com as bibliotecas necessárias (como o `pandas`).
2. Abra o terminal na pasta do projeto (`studySQLite`).
3. Execute o script desejado, por exemplo:
   ```bash
   python innerjoin.py

Descrição corrigida por IA. :)
