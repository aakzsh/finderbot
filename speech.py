import requests
data = {
    'api_token': 'your api token',
    'return': 'apple_music,spotify',
}
files = {
    'file': open('bs.mp3', 'rb'),
}
result = requests.post('https://api.audd.io/', data=data, files=files)
print(result.text)