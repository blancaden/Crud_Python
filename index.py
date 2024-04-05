from src import init__app
from config import config

configuracion = config ['development']

app = init__app(configuracion)

if __name__ == '__main__':
    app.run()