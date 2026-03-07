import os
import shutil


def organizar_descargas():
    categories = {
        "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".jfif"],
        "Documentos": [".pdf",".docx",".doc",".txt",".xlsx",".xls",".pptx",".csv",".md",".mscz",],
        "Programas": [".exe", ".msi"],
        "Comprimidos": [".zip", ".rar", ".7z", ".tar", ".gz", ".iso"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Audio": [".mp3", ".wav", ".flac"],
        "Codigo": [".py",".js",".html",".css",".cpp",".java",".kt",".ipynb",".ts",".sql",],
    }

    print("======= ORGANIZADOR DE DESCARGAS =======")

    home = os.path.expanduser("~")
    opciones = ["Descargas", "Downloads"]
    downloads_path = None

    for o in opciones:
        path = os.path.join(home, o)
        if os.path.exists(path):
            downloads_path = path
            break

    if not downloads_path:
        print(" [!] No se encontro la carpeta de descargas.")
        exit()

    print(f" [+] Iniciando proceso de organizar directorio {downloads_path}")

    for f in os.listdir(downloads_path):
        file_path = os.path.join(downloads_path, f)
        if os.path.isfile(file_path):
            ext = os.path.splitext(f)[1].lower()
            for category, extensions in categories.items():
                if ext in extensions:
                    folder = os.path.join(downloads_path, category)
                    if not os.path.exists(folder):
                        os.makedirs(folder)
                    shutil.move(file_path, os.path.join(folder, f))

    print(f" [+] Directorio {downloads_path} organizado de manera exitosa.")


if __name__ == "__main__":
    organizar_descargas()
