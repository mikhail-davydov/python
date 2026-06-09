import re


def normalize_jpeg(filename):
    return re.sub(r'jpe?g$', 'jpg', filename, flags=re.I)


print(normalize_jpeg('stepik.jPeG'))
print(normalize_jpeg('mountains.JPG'))
print(normalize_jpeg('windows11.jpg'))
print(normalize_jpeg('stepik.jpeg.jpeg'))