import json

POST_PATH = "posts.json"


def load_posts():
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_posts_by_word(word):
    result = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            result.append(post)
    return result


def save_picture(picture):
    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(path)
    return path