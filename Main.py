import tkinter as tk
from tkinter.simpledialog import askfloat
import customtkinter as ctk
import openai
from PIL import Image, ImageTk
import os
from io import BytesIO
import base64
import requests

# 创建应用程序窗口
app = tk.Tk()
app.geometry("800x750")
app.title("DALL·E Magic  By Group23 ")
ctk.set_appearance_mode("dark")

# 创建画布和滚动条的框架
frame = tk.Frame(app)
frame.place(x=10, y=420)

# 创建垂直滚动条
vbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
vbar.pack(side=tk.RIGHT, fill=tk.Y)

# 创建水平滚动条
hbar = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
hbar.pack(side=tk.BOTTOM, fill=tk.X)

# 创建画布
main_image = tk.Canvas(frame, width=768, height=300, yscrollcommand=vbar.set,
                       xscrollcommand=hbar.set)
main_image.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

# 配置滚动条
vbar.config(command=main_image.yview)
hbar.config(command=main_image.xview)

# 创建输入框：OpenAI密钥
auth_token_input = ctk.CTkEntry(
    master=app,
    height=40,
    width=512,
    text_color="black",
    fg_color="white",
    placeholder_text="请输入OpenAI密钥:",
)
auth_token_input.place(x=144, y=10)

# 创建输入框：提示语
prompt_input = ctk.CTkEntry(
    master=app,
    height=40,
    width=512,
    text_color="black",
    fg_color="white",
    placeholder_text="输入提示语.",
)
prompt_input.place(x=144, y=60)

# 创建输入框：图像尺寸
size_input = ctk.CTkEntry(
    master=app,
    height=40,
    width=512,
    text_color="black",
    fg_color="white",
    placeholder_text="输入图像尺寸 (如:512x512).",
)
size_input.place(x=144, y=110)

# 创建输入框：保存目录
directory_input = ctk.CTkEntry(
    master=app,
    height=40,
    width=512,
    text_color="black",
    fg_color="white",
    placeholder_text="输入保存图像的目录.",
)
directory_input.place(x=144, y=160)

# 创建输入框：生成图像数量
n_images_input = ctk.CTkEntry(
    master=app,
    height=40,
    width=512,
    text_color="black",
    fg_color="white",
    placeholder_text="输入要生成的图像数量.",
)
n_images_input.place(x=144, y=210)

# 创建输入框：腾讯云API密钥
tencent_api_key_input = ctk.CTkEntry(
    master=app,
    height=40,
    width=512,
    text_color="black",
    fg_color="white",
    placeholder_text="请输入腾讯云API密钥:",
)
tencent_api_key_input.place(x=144, y=260)


def apply_magic():
    global img
    global tk_img_list

    auth_token = auth_token_input.get()
    openai.api_key = auth_token

    size = size_input.get()
    prompt = prompt_input.get()
    n_images = int(n_images_input.get())
    directory = directory_input.get()

    tk_img_list = []
    for i in range(n_images):
        response = openai.Image.create(prompt=prompt, n=1, size=size)
        image_url = response["data"][0]["url"]
        img = Image.open(requests.get(image_url, stream=True).raw)

        # 检查目录是否存在，如果不存在则创建
        if not os.path.exists(directory):
            os.makedirs(directory)

        img.save(f"{directory}/{prompt}_{i}.png")

        tk_img = ImageTk.PhotoImage(img)
        tk_img_list.append(tk_img)

    for i, tk_img in enumerate(tk_img_list):
        main_image.create_image(i * 512, 0, anchor=tk.NW, image=tk_img)
        # 更新滚动区域
        main_image.config(scrollregion=main_image.bbox("all"))
    print("请输入图片关键词:", prompt)


magic_button = ctk.CTkButton(
    master=app,
    height=40,
    width=120,
    text_color="white",
    fg_color=("white", "gray38"),
    command=apply_magic,
)
magic_button.configure(text="生成图像")
magic_button.place(x=100, y=350)


def enlarge_image():
    global img
    global tk_img_list

    scale = askfloat("放大倍数", "输入所需放大倍数:")

    if scale is not None:
        enlarged_images = []
        for tk_img in tk_img_list:
            # 获取原始图像
            img = ImageTk.getimage(tk_img)
            # 调整图像尺寸
            img = img.resize((int(img.width * scale), int(img.height * scale)), Image.LANCZOS)  # Changed here
            # 将放大后的图像添加到列表
            enlarged_images.append(img)

        tk_img_list = []
        for enlarged_img in enlarged_images:
            # 将放大后的图像转换为Tk PhotoImage对象
            tk_img = ImageTk.PhotoImage(enlarged_img)
            tk_img_list.append(tk_img)

        main_image.delete("all")  # 清空画布
        for i, tk_img in enumerate(tk_img_list):
            main_image.create_image(i * 512, 0, anchor=tk.NW, image=tk_img)
            # 更新滚动区域
            main_image.config(scrollregion=main_image.bbox("all"))


enlarge_button = ctk.CTkButton(
    master=app,
    height=40,
    width=120,
    text_color="white",
    fg_color=("white", "gray38"),
    command=enlarge_image,
)
enlarge_button.configure(text="放大图像")
enlarge_button.place(x=260, y=350)


def save_image():
    global img
    global tk_img_list

    prompt = prompt_input.get().replace(" ", "_")
    directory = directory_input.get()

    # 检查目录是否存在，如果不存在则创建
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i, tk_img in enumerate(tk_img_list):
        img = ImageTk.getimage(tk_img)
        img.save(f"{directory}/{prompt}_{i}.png")


save_button = ctk.CTkButton(
    master=app,
    height=40,
    width=120,
    text_color="white",
    fg_color=("white", "gray38"),
    command=save_image,
)
save_button.configure(text="保存图像")
save_button.place(x=420, y=350)


def cartoonize_image():
    global img
    global tk_img_list

    tencent_api_key = tencent_api_key_input.get()

    # 将图片转换为base64编码
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    # 构造请求数据
    data = {
        "Action": "FaceCartoonPic",
        "Version": "2020-03-04",
        "Region": "ap-guangzhou",  # 你需要替换为你的实际Region
        "Image": img_str,
        "RspImgType": "base64"
    }

    # 发送请求
    response = requests.post("https://ft.tencentcloudapi.com", headers={"Authorization": "Bearer " + tencent_api_key},
                             data=data)

    # 检查响应状态
    if response.status_code == 200:
        # 解析响应数据
        result = response.json()
        if "Response" in result and "ResultImage" in result["Response"]:
            # 将返回的base64编码的图片转换为Image对象
            cartoonized_img = Image.open(BytesIO(base64.b64decode(result["Response"]["ResultImage"])))
            # 将Image对象转换为Tk PhotoImage对象
            cartoonized_tk_img = ImageTk.PhotoImage(cartoonized_img)
            # 在Canvas上显示图片
            main_image.create_image(0, 0, anchor=tk.NW, image=cartoonized_tk_img)
        else:
            print("Error: ", result)
    else:
        print("Request failed, status code: ", response.status_code)


cartoonize_button = ctk.CTkButton(
    master=app,
    height=40,
    width=120,
    text_color="white",
    fg_color=("white", "gray38"),
    command=cartoonize_image,
)
cartoonize_button.configure(text="卡通化图像")
cartoonize_button.place(x=580, y=350)

app.mainloop()
