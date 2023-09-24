from ultralytics import YOLO
from PIL import Image

# Устанавливаем качество сжатия (1 - наихудшее качество, 95 - наилучшее качество)
compression_quality = 30
# Устанавливаем качество сжатия разрешения (в процентах)
size_compression = 100


def image_compression(image):
    width, height = image.size
    if (width < 600) or (height < 600):
        return image
    # Устанавливаем новое разрешение (ширину и высоту)
    new_width = (width // 100) * size_compression  # Новая ширина в пикселях
    new_height = (height // 100) * size_compression  # Новая высота в пикселях
    # Изменяем разрешение изображения
    return image.resize((new_width, new_height))


# Открываем изображение
input_image_path = 'temp\\pic.jpg'
output_image_path = 'temp\\compressed_pic.jpg'
# Открываем изображение с помощью Pillow
image = Image.open(input_image_path)

resized_image = image_compression(image)
# Сжимаем изображение и сохраняем его
resized_image.save(output_image_path, format="JPEG", quality=compression_quality)

# Определение типа детали
model = YOLO('best.pt')
# img_path = output_image_path
results = model.predict(
    output_image_path,
    save=True,
    project='temp', 
    name='result'
)




