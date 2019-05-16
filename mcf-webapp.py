from app import app

if __name__ == '__main__':
    new_app = app.create_app()
    new_app.run(debug=True, host='0.0.0.0')
