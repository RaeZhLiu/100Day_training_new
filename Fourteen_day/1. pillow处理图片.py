from PIL import Image, ImageFilter

if __name__ == "__main__":
    # 读取图像
    image = Image.open('./image-show.png')
    image.format, image.size, image.mode
    ('JPEG', (500, 750), 'RGB')
    image.show()
    # 裁剪图片
    rect = 80, 20, 310, 360
    image.crop(rect).show()
    # 缩略图
    size = 128, 128
    image.thumbnail(size)
    image.show()
    # 缩放及粘贴图像
    image1 = Image.open('./image-putpixel.png')
    image2 = Image.open('./image-show.png')
    rect_2 = 80, 20, 310, 360
    guidao_head = image2.crop(rect_2)
    width, height = guidao_head.size
    image1.paste(guidao_head.resize((int(width), int(height))), (192, 285))
    # 旋转和翻转图片, 旋转180°及左右翻转
    image2.rotate(180).show()
    image2.transpose(Image.FLIP_LEFT_RIGHT).show()
    # 操作像素
    for x in range(80, 310):
        for y in range(20, 360):
            image2.putpixel((x, y), (128, 128, 128))

    image2.show()
    # 滤镜效果
    image3 = Image.open('./image-show.png')
    image3.filter(ImageFilter.CONTOUR).show()