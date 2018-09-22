from PIL import Image
from PIL import ImageFilter

if __name__ == "__main__":
    im = Image.open(r"F:/images/zongzi.png")
    floatim = Image.open("thumbnail.png")
    # im.paste(floatim, (150, 50))
    # im.show()

    # nim = im.crop((700, 300, 1500, 1300))
    # nim.show()
    # nim.thumbnail((400, 400))
    # nim.show()

    im.show()
    for i in range(20):
        im = im.filter(ImageFilter.BLUR)
    im.show()
