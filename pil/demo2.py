from PIL import Image

if __name__ == "__main__":
    im = Image.open(r"F:/images/zongzi.png")
    # width = 400
    # ratio = float(width) / im.size[0]
    # height = int(im.size[1] * ratio)
    # nim = im.resize((width, height), Image.BILINEAR)
    # print(nim.size)
    # im.save("demo2.png")

    # im.rotate(45, Image.BILINEAR).show()
    #
    # im.transpose(Image.ROTATE_90).show()

    im.thumbnail((400, 100))
    im.save("thumbnail.png")
    print(im.size)