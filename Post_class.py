
import json
from config import FILE


class Posts:

    def load_post_from_json(self):
        '''Открытие JSON файла'''
        with open(FILE, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data


    def get_posts_by_user(self, all_users, user_name):
        '''Получение постов юзера по имени'''
        all_post_user = []
        for i in all_users:
            if i['poster_name'] == user_name:
                all_post_user.append(i)
        if not len(all_post_user):
            return 'Пользователя нет'
        return all_post_user


    def search_for_posts(self, all_posts, query):
        '''Поиск постов по слову'''
        search_posts = []
        for i in all_posts:
            if query in i["content"]:
                search_posts.append(i)
        return search_posts


    def get_post_by_pk(self, id_posts, id):
        '''Получение поста по id'''
        search_posts_id = []
        for i in id_posts:
            if id == i["pk"]:
                search_posts_id.append(i)
        return search_posts_id


