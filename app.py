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


if __name__ == '__main__':
    app.run(debug=True)