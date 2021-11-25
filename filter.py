from PIL import Image
import numpy as np


def convert_image_to_mosaic(image, size, gradation_step):
    """
    :param image:
    :param size:
    :param gradation_step:
    :return image:
    """

    for x in range(0, len(image), size):
        for y in range(0, len(image[0]), size):
            image[x:x + size, y:y + size] = get_average_brightness(
                image[x:x + size, y:y + size], size, gradation_step)
    return image


def get_average_brightness(block, size, gradation_step):
    """
    Возвращает среднюю яркость с оттенками серого
    :param block:
    :param size:
    :param gradation_step:
    :return int:

    >>> get_average_brightness(np.array([[[1, 2, 3], [4, 5, 6]]]), 50, 5)
    0

    >>> get_average_brightness(np.array([[[15, 10, 11]], [[40, 11, 15]]]), 150, 10)
    0
    """
    average_color = (block[:size, :size].sum() / 3) // size ** 2
    return int(average_color // gradation_step) * gradation_step


def main():
    image_file = Image.open(input("Введите имя файла, которое хотите конвертировать: "))
    block_size = int(input("Введите размер блока: "))
    gradations_count = int(input("Введите количество градаций серого: "))
    image = np.array(image_file)
    gradation_step = 255 // gradations_count

    done = convert_image_to_mosaic(image, block_size, gradation_step)

    res = Image.fromarray(done)
    res.save(input("Введите имя файла, в которой хотите сохранить результат: "))


if __name__ == '__main__':
    main()
