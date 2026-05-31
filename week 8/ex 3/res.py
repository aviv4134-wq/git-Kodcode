import requests

re = requests.get('http://127.0.0.1:8000/calc/1/mul/4')

print(re.json())