
import json
from config import FILE


class Posts:

    @staticmethod
    def load_post_from_json():
        '''Открытие JSON файла'''
        with open(FILE, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    @classmethod
    def get_posts_by_user(cls, user_name):
        '''Получение постов юзера по имени'''
        all_post_user = []
        for i in cls.load_post_from_json():
            if i['poster_name'] == user_name:
                all_post_user.append(i)
        if not len(all_post_user):
            return 'Пользователя нет'
        return all_post_user

    @classmethod
    def search_for_posts(cls, query):
        '''Поиск постов по слову'''
        search_posts = []
        for i in cls.load_post_from_json():
            if query in i["content"]:
                search_posts.append(i)
        return search_posts

    @classmethod
    def get_post_by_pk(cls,id):
        '''Получение поста по id'''
        search_posts_id = []
        for i in cls.load_post_from_json():
            if id == i["pk"]:
                search_posts_id.append(i)
        return search_posts_id


