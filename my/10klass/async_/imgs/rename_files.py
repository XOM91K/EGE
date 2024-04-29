import os
def rename_files(folder_path):
    files = os.listdir(folder_path)
    jpg_files = [file for file in files if file.endswith(".jpg")]

    for i, file in enumerate(jpg_files, start=1):
        new_name = f"{i}.jpg"
        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed {file} to {new_name}")


if __name__ == "__main__":
    folder_path = r"C:\Users\Zarif\PycharmProjects\EGE\my\10klass\async_\imgs\imgss"  # Замените на путь к вашей папке
    rename_files(folder_path)