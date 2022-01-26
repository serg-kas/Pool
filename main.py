import poolmodule as pool
import cv2
from os import listdir
from random import randint

import warnings
warnings.filterwarnings("ignore")

# Параметры для вызова функции модуля
model_FILE = 'best.pt'       # веса
img_PATH = 'images'              # папка откуда берем картинки для обработки
out_PATH = 'images_out'          # папка куда помещаем результат

if __name__ == '__main__':
    img_files = sorted(listdir(img_PATH))
    out_files = sorted(listdir(out_PATH))
    files = []
    for f in img_files:
        if not (('out_'+f) in out_files):
            files.append(f)
    if len(files)==0:        # если все файлы уже были обработаны
        files = img_files    # то будем брать любой из имеющихся
    # если список не пуст выбираем случайный файл
    if len(files) > 0:
        idx = randint(0, len(files) - 1)
        img_FILE = img_PATH + '/' + files[idx]
        out_FILE = out_PATH + '/' + 'out_' + files[idx]
        # Вызываем функцию из модуля и получаем пути к файлам картинок
        out_FILE = pool.detect(model_FILE, img_FILE, out_FILE)
        # out_FILE = pool.detect(model_FILE, img_FILE)
        # print(out_FILE)
        out_image = cv2.imread(out_FILE)
        cv2.imshow('image', out_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:
        print('В папке images пусто')




