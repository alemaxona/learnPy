# -*- coding: utf-8 -*-

# Framework - другое название библиотеки
# Flask Самый простой фрэймворк(micro (значит - очень маленький) framework) для web разработки (Соболев Н.)
# Django - огромный, полноценный фрэймворк.
# Концепции WEB приложения: MVC - Model | View | Controller
# Model - хранит данные, View - отображает данные, Controller - котнотролирует отображение, хранение и т.д.
# (Flask) Routes - Устанваливает соотвествие мужу URL адресои и функцией виду View

# Подвид MVC: MVT - Model | View | Template

# Компоненты Flak:
# Web-server - Werkzeug (веркзоег) (библиотека которая лежит в основе Flask и работает с
# протоколом WSGI - (Web Server Gateway Interface)
# По сути можно использовать его и не сипользовать Flask, но он сложный, к примеру описывать Routes!


from flask import Flask

app = Flask(__name__)  # Controller


@app.route('/')  # /test - http://127.0.0.1:5000/test
def home():
    return 'hello world!'  # 'Hello world' - В данном случае - это View


@app.route('/test')
def home2():
    return 'hello User!'


@app.route('/hello/<user>')  # С параметром <имя параметра>
def home(user):
    return 'hello user: ' + user


@app.route('/<num1>,<num2>')
def usr_sum(num1, num2):
    rez = int(num1) + int(num2)
    return 'sum: ' + str(rez)


# Model(логины, пароли, отчеты...) тут нет, мы не храним данные, текст - это больше отобрпжение (View)
if __name__ == '__main__':
    app.run()
