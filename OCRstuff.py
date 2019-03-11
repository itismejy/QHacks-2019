#takes in a list of pages to use OCR to output a text file from a pdf

from wand.image import Image
from PIL import Image as PI
import pyocr
import pyocr.builders
import io

#to be used later to detect words in photo
tool = pyocr.get_available_tools()[0]
lang = tool.get_available_languages()
req_image = []
final_text = []

#opens a pdf file and turns it into a jpeg
image_pdf = Image(filename="./Comm131.pdf",resolution=300)
image_jpeg = image_pdf.convert('jpeg')

#loops through
for img in image_jpeg.sequence:
    img_page = Image(image=img)
    req_image.append(img_page.make_blob('jpeg'))


for img in req_image:
    txt = tool.image_to_string(
        PI.open(io.BytesIO(img)),
        lang=lang,
        builder = pyocr.builders.TextBuilder(),
    )
    final_text.append(txt)

print(final_text)