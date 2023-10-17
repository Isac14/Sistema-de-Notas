from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Aluno(Base):
    __tablename__ = 'alunos'

    matricula = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

    notas = relationship("Nota", back_populates="aluno")

class Nota(Base):
    __tablename__ = 'notas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    matricula_aluno = Column(Integer, ForeignKey('alunos.matricula'), nullable=False)
    materia = Column(String(100), nullable=False)
    nota = Column(Float(precision=4, asdecimal=True, decimal_return_scale=2), nullable=False)
    status = Column(String(10), CheckConstraint("status IN ('Aprovado', 'Reprovado')"), nullable=True)

    aluno = relationship("Aluno", back_populates="notas")