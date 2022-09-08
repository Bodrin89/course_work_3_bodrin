import json

COMMENTS_FILE = './data/comments.json'


class Comments:

    def load_comments(self):
        '''Открытие JSON файла'''
        with open(COMMENTS_FILE, 'r', encoding='utf-8') as file:
            data_comments = json.load(file)
            return data_comments

    def load_comment(self, all_comment, pk):
        '''Получение комментария по id'''

        comments_id = []
        for i in all_comment:
            if pk == i['post_id']:
                comments_id.append(i)
        return comments_id
