from PIL import Image

ascii_chars = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

# 调整图像大小
def resize_image(image,new_width = 100):
    width, height = image.size
    ratio = float(height) / float(width) / 0.6
    new_height = int(ratio * new_width)
    resized_image = image.resize((new_height, new_width))
    return resized_image

# 将图像转化为灰度图
def grayify(image):
    return image.convert('L')

# 将像素值映射到字符集
def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = " "
    for pixel in pixels:
        ascii_str += ascii_chars[pixel // 32]
    return ascii_str

# 将图片转换为ASCII字符画
def image_to_ascii(image_path,new_width = 100):
    # 检测能否打开图像
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return
    # 对图片进行处理
    image = resize_image(image, new_width)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join([ascii_str[index:(index + img_width)] for index in range(0, ascii_str_len, img_width)])
    print(ascii_img)
    return ascii_img


# 保存文件到txt中
def save_ascii_art(ascii_img, output_file):
    with open(output_file, "w") as f:
        f.write(ascii_img)

image_path = 'white.jpg' # 这里填想要转换的图片
ascii_img = image_to_ascii(image_path)
if ascii_img is not None: # 确保image_to_ascii成功执行
    save_ascii_art(ascii_img, "output.txt")
else:
    print("无法打开图像或转换失败。")

