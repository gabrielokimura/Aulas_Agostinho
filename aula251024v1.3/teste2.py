from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base


bd = create_engine("sqlite:///banco_sqlachemy.db")

Session = sessionmaker(bind = bd)

session = Session()

Base = declarative_base()


# Parte de tabelas

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email= Column("email", String)
    senha= Column("senha", String)
    ativo= Column("ativo", Boolean)

    def __init__(self, nome, email, senha, ativo = True):
        self.nome = nome 
        self.email = email
        self.senha = senha 
        self.ativo = ativo



class Livro(Base):
    __tablename__ = "livros"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String)
    qtdade_pag = Column("qtdade_pag", Integer)
    dono =Column("dono", ForeignKey("usuarios.id"))


    def __init__(self, titulo, qtdade_pag, dono):
        self.titulo =titulo
        self.qtdade_pag = qtdade_pag
        self.dono = dono






Base.metadata.create_all(bind = bd)








usuario = Usuario(nome="Kiki", email = "gg@gmail.com", senha = "123")
session.add(usuario)
session.commit()





lista_usuarios = session.query(Usuario).all()
print(lista_usuarios)



livro = Livro(titulo = "SLA", qtdade_pag=3, dono=True)