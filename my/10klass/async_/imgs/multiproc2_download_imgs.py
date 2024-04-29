import tkinter as tk
from PIL import ImageTk, Image
import requests
from io import BytesIO
import multiprocessing

def download_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    return image

def update_image(image):
    label = tk.Label(root, image=image)
    label.grid(row=row, column=column)

    column += 1
    if column == 6:
        row += 1
        column = 0

def worker(url):
    image = download_image(url)
    update_image(image)

if __name__ == "__main__":
    urls = [
        "https://example.com/image1.jpg",
        "https://example.com/image2.jpg",
        "https://example.com/image3.jpg",
        # добавьте другие URL-адреса изображений здесь
    ]

    root = tk.Tk()
    row = 0
    column = 0

    processes = []
    for url in urls:
        process = multiprocessing.Process(target=worker, args=(url,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    root.mainloop()