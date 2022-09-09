
import logging
from flask import Flask, request, render_template, jsonify
from Post_class import *
from Comments_class import *


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

load_post_from_json = Posts.load_post_from_json(FILE)
get_posts_by_user = Posts()
get_posts = Posts()
get_post_by_id = Posts()

get_comments_id = Comments()

# Домашняя страница
@app.route('/')
def home_page():
    title = 'Главная страница'
    home_page = render_template('home_page.html', posts=load_post_from_json, title=title)
    return home_page

#Получение постов юзера по имени
@app.route('/user/<name_user>')
def user(name_user):
    title = f'Посты пользователя {name_user}'
    posts = get_posts_by_user.get_posts_by_user(load_post_from_json, name_user)
    if type(posts) == str:
        return posts
    user_post = render_template('home_page.html', posts=posts, title=title)
    return user_post

# Переход на страницу поиска
@app.route("/search")
def search_page():
    title = 'Страница поиска'
    search_post_user = render_template('search_page.html', title=title)
    return search_post_user

# Поиск постов по слову
@app.route('/found/posts')
def get_found_posts():
    text = request.args.get("search_text")
    posts = get_posts.search_for_posts(load_post_from_json, text)
    found_post = render_template('home_page.html', posts=posts)
    return found_post


# Переход по кнопке "Подробнее" к полному посту и коментариям
@app.route('/found/id/<int:id_post>')
def get_found_posts_id(id_post):
    posts = get_post_by_id.get_post_by_pk(load_post_from_json, id_post)
    id_comment = get_comments_id.load_comment(id_post)
    count_comments = len(get_comments_id.load_comment(id_post))
    found_post_id = render_template('found_post_id.html', posts=posts, id_comment=id_comment,
                                    count_comments=count_comments)
    return found_post_id

@app.route('/api/post')
def load_json():
    data = load_post_from_json
    logger_one = logging.getLogger("one")
    file_handler_one = logging.FileHandler("./logs/basic.log")
    formatter_one = logging.Formatter("%(asctime)s : %(message)s")
    file_handler_one.setFormatter(formatter_one)
    logger_one.addHandler(file_handler_one)
    logger_one.critical(f"Запрос /api/posts")
    return jsonify(data)

@app.route('/api/post/<int:post_id>')
def get_json_post_id(post_id):
    data = get_post_by_id.get_post_by_pk(load_post_from_json, post_id)
    logger_one = logging.getLogger("one")
    file_handler_one = logging.FileHandler("./logs/basic.log")
    formatter_one = logging.Formatter("%(asctime)s : %(message)s")
    file_handler_one.setFormatter(formatter_one)
    logger_one.addHandler(file_handler_one)
    logger_one.critical(f"Запрос /api/posts {post_id}")
    return jsonify(data)

if __name__ == '__main__':
    app.run()
