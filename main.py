from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')  # слеш означает, что мы отслеживаем главную страницу
@app.route('/home') # можно дописывать таким образом, тогда просто / и /home будут выводить один и тот же текст
def index():
    return render_template('index.html')  # теперь у нас открывается шаблон index.html


@app.route('/about')  # после слеша переход к внутренней страницы по отношению к главной
def about():
    return 'About page'


@app.route('/user/<string:name>/<int:id>') # таким образом можно в url прописывать имена и id
def user(name, id):
    return 'User page: ' + name + ' - ' + str(id) #id меняем запись, тк принимается число, а выводится строка


# основным файлом для запуска является main.py, прописываем, что оно должно открываться как фласк приложение
if __name__ == '__main__':
    app.run(debug=True)  #True будет выводить все ошибки на странице, False- не будет
