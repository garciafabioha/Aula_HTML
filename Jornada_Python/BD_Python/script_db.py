from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from unidecode import unidecode
#configurar o banco de dados escolhido
engine = create_engine("sqlite:///database.db")
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    tipo = Column(String, nullable=False)

def criar_tabela():
    Base.metadata.create_all(engine)

def insert_usuario(nome_usuario, tipo_usuario):
    session = Session()
    try:
        if nome_usuario and tipo_usuario:
            usuario = Usuario(nome=nome_usuario, tipo=tipo_usuario)
            session.add(usuario)
            session.commit()
            print(f"Usuário {nome_usuario} cadastrado com sucesso!")
        else:
            print("É obrigatório preencher o nome e tipo do usuário!")
    except Exception as e:
        session.rollback()
        print(f"Ocorreu um erro ao tentar cadastrar o usuário {nome_usuario}: {e}")
    finally:
        session.close()

def select_usuarios(nome_usuario=''):
    session = Session()
    try:
        dados = session.query(Usuario).all()
        if nome_usuario:
            busca = unidecode(nome_usuario).lower()
            dados = [u for u in dados if busca in unidecode(u.nome).lower()]
        return dados
    except Exception as e:
        print(f"Ocorreu algum erro ao consultar o(s) usuário(s): {e}")
        return []
    finally:
        session.close()

def update_usuarios(id_usuario, nome_usuario):
    session = Session()
    try:
        if id_usuario and nome_usuario:                          # ← bug corrigido
            usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
            if usuario:
                usuario.nome = nome_usuario
                session.commit()
                print(f"Usuário ID {id_usuario} atualizado para '{nome_usuario}'!")
            else:
                print(f"Usuário ID {id_usuario} não encontrado!")
        else:
            print("É obrigatório informar o id e o novo nome do usuário!")
    except Exception as e:
        session.rollback()
        print(f"Ocorreu algum erro ao atualizar o usuário: {e}")
    finally:
        session.close()

def delete_usuarios(id_usuario):
    session = Session()
    try:
        if id_usuario:                          
            usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
            if usuario:
                session.delete(usuario)
                session.commit()
                print(f"Usuário ID {id_usuario} apagado com sucesso'!")
            else:
                print(f"Usuário ID {id_usuario} não encontrado!")
        else:
            print("É obrigatório informar o id do usuário a ser apagado!")
    except Exception as e:
        session.rollback()
        print(f"Ocorreu algum erro ao apagar o usuário: {id_usuario}")
    finally:
        session.close()