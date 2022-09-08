import json

POST_PATH = "posts.json"


def load_posts():
    """
    Загрузка файла json
    """
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_posts_by_word(word):
    """
    Функция для нахождения постов через поиск
    """
    result = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            result.append(post)
    return result


def save_picture(picture):
    """
    Сохранение переданной картинки
    """
    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(path)
    return path


def func_add_post(post):
    """
    Сохранение поста в файл со всеми постами
    """
    posts = load_posts()
    posts.append(post)
    with open(POST_PATH, 'w', encoding='utf-8') as file:
        json.dump(posts, file)
    return post
