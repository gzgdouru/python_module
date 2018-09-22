from PIL import Image

if __name__ == "__main__":
    im = Image.open(r"F:/images/zongzi.png")
    # im.show()
    print(im.format, im.size, im.mode)
    r, g, b, a = im.split()
    im = Image.merge("RGB", (r, g, b))
    im.save("demo1.jpg")
    # im.show()