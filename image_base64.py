
import base64
import os

folder_path = "images"

image_files = []
for file_name in os.listdir(folder_path):
    if file_name.endswith(".jpg") or file_name.endswith(".JPG"):
        image_files.append(file_name)

index = 1
    
for file_name in image_files:
    image_path = os.path.join(folder_path, file_name)

    with open(image_path,"rb") as image:
       base64_image = base64.b64encode(image.read()).decode()
    
    print(f"Image ID: {index}")
    print(base64_image)
    index += 1
