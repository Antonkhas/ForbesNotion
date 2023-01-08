from flask import Flask

app = Flask(__name__)


@app.route('/')  # слеш означает, что мы отслеживаем главную страницу
def index():
    return 'Hello world'


@app.route('/about')  # после слеша переход к внутренней страницы по отношению к главной
def about():
    return 'About page'

# основным файлом для запуска является main.py, прописываем, что оно должно открываться как фласк приложение
if __name__ == '__main__':
    app.run(debug=True)  #True будет выводить все ошибки на странице, False- не будет