from PIL import Image

def create_tiff(images, output_path):
    base_image = images[0]
    layers = images[1:]
    base_image.save(output_path, save_all=True, append_images=layers, format='TIFF')
