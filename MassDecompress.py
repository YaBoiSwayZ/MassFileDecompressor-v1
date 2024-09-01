import os
import subprocess
import glob
import platform
import tarfile
import gzip
from tqdm import tqdm
from zipfile import ZipFile, BadZipFile
from plyer import notification
from pathlib import Path

def get_downloads_folder():
    if platform.system() == "Windows":
        return os.path.join(Path.home(), "Downloads")
    elif platform.system() == "Darwin":
        return os.path.join(Path.home(), "Downloads")
    else:
        return os.path.join(Path.home(), "Downloads")

def change_directory(target_directory):
    if not os.path.isdir(target_directory):
        print(f"Directory {target_directory} does not exist.")
        notification.notify(
            title="Directory Not Found",
            message=f"Could not find directory: {target_directory}.",
            app_name="File Extractor"
        )
        return False
    os.chdir(target_directory)
    print("Changed to Directory:", os.getcwd())
    return True

def list_compressed_files(supported_extensions):
    compressed_files = []
    for extension in supported_extensions:
        compressed_files.extend(glob.glob(extension))
    return compressed_files

def extract_zip_file(file_to_extract):
    try:
        with ZipFile(file_to_extract, 'r') as zip_ref:
            bad_file = zip_ref.testzip()
            if bad_file:
                print(f"Warning: {file_to_extract} contains a bad file: {bad_file}")
                notification.notify(
                    title="Corrupted File",
                    message=f"File {file_to_extract} contains a bad file: {bad_file}.",
                    app_name="File Extractor"
                )
                return False
            for file in tqdm(zip_ref.namelist(), desc=f"Extracting {file_to_extract}"):
                zip_ref.extract(file)
            print(f"File {file_to_extract} successfully decompressed.")
        return True
    except BadZipFile:
        print(f"Failed to decompress {file_to_extract}. It may be corrupted or not a valid zip archive.")
        notification.notify(
            title="Extraction Failed",
            message=f"Failed to decompress {file_to_extract}. It may be corrupted.",
            app_name="File Extractor"
        )
    except PermissionError:
        print(f"Permission denied: Cannot extract {file_to_extract}. Please check your permissions.")
        notification.notify(
            title="Permission Denied",
            message=f"Cannot extract {file_to_extract}. Check your permissions.",
            app_name="File Extractor"
        )
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        notification.notify(
            title="Unexpected Error",
            message=f"An error occurred while extracting {file_to_extract}.",
            app_name="File Extractor"
        )
    return False

def extract_tar_file(file_to_extract):
    try:
        with tarfile.open(file_to_extract, 'r:*') as tar_ref:
            tar_ref.extractall()
            print(f"File {file_to_extract} successfully decompressed.")
        return True
    except tarfile.TarError as e:
        print(f"Failed to decompress {file_to_extract}. It may be corrupted or not a valid tar archive.")
        notification.notify(
            title="Extraction Failed",
            message=f"Failed to decompress {file_to_extract}. It may be corrupted.",
            app_name="File Extractor"
        )
    except PermissionError:
        print(f"Permission denied: Cannot extract {file_to_extract}. Please check your permissions.")
        notification.notify(
            title="Permission Denied",
            message=f"Cannot extract {file_to_extract}. Check your permissions.",
            app_name="File Extractor"
        )
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        notification.notify(
            title="Unexpected Error",
            message=f"An error occurred while extracting {file_to_extract}.",
            app_name="File Extractor"
        )
    return False

def notify_user(file_to_extract):
    try:
        notification.notify(
            title='Extraction Complete',
            message=f'{file_to_extract} was successfully extracted.',
            app_name='File Extractor'
        )
    except Exception as e:
        print(f"Failed to send notification: {e}")

def extract_all_files(compressed_files):
    for file_to_extract in compressed_files:
        file_extension = os.path.splitext(file_to_extract)[1]
        if file_extension in [".gz", ".tgz", ".tar", ".tar.gz"]:
            success = extract_tar_file(file_to_extract)
        elif file_extension == ".zip":
            success = extract_zip_file(file_to_extract)
        else:
            print(f"Unsupported file format: {file_to_extract}")
            continue
        if success:
            notify_user(file_to_extract)

def extract_compressed_files():
    custom_directory = input("Enter the directory path containing compressed files, or press Enter to use the default Downloads folder: ")
    target_directory = custom_directory if custom_directory else get_downloads_folder()
    if not change_directory(target_directory):
        return
    supported_extensions = ["*.gz", "*.zip", "*.tar", "*.tar.gz", "*.tgz"]
    compressed_files = list_compressed_files(supported_extensions)
    if not compressed_files:
        print("No supported compressed files found in the directory.")
        return
    extract_all = input("Do you want to extract all files? (y/n): ").lower()
    if extract_all == 'y':
        extract_all_files(compressed_files)
        return
    print("Available compressed files:")
    for idx, compressed_file in enumerate(compressed_files, start=1):
        print(f"{idx}: {compressed_file}")
    while True:
        file_index = input(f"Enter the number of the file you want to extract (1-{len(compressed_files)}, or type 'exit' to quit): ")
        if file_index.lower() == "exit":
            break
        if not file_index.isdigit() or not (1 <= int(file_index) <= len(compressed_files)):
            print("Invalid selection. Please choose a valid file number.")
            continue
        file_to_extract = compressed_files[int(file_index) - 1]
        file_extension = os.path.splitext(file_to_extract)[1]
        if file_extension in [".gz", ".tgz", ".tar", ".tar.gz"]:
            success = extract_tar_file(file_to_extract)
        elif file_extension == ".zip":
            success = extract_zip_file(file_to_extract)
        else:
            print(f"Unsupported file format: {file_to_extract}")
            continue
        if success:
            notify_user(file_to_extract)
        exit_choice = input("Do you want to extract another file? (y/n): ")
        if exit_choice.lower() != "y":
            break

extract_compressed_files()
