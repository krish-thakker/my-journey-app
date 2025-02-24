import requests

url = 'http://127.0.0.1:5000/logs'

files = {
    'images': ('tokyo.jpeg', open('tokyo.jpeg', 'rb'), 'image/jpeg')
}

data = {
    'place_name': 'Tokyo',
    'description': 'The vibrant capital of Japan, known for its skyscrapers',
    'latitude': '35.6762',
    'longitude': '139.6503'
}

response = requests.post(url, files=files, data=data)
print(response.status_code)
print(response.text)