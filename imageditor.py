from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageFont
import os  # import the os iteraction with the file systems

path = "./imgs" # folder for unedited images
pathOut = "./editedimgs" # folder for edited images

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    # sharpening, BW
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(0)

    # contrast
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)


    edit=img.filter(ImageFilter.BoxBlur(4))
   

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')