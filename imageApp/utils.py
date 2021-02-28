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
    img = Image.open(image.origin.path)
    img.convert('RGB')
    img.thumbnail(size)  # resize image
    thumbnail_io = BytesIO()
    img.save(thumbnail_io, 'JPEG', quality=85)  # save image to BytesIO object
    thumbnail = File(thumbnail_io, name=image.origin.name)  # create a django friendly File object

    return thumbnail