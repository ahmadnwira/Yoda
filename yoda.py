import os
from jinja2 import Template
from misaka import html
from jinja2 import Environment, FileSystemLoader, select_autoescape

BASE_DIR = os.getcwd()
POSTS_DIR = os.path.join(BASE_DIR, 'posts')
HTML_DIR = os.path.join(BASE_DIR, 'html')
THEME_DIR = os.path.join(BASE_DIR, 'theme')

env = Environment(loader=FileSystemLoader(THEME_DIR))


def get_posts():
    for file in os.listdir(POSTS_DIR):
        if file.endswith('.md'):
            yield file


def to_html(templates):
    for post in get_posts():
        # markdwon to html
        with open(os.path.join(POSTS_DIR, post)) as p:
            markdown_html = html(p.read())
        file_name = os.path.splitext(post)[0] + '.html'

        template = env.get_template('post.html')
        open(os.path.join(HTML_DIR, file_name), 'w').write(
            template.render(content=markdown_html)
        )


def yoda():
    if not os.path.exists(HTML_DIR):
        os.mkdir(HTML_DIR)
    to_html(get_posts)

if __name__ == "__main__":
    yoda()
