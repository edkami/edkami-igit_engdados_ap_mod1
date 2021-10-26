from sqlalchemy import (create_engine, Column, Integer,
                        String, Float, Text, Time, Date,
                        ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy_utils import database_exists, create_database

Base = declarative_base()


# Criação da tabela livro
class Livro(Base):
    __tablename__ = 'livro'
    id = Column('id', Integer, primary_key=True)
    titulo_livro = Column('titulo_livro', String)
    numero_edicao = Column('numero_edicao', Integer)
    ano_edicao = Column('ano_edicao', Integer)
    codigo_editora = Column('codigo_editora', Integer, ForeignKey('editora.codigo_editora'))
    idioma = Column('idioma', String)
    area_conhecimento = Column('area_conhecimento', Integer, ForeignKey('area_conhecimento.id'))
    preco = Column('preco', Float(10, 2))
    isbn = Column('ISBN', String, unique=True, nullable=True)

    # Relação
    editora_id = relationship('Editora', foreign_keys=codigo_editora)
    area_conhecimento_id = relationship('AreaConhecimento', foreign_keys=area_conhecimento)


# Criação da tabela editora
class Editora(Base):
    __tablename__ = 'editora'
    codigo_editora = Column('codigo_editora', Integer, primary_key=True)
    nome_editora = Column('nome_editora', String)
    pais = Column('pais', String)
    cidade = Column('cidade', String, nullable=True)


# Criação da tabela area conhecimento
class AreaConhecimento(Base):
    __tablename__ = 'area_conhecimento'
    id = Column('id', Integer, primary_key=True)
    descricao = Column('descricao', String)


# Criação da tabela autor
class Autor(Base):
    __tablename__ = 'autor'
    id = Column('id', Integer, primary_key=True)
    nome = Column('nome', String)
    pais_nacimento = Column('paisnascimento', String)
    biografia = Column('biografia', Text, nullable=True)


# Criação da tabela exemplar
class Exemplar(Base):
    __tablename__ = 'exemplar'
    id = Column('id_exemplar', Integer, primary_key=True)
    id_livro = Column('id_livro', Integer, ForeignKey('livro.id'))
    isbn = Column('ISBN', String, ForeignKey('livro.ISBN'))
    volume = Column('volume', Integer)
    situacao = Column('situacao', String)
    # Relação
    livro_id = relationship('Livro', foreign_keys=id_livro)
    isbn_livro = relationship('Livro', foreign_keys=isbn)


# Criação da tabela autoria
class Autoria(Base):
    __tablename__ = 'autoria'
    id_livro = Column('id_livro', Integer, ForeignKey('livro.id'), primary_key=True)
    id_autor = Column('idautor', Integer, ForeignKey('autor.id'), primary_key=True)

    # Relação
    livro_id = relationship('Livro', foreign_keys=id_livro)
    autor_id = relationship('Autor', foreign_keys=id_autor)


# Criação da tabela usuario
class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column('id', Integer, primary_key=True)
    nome = Column('nome', String)
    cpf = Column('cpf', String)
    rg = Column('rg', String)
    data_nascimento = Column('data_nascimento', Date)
    sexo = Column('sexo', String)
    email = Column('email', String)
    cep = Column('cep', String)
    logradouro = Column('logradouro', String)
    num = Column('num', Integer)
    bairro = Column('bairro', String)
    cidade = Column('cidade', String)
    uf = Column('uf', String)
    telefone_fixo = Column('telefone_fixo', String)
    celular = Column('celular', String)
    status = Column('status', String)


# Criação da tabela emprestimo
class Emprestimos(Base):
    __tablename__ = 'emprestimos'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    id_exemplar = Column('id_exemplar', Integer, ForeignKey('exemplar.id_exemplar'))
    id_usuario = Column('id_usuario', Integer, ForeignKey('usuario.id'))
    data_emprestimo = Column('data_emprestimo', Date)
    data_prevista_devolucao = Column('data_prevista_devolucao', Date)
    data_devolucao = Column('data_devolucao', Date)
    hora_devolucao = Column('hora_devolucao', Time)

    # Relação
    exemplar_id = relationship('Exemplar', foreign_keys=id_exemplar)
    usuario_id = relationship('Usuario', foreign_keys=id_usuario)


def create_db():
    # Criação do banco de dados caso não exista
    usuario_bd = 'user'
    senha = 'password'
    engine = create_engine(f'postgresql://{usuario_bd}:{senha}@localhost/livraria', echo=True)
    if not database_exists(engine.url):
        create_database(engine.url)
    print(f'Banco de dados criado: {database_exists(engine.url)}')
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
