import asyncio
import os
from PIL import Image

async def convert_to_bw(image_path, output_path):
    image = Image.open(image_path)
    bw_image = image.convert("L")
    bw_image.save(output_path)

async def main():
    images = []
    for x in range(1, 18):
        images.append(fr"C:\Users\Zarif\Desktop\imgs\colored\{x}.jpg")
    tasks = []
    for image in images:
        output_filename = os.path.basename(image)
        output_path = fr"C:\Users\Zarif\Desktop\imgs\gray\bw_{output_filename}"
        task = asyncio.create_task(convert_to_bw(image, output_path))
        tasks.append(task)
    await asyncio.gather(*tasks)

asyncio.run(main())
