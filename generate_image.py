from openai import OpenAI
import base64

client = OpenAI(api_key='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')

# 设置 OpenAI API 密钥

# 上传第一张图片（主体）
image_1_path = "12.png"
# image_1 = client.images.generate(file=open(image_1_path), purpose="fine-tune")

# 上传第二张图片（样式参考）
image_2_path = "1.png"
# image_2 = client.images.generate(file=open(image_2_path), purpose="fine-tune")

# Function to encode image to Base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Encode images
image_1_base64 = encode_image(image_1_path)
image_2_base64 = encode_image(image_2_path)

# Use image descriptions in the prompt
prompt = f"Create an image using the following images encoded in Base64: {image_1_base64} and {image_2_base64}. The first image is the subject, and the second image is the style reference."

# Generate new image using the updated prompt
response = client.images.generate(
    model="dall-e-3",  # Use DALL-E model for image generation
    prompt=prompt,
    n=1,
    size="1024x1024"
)

# 打印生成的图像 URL
print(response.data[0].url)