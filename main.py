from images.download_images import download_images_from_yandex_disk, download_image
from utils.create_tiff import create_tiff


def main(folder_names):
    output_path = 'Result.tif'
    all_images = []

    for folder_name in folder_names:
        folder_url = f'https://disk.yandex.ru/d/V47MEP5hZ3U1kg/{folder_name}'
        image_urls = download_images_from_yandex_disk(folder_url)

        for url in image_urls:
            image = download_image(url)
            all_images.append(image)

    create_tiff(all_images, output_path)
    print(f'TIFF файл создан и сохранен как {output_path}')


if __name__ == '__main__':
    folder_names = ['1388_12_Наклейки 3-D_3']
    main(folder_names)
