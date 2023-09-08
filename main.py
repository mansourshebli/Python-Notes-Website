from website import create_app

app = create_app()

# If we run this file app.run will be excuted
if __name__ == 'main':
    app.run(debug=True)
