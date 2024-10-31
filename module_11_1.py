# requests
# import requests
#
# res = requests.get('https://stackoverflow.com')
# print(res.content)

# numpy
# import numpy as np
#
# a1 = np.array([1, 2, 3])
# a2 = np.array([[1, 2, 3], [4, 5, 6]])
# a3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#
# print(f'Массив {a1}, количество измерений {a1.ndim}')
# print()
# print(f'Массив {a2}, количество измерений {a2.ndim}')
# print()
# print(f'Массив {a3}, количество измерений {a3.ndim}')
#
# print(a1 + a2)
# print(a2 * 2)
# print(a3 ** 2)

# pillow

from PIL import Image

with Image.open('img.jpg') as img:
    img.load()

print(type(img), img.mode)

img2 = img.resize((800, 600))
img2 = img2.convert("CMYK")
img2 = img2.convert("L")
img2.save('img2.jpg')
print(type(img2), img2.mode)
