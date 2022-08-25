import json


def load_posts() -> list[dict]:
    """Make a Py-list from JSON"""
    with open('posts.json', 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def get_posts_by_word(word: str) -> list[dict]:
    """Finds a suitable posts with certain word"""
    suitable_posts = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            suitable_posts.append(post)
    return suitable_posts


def save_picture(picture) -> str:
    """Save user's picture in our directory"""
    filename = "/" + picture.filename
    path = f"./uploads/images/{filename}"

    picture.save(path)

    return path


def add_post(post: dict) -> dict:
    """Add new user post in posts list"""
    posts = load_posts()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file)
    return post


