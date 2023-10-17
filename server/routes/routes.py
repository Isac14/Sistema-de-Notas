from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from server.entities.entities import Nota, Aluno
from flask import request, jsonify

engine = create_engine('postgresql://postgres:142804@localhost:5432/sistema_notas')
Session = sessionmaker(bind=engine)

def create_routes(app):
    @app.route('/')
    def home():
        return 'x'
    @app.route('/get/notas', methods=['GET'])
    def get_notas():
        try:
            session = Session()
            notas = session.query(Nota).all()
            response = [
                {
                    "materia": nota.materia,
                    "nota": nota.nota,
                    "status": nota.status
                }
                for nota in notas
            ]
            return jsonify(response), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            session.close()

    @app.route('/matricula', methods=['POST'])
    def matricula():
        session = Session()
        try:
            data = request.json
            matricula = data

            aluno = session.query(Aluno).filter_by(matricula=matricula).first()

            if not aluno:
                return jsonify({"error": "Aluno não encontrado"}), 404

            notas = aluno.notas
            response = [
                {
                    "materia": nota.materia,
                    "nota": nota.nota,
                    "status": nota.status
                }
                for nota in notas
            ]

            return jsonify(response), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            session.close()