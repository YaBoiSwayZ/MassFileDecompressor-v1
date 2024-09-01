# File Extractor

This Python script provides a simple and efficient way to extract various compressed files from a specified directory or the default Downloads folder. It supports `.zip`, `.gz`, `.tgz`, `.tar`, and `.tar.gz` file formats. The script includes functionality for user notifications and error handling, making it user-friendly and robust.

## Features

- **Directory Selection:** Choose a custom directory or use the default Downloads folder.
- **Supported Formats:** Automatically detects and extracts `.zip`, `.gz`, `.tgz`, `.tar`, and `.tar.gz` files.
- **User Notifications:** Sends desktop notifications for important events, such as successful extraction or errors.
- **Error Handling:** Handles common errors such as file corruption, permission issues, and unsupported formats.
- **Progress Display:** Shows extraction progress using a progress bar.

## Requirements

- Python 3.x
- Modules:
  - `os`
  - `subprocess`
  - `glob`
  - `platform`
  - `tarfile`
  - `gzip`
  - `tqdm`
  - `zipfile`
  - `plyer`
  - `pathlib`

You can install the required modules using `pip`:

```
pip install tqdm plyer
```

## How to Use

1. **Clone the Repository:**

   ```
   git clone https://github.com/YaBoiSwayZ/MassFileDecompressor-v1.git
   cd MassFileDecompressor-v1-main
   ```

2. **Run the Script:**

   Execute the script in your terminal:

   ```
   python MassDecompress.py
   ```

3. **Select Directory:**

   - You will be prompted to enter a directory path. Press Enter to use the default Downloads folder.

4. **Extract Files:**

   - The script will list all supported compressed files in the selected directory.
   - You can choose to extract all files or select individual files by their index.

## Notifications

- The script uses the `plyer` module to send desktop notifications for:
  - Successful extractions
  - Corrupted files
  - Permission issues

## Usage

1. Run the script:

   ```
   python MassDecompress.py
   ```

2. Select files to extract from the listed options or choose to extract all.

## Contribution

Feel free to contribute to this project by submitting issues or pull requests. For major changes, please open an issue to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [tqdm](https://github.com/tqdm/tqdm) for the progress bar.
- [plyer](https://github.com/kivy/plyer) for desktop notifications.
