import json
from config import COMMENTS_FILE



class Comments:

    def load_comments(self):
        '''Открытие JSON файла'''
        with open(COMMENTS_FILE, 'r', encoding='utf-8') as file:
            data_comments = json.load(file)
            return data_comments


    @classmethod
    def load_comment(cls, pk):
        '''Получение комментария по id'''
        comments_id = []
        for i in cls.load_comments(cls):
            if pk == i['post_id']:
                comments_id.append(i)
        return comments_id
