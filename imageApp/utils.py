from django.core.files import File

from re import search
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
from io import BytesIO
from PIL import Image

def get_remote_image(url: str):
    if url:
        title = search(r"([-\w]+\.(?:jpg|gif|png|jpeg))", url)
        title = title[1] if title else None
        image_temp = NamedTemporaryFile(delete=True)
        image_temp.write(urlopen(url).read())
        image_temp.flush()
        return File(image_temp), title

def resize_image(image, size: tuple):
    if 0 in size:
        basewidth, baseheight = image.origin.width, image.origin.height
        size = find_rotation(size, basewidth, baseheight)
    img = Image.open(image.origin.path)
    type = image.origin.path.split('.')[-1].upper()  # GET IMAGE TYPE
    img.convert('RGB')
    img.thumbnail(size, Image.EXTENT)  # resize image
    thumbnail_io = BytesIO()
    img.save(thumbnail_io, type, quality=85)  # save image to BytesIO object
    thumbnail = File(thumbnail_io, name=image.origin.name)  # create a django friendly File object

    return thumbnail


def find_rotation(size: tuple, basewidth, baseheight):
    """ Определение нехватающее пропорциональной ширины или длины """
    widht, height = size
    if widht:
        ratio = basewidth / widht
        height = int((float(baseheight) * float(ratio)))
        return (widht, height)
    if height:
        ratio = baseheight / height
        height = int((float(basewidth) * float(ratio)))
        return (widht, height)
