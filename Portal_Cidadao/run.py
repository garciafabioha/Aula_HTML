from app import create_app

app = create_app()

if __name__ == "__main__":
    # debug=True facilita o desenvolvimento (recarrega sozinho,
    # mostra erros detalhados no navegador). Em produção isso
    # deve ser desligado.
    app.run(debug=True)
