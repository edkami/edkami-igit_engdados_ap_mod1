import pandas as pd
from create_banco_dados import create_db
from insert_dados import inserir_dados

# Importando o arquivo xlsx no pandas
file = 'datasetTP.xlsx'
xls_file = pd.ExcelFile(file)

# Criando dicionários de dados para cada shape do excel
dfs_editora = pd.read_excel(xls_file, 'editora')
dfs_area_conhecimento = pd.read_excel(xls_file, 'area_conhecimento')
dfs_autor = pd.read_excel(xls_file, 'autor')
dfs_livro = pd.read_excel(xls_file, 'livro')
dfs_autoria = pd.read_excel(xls_file, 'autoria')
dfs_exemplar = pd.read_excel(xls_file, 'exemplar')
dfs_usuario = pd.read_excel(xls_file, 'usuario')
dfs_emprestimo = pd.read_excel(xls_file, 'emprestimos')


# Criar banco de dados
create_db()

# Inserir dados
inserir_dados(dfs_editora, 'editora')
inserir_dados(dfs_area_conhecimento, 'area_conhecimento')
inserir_dados(dfs_autor, 'autor')
inserir_dados(dfs_usuario, 'usuario')
inserir_dados(dfs_livro, 'livro')
inserir_dados(dfs_exemplar, 'exemplar')
inserir_dados(dfs_autoria, 'autoria')
inserir_dados(dfs_emprestimo, 'emprestimos')



