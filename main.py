import os
import shutil

class Colors:
    GREEN = '\033[92m'
    RED = '\033[31m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

def print_header():
    width = 42
    line = "=" * width
    title = "🧹 Downloads Organizer 🐍"
    
    print(f"{Colors.CYAN}{Colors.BOLD}{line}")
    print(f"{title.center(width)}")
    print(f"{line}{Colors.RESET}\n")

def choose_dir(directories:list):
    print(" [📂] Choose a folder to organize:")
    for i, folder in enumerate(directories, 1):
        print(f"    {i}. ~/{folder}")

    while(True):
        try:
            op = input("\n    Number: ")
            option = int(op)

            if option == 0:
                print(" [👋] Exiting...")
                exit()

            if option > len(directories) or option < 1:
                print(f"{Colors.RED} [❌] Invalid number, choose a folder between 1 and {len(directories)}...{Colors.RESET}")
            else:
                break

        except ValueError as e:
            print(f"{Colors.RED} [❌] Invalid input! Please enter a number.{Colors.RESET}")

    folder = directories[option - 1]
    print(f"\n [📍] Chosen: {folder}\n")
    return folder

def organize_folder(folder_path):
    categories = {
        "Images": [".jpg", ".jpeg", ".ico", ".png", ".gif", ".webp", ".jfif", ".svg", ".heic", ".psd", ".ai"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".csv", ".md", ".mscz", ".rtf", ".odt"],
        "Books": [".epub", ".mobi", ".azw3"],
        "Executables": [".exe", ".msi", ".deb", ".rpm", ".appimage"],
        "Compressed": [".zip", ".rar", ".7z", ".tar", ".gz", ".iso"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
        "Audio": [".mp3", ".wav", ".flac", ".m4a", ".aac", ".ogg"],
        "Source": [".ttf", ".otf", ".woff", ".woff2"],
        "Code": [".py", ".js", ".html", ".css", ".cpp", ".java", ".kt", ".ipynb", ".ts", ".sql", ".json", ".xml", ".yaml", ".yml", ".sh", ".bat"],
    }
    
    print(f" [📍] Path: {folder_path}")
    print(f" [⚙️] Starting process...\n")

    current_script = os.path.basename(__file__)

    for f in os.listdir(folder_path):
        if f == current_script:
            continue
        file_path = os.path.join(folder_path, f)
        if os.path.isfile(file_path):
            ext = os.path.splitext(f)[1].lower()
            for category, extensions in categories.items():
                if ext in extensions:
                    folder = os.path.join(folder_path, category)
                    if not os.path.exists(folder):
                        os.makedirs(folder)
                    shutil.move(file_path, os.path.join(folder, f))

    print(f"{Colors.GREEN} [✅] Directory {folder_path} successfully organized. 🧹🐍{Colors.RESET}")

if __name__ == "__main__":
    print_header()
    
    home = os.path.expanduser("~")
    directories = [d for d in os.listdir(home) if os.path.isdir(os.path.join(home, d))]    
    folder_name = choose_dir(directories)
    folder_path = os.path.join(home, folder_name)
    organize_folder(folder_path)
