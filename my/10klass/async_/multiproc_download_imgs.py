from io import BytesIO
import requests
from multiprocessing import Pool
import tkinter as tk
from PIL import Image, ImageTk

def download_image(url):
    response = requests.get(url)
    image_data = response.content
    print(f"Downloaded image from {url}")
    return image_data

def process_image(url):
    image_data = download_image(url)
    image = Image.open(BytesIO(image_data))
    # Дополнительная обработка изображения, если необходимо
    return image

def main():
    urls = []
    for x in range(1, 18):
        urls.append(f"http://xom91k.beget.tech/ege/img/ex/{x}.jpg")

    with Pool() as pool:
        images = pool.map(process_image, urls)

    root = tk.Tk()
    tk_images = []
    for image in images:
        tk_images.append(ImageTk.PhotoImage(image))

    row = 0
    column = 0

    for x in range(17):
        label = tk.Label(root, image=tk_images[x])
        label.grid(row=row, column=column)

        column += 1
        if column == 6:
            row += 1
            column = 0

    root.mainloop()

if __name__ == "__main__":
    main()