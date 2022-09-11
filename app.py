

from flask import Flask, request, render_template, jsonify
from post_class import Posts
from comments_class import Comments
from config import logger_api

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


# Домашняя страница
@app.route('/')
def home_page():
    load_post_from_json = Posts.load_post_from_json()
    title = 'Главная страница'
    home_page = render_template('home_page.html', posts=load_post_from_json, title=title)
    return home_page

#Получение постов юзера по имени
@app.route('/user/<name_user>')
def user(name_user):
    title = f'Посты пользователя {name_user}'
    posts = Posts.get_posts_by_user(name_user)
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
    posts = Posts.search_for_posts(text)
    found_post = render_template('home_page.html', posts=posts)
    return found_post


# Переход по кнопке "Подробнее" к полному посту и коментариям
@app.route('/found/id/<int:id_post>')
def get_found_posts_id(id_post):
    posts = Posts.get_post_by_pk(id_post)
    id_comment = Comments.load_comment(id_post)
    count_comments = len(Comments.load_comment(id_post))
    found_post_id = render_template('found_post_id.html', posts=posts, id_comment=id_comment,
                                    count_comments=count_comments)
    return found_post_id

@app.route('/api/post')
def load_json():
    data = Posts.load_post_from_json()
    logger_api.info(f"Запрос /api/posts")
    return jsonify(data)

@app.route('/api/post/<int:post_id>')
def get_json_post_id(post_id):
    data = Posts.get_post_by_pk(post_id)
    logger_api.info(f"Запрос /api/posts/ {post_id}")
    return jsonify(data)

if __name__ == '__main__':
    app.run()
