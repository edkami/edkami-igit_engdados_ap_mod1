from sqlalchemy import create_engine


def inserir_dados(dicionario, tabela):
    engine = create_engine('postgresql://postgres:local@localhost/livraria', echo=True)
    dicionario.to_sql(tabela, con=engine, if_exists='append', index=False)
