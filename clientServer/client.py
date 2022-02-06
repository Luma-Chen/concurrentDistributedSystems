import pip._vendor.requests as request

url = 'http://localhost:8080/'
path = 'path008'
print(f'Pode me prestar um serviço?')

response = request.get(url + path)
print(f'Serviço prestado pela {response.text}')
input() 