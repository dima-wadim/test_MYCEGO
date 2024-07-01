import requests
from PIL import Image
from io import BytesIO


def download_images_from_yandex_disk(folder_url):
    # Здесь нужно реализовать скачивание файлов из папки Яндекс.Диск
    # Например, используя API Яндекс.Диск или другую стратегию для получения файлов
    # В данном примере предполагается, что мы уже имеем ссылки на файлы изображений

    # Пример получения ссылок на файлы изображений
    image_urls = [
        'https://example.com/image1.jpg',  # замените на реальные URL
        'https://example.com/image2.jpg',  # замените на реальные URL
        # добавьте другие ссылки на изображения
    ]
    return image_urls


def download_image(url):
    response = requests.get(url)
    response.raise_for_status()
    return Image.open(BytesIO(response.content))
