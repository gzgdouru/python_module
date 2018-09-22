from PIL import Image, ImageDraw, ImageFont

if __name__ == "__main__":
    font = ImageFont.truetype(r"F:/font/xiaowei.ttf", 16)
    im = Image.new("RGB", (400, 300))
    draw = ImageDraw.Draw(im)
    draw.text((20, 20), text="hello, 您好!", font=font)
    im.show()