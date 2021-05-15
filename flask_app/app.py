import flask, io, json, os, base64, requests
from flask import Flask, url_for, render_template, redirect, request, jsonify
from PIL import Image
from draw_text import draw
from generate_test import main


app = Flask(__name__)

app.config["DEBUG"] = False


def to_string(name):
    with open(name, "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())
    return converted_string


@app.route('/post/img/<string:id>', methods=['GET', 'POST'])
def home(id):
    print(os.getcwd())
    print(id)
    draw(id)
    main(id)
    img = to_string(f'{id}_test.png')
    print(img.decode('utf-8'))
    return {id: img.decode('utf-8')}


@app.route('/image', methods=['GET', 'POST'])
def first():
    path = 'C:/Users/HP/OneDrive/Изображения/Снимки экрана/2021-05-08.png'


if __name__ == '__main__':
    app.run()

#добавить бд чтобы если такие есть уже заготовки, то просто скидывать их, а не заново генерировать
# + вариации цветов добавить

