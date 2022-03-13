import json


def post_finder(word):
    posts_to_return = []
    with open('posts.json', encoding='utf-8') as file:
        file = file.read()
        file = json.loads(file)
        for i in file:
            if word.lower() in i['content'].lower():
                posts_to_return.append(i)
    return posts_to_return


def post_saving(picture, content):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    filename = picture.filename
    extension = filename.split(".")[-1]
    if extension not in ALLOWED_EXTENSIONS:
        return False
    picture_link = f"./uploads/images/{filename}"
    picture.save(picture_link)
    with open('posts.json', 'r+', encoding='utf-8') as file:
        info = file.read()
        info = json.loads(info)
        picture_link = picture_link.replace('.', 'http://127.0.0.1:5000', 1)
        info.append({'pic': picture_link, 'content': content})
        info = json.dumps(info)
        file.seek(0)
        file.write(info)
    return picture_link



