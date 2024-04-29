from io import BytesIO

import aiohttp
import asyncio
import time
import tkinter as tk
from PIL import Image, ImageTk


async def download_image(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            image_data = await response.read()
            print(f"Downloaded image from {url}")
            return image_data


async def main():
    start_time = time.time()
    urls = []
    for x in range(1, 18):
        urls.append(f"http://xom91k.beget.tech/ege/img/ex/{x}.jpg")
    images = []
    for url in urls:
        image_data = await download_image(url)
        image = Image.open(BytesIO(image_data))
        images.append(image)
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time} seconds")
    #Отображение изображений в окне
    root = tk.Tk()
    tk_images = []
    for image in images:
        tk_images.append(ImageTk.PhotoImage(image))
    for x in range(17):
        label = tk.Label(root, image=tk_images[x])
        label.pack()

    root.mainloop()


if __name__ == "__main__":
    asyncio.run(main())
