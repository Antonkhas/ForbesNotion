import requests

# смотрим какие методы можно с этим сайтом
res_options = requests.options('https://httpbin.org/')
print('Метод options: ' + res_options.headers['Access-Control-Allow-Methods'])

# можно управлять запросами, используя именованный аргумент params
get_params = {'page': 11, 'product': 'car'}
res_get = requests.get('https://httpbin.org/', params=get_params)
print('Метод get: ' + res_get.url)

# для отправки данных, например форм
post_params = {'user': 'admin', 'password': 'admin_pass1'}
res_post = requests.post('https://httpbin.org/post', data=post_params)
print('Метод post: ')
print(res_post.json())


