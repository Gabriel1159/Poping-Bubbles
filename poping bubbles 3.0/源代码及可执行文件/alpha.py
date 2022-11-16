# 修改图片透明度
def change_alpha(image, alpha=255):
    width, height = image.get_size()
    for x in range(0, width):
        for y in range(0, height):
            r, g, b, old_alpha = image.get_at((x, y))
            if old_alpha>0:
                image.set_at((x, y), (r, g, b, alpha))