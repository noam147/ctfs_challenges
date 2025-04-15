import os
import zipfile
import io
CURRENT_ID = 0

def is_zip(file) -> bool:
    return file and file.filename.endswith('.zip')
def get_txt_from_zip(file):
    zip_file = zipfile.ZipFile(file.stream)
    # Find the first .txt file in the archive
    for name in zip_file.namelist():
        if name.endswith('.txt'):
            # Extract the first .txt file content
            txt_file = zip_file.open(name)
            return txt_file

    return None
def save_response_to_machine(content_from_bard,option):
    global CURRENT_ID
    folder_path = "responses"
    file_path = os.path.join(folder_path, f"res{CURRENT_ID}.txt")
    CURRENT_ID += 1
    os.makedirs(folder_path, exist_ok=True)

    file_text = f"<h1>OPTION:{option}</h1><br>{content_from_bard}"
    with open(file_path,"w",encoding="utf-8") as f:
        f.write(file_text)
def save_response_to_machine_user_mode(content_from_bard,option,fileid):
    folder_path = "user_responses"
    file_path = os.path.join(folder_path, f"{fileid}.txt")
    os.makedirs(folder_path, exist_ok=True)
    file_text = f"<h1>OPTION:{option}</h1><br>{content_from_bard}"
    with open(file_path,"w",encoding="utf-8") as f:
        f.write(file_text)
def count_files_in_folder(folder_path):
    try:
        return len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
    except FileNotFoundError:
        print("Folder not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
def set_current_id():
    global CURRENT_ID
    CURRENT_ID = count_files_in_folder("responses")