import os
from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader('theme'))

POST_TEMPLATE = env.get_template('post.html')
INDEX_TEMPLATE = env.get_template('index.html')
