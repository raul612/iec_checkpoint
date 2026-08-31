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

@app.route("/filmes-em-lancamento", methods=["GET"])
def filmes_em_lancamento():
    lancamentos = [
        {"id": 1, "titulo": "Missao Impossivel: Novo Horizonte", "genero": "Acao", "data_estreia": "15/09/2026"},
        {"id": 2, "titulo": "O Reino Perdido", "genero": "Aventura", "data_estreia": "22/09/2026"},
        {"id": 3, "titulo": "Sombras do Amanha", "genero": "Suspense", "data_estreia": "03/10/2026"},
    ]
    return jsonify(lancamentos)

@app.route("/cardapio", methods=["GET"])
def cardapio():
    itens = [
        {"item": "Pipoca Pequena", "preco": 12.00},
        {"item": "Pipoca Media", "preco": 18.00},
        {"item": "Pipoca Grande", "preco": 24.00},
        {"item": "Refrigerante 500ml", "preco": 9.00},
        {"item": "Combo Casal", "preco": 38.00},
        {"item": "Nachos com Cheddar", "preco": 16.00},
    ]
    return jsonify(itens)


@app.route("/salas", methods=["GET"])
def salas():
    salas = [
        {"numero": 1, "tipo": "Padrão", "capacidade": 120},
        {"numero": 2, "tipo": "3D", "capacidade": 90},
        {"numero": 3, "tipo": "VIP", "capacidade": 40},
        {"numero": 4, "tipo": "IMAX", "capacidade": 150},
    ]

    return jsonify(salas)

@app.route("/promocoes", methods=["GET"])
def promocoes():
    promocoes = [
        {"titulo": "Segunda em Dobro", "descricao": "Compre um ingresso e ganhe outro na segunda-feira"},
        {"titulo": "Meia-entrada Estudante", "descricao": "50% de desconto para estudantes com carteirinha"},
        {"titulo": "Combo Família", "descricao": "4 ingressos + pipoca grande + 4 refrigerantes com desconto"},
        ]
    return jsonify(promocoes)

if __name__ == '__main__':
    app.run(debug=True)