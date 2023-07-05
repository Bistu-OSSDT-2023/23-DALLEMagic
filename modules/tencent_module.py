import requests
from PIL import Image
import base64
from io import BytesIO

def cartoonize_image(img, tencent_api_key):
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
            return cartoonized_img
        else:
            print("Error: ", result)
    else:
        print("Request failed, status code: ", response.status_code)
