import os
from misaka import html
from yaml import load
from theme import INDEX_TEMPLATE, POST_TEMPLATE

BASE_DIR = os.getcwd()
POSTS_DIR = os.path.join(BASE_DIR, 'posts')
HTML_DIR = os.path.join(BASE_DIR, 'html')
PROJECT_TITLE = 'Yoda'


def _convert_filename(file_name, new_ext=".html"):
    return os.path.splitext(file_name)[0] + new_ext


def get_posts():
    for file in os.listdir(POSTS_DIR):
        if file.endswith('.md'):
            yield file


def parse_file(file, have_content=True):
    with open(os.path.join(POSTS_DIR, file)) as f:
        all_content = f.read()

    meta, content = all_content.split('====', maxsplit=1)
    if not have_content:
        return load(meta)

    return load(meta), content


def render_html(file_name, meta=None, content=None, template=POST_TEMPLATE):
    open(os.path.join(HTML_DIR, file_name), 'w').write(
        template.render(
            content=content,
            data=meta
        )
    )


def md_to_html(posts, template=POST_TEMPLATE):
    """
        takes list of markdown files and genereate html
        files based on a template you specify
    """
    for post in posts:
        meta, content = parse_file(post)
        markdown_toHtml = html(content)

        try:
            file_name = meta.get('title').replace(" ", "") + '.html'
        except:
            file_name = _convert_filename(post)

        render_html(file_name, content=markdown_toHtml, meta=meta)


def generate_index(files):
    titles = [
        {
            'title': parse_file(file, have_content=False).get('title'),
            'url': _convert_filename(file)
        }
        for file in files
    ]
    render_html(
        'index.html',
        content=titles,
        meta={'title': 'index', 'project_name': PROJECT_TITLE},
        template=INDEX_TEMPLATE
    )


def yoda():
    if not os.path.exists(HTML_DIR):
        os.mkdir(HTML_DIR)

    generate_index(get_posts())
    md_to_html(get_posts())


if __name__ == "__main__":
    yoda()
