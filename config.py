
import logging

COMMENTS_FILE = './data/comments.json'
FILE = './data/posts.json'

logger_api = logging.getLogger("one")
logger_api.setLevel(logging.INFO)
file_handler_one = logging.FileHandler("./logs/basic.log")
formatter_one = logging.Formatter("%(asctime)s : %(message)s")
file_handler_one.setFormatter(formatter_one)
logger_api.addHandler(file_handler_one)
