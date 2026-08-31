from flask import Flask, jsonify;

app = Flask(__name__)

@app.route('/')
def status():
    return {'servico': 'Cinema', 'status': 'online'}


@app.route("/filmes-em-cartaz", methods=["GET"])
def filmes_em_cartaz():
    filmes = [
        {"id": 1, "titulo": "Guerra nas Estrelas: Nova Jornada", "genero": "Ficção Científica", "classificacao": "12 anos"},
        {"id": 2, "titulo": "Comédia da Vida", "genero": "Comédia", "classificacao": "Livre"},
        {"id": 3, "titulo": "Terror na Noite", "genero": "Terror", "classificacao": "16 anos"},
    ]
    return jsonify(filmes)

@app.route("/horarios", methods=["GET"])
def horarios():
    horarios = [
        {"filme": "Guerra nas Estrelas: Nova Jornada", "sessoes": ["14:00", "16:30", "19:00", "21:30"]},
        {"filme": "Comédia da Vida", "sessoes": ["13:00", "15:30", "18:00", "20:15"]},
        {"filme": "Terror na Noite", "sessoes": ["22:00", "00:00"]},
    ]
    return jsonify(horarios)


if __name__ == '__main__':
    app.run(debug=True)