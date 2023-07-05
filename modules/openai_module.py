import openai
import requests
from PIL import Image
from io import BytesIO
import os

def apply_magic(auth_token, size, prompt, n_images, directory):
    openai.api_key = auth_token

    tk_img_list = []
    for i in range(n_images):
        response = openai.Image.create(prompt=prompt, n=1, size=size)
        image_url = response["data"][0]["url"]
        img = Image.open(requests.get(image_url, stream=True).raw)

        # Check if the directory exists and create it if it doesn't
        if not os.path.exists(directory):
            os.makedirs(directory)

        img.save(f"{directory}/{prompt}_{i}.png")

        tk_img = ImageTk.PhotoImage(img)
        tk_img_list.append(tk_img)

    return tk_img_list

def enlarge_image(tk_img_list, scale):
    enlarged_images = []
    for tk_img in tk_img_list:
        # 获取原始图像
        img = ImageTk.getimage(tk_img)
        # 调用放大函数
        enlarged_img = enlarge_image(img, scale)
        # 将放大后的图像添加到列表
        enlarged_images.append(enlarged_img)

    tk_img_list = []
    for enlarged_img in enlarged_images:
        # 将放大后的图像转换为Tk PhotoImage对象
        tk_img = ImageTk.PhotoImage(enlarged_img)
        tk_img_list.append(tk_img)

    return tk_img_list

def save_image(tk_img_list, prompt, directory):
    # Check if the directory exists and create it if it doesn't
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i, tk_img in enumerate(tk_img_list):
        img = ImageTk.getimage(tk_img)
        img.save(f"{directory}/{prompt}_{i}.png")
