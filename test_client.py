import requests
from PIL import Image
from io import BytesIO


url = "http://localhost:8000/api/v1/"

# Создаем объекты, которые будем отправлять на сервер
person = {"pos": {"x": 10, "y": 20}, "velocity": 1.0}
gas = {"pos": {"x": 30, "y": 40}, "gas": 0}
image = Image.open("test_image.jpg")

# Преобразуем изображение в байты
buffer = BytesIO()
image_bytes = buffer.getvalue()

# Создаем JSON-объект, описывающий объект BaseSettings
base_settings = {"person": person, "gases": [gas], "image": image_bytes.decode('utf-8')}

# Отправляем POST-запрос на сервер
response = requests.post(url, json=base_settings)

# Выводим ответ сервера
print(response.content)
