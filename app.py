from flask import Flask, request, render_template, send_from_directory
import logging
import functions
from main.views import main_blueprint

logging.basicConfig(filename="basic.log")

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    logging.info("Главная страница запрошена")
    return render_template('index.html')


@app.route("/list")
def page_tag():
    pass


@app.route("/post", methods=["GET", "POST"])
def page_post_form():
    return render_template('post_form.html')


@app.route("/upload", methods=["POST"])
def page_post_upload():
    picture = request.files.get("picture")
    content = request.form.get('content')
    if picture:
        try:
            picture_link = functions.post_saving(picture, content)
            if picture_link:
                return render_template('post_uploaded.html', picture=picture_link, content=content)
            else:
                logging.info("Загруженный файл - не картинка")
                return """
                <h1>А ЧЕ ЭТО ЗА РАЗРЕШЕНИЕ НЕ ПОНЯЛ</h1>
                <h2>ПЕРЕДЕЛЫВАЙ</h2>
                <h3>!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!</h3>
                """
        except:
            logging.exception("Ошибка при загрузке файла")
            return '<h1>Ошибка при загрузке файла</h1>'
    else:
        logging.info("Загруженный файл - не картинка")
        return """
        <h1>А ГДЕ ФОТО НЕ ПОНЯЛ</h1>
        <h2>ПЕРЕДЕЛЫВАЙ</h2>
        <h3>!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!</h3>
        """


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


@app.route('/search/')
def search_page():
    logging.info("Поиск постов запрошен")
    s = request.args.get('s')
    posts = functions.post_finder(s)
    return render_template('post_list.html', s=s, posts=posts)


app.register_blueprint(main_blueprint)

app.run()
