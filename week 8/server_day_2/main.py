import requests

users = requests.get('https://jsonplaceholder.typicode.com/users')
posts = requests.get('https://jsonplaceholder.typicode.com/posts')
post_user_2 = requests.get('https://jsonplaceholder.typicode.com/posts?userID=2')
post_user_2 = post_user_2.json()
posts = posts.json()
users = users.json()
#print(f'Name:{respond['name']}\nEmail: {respond['email']}\nCity: {respond['address']['city']}')
#print(f'the number of posts is {len(posts)}')
#print(post_user_2)
#print(respond)
print(posts)
print(users)

def safe_get(url):
    respond = requests.get(url)
    if respond.status_code == 200:
        return respond.json()
    elif respond.status_code == 404:
        return None
    else:
        raise Exception(respond.status_code)
for post in posts:
    for user in users:
        if user['id'] == post['userId']:
            print(f'{post['title']},{user['name']}')
#safe_get('https://jsonplaceholder.typicode.com/posts')