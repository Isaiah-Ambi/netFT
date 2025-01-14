# Local File Transfer

A simple web-based file transfer application that allows you to easily share files between devices on your local network. Perfect for quickly transferring photos, documents, and other files between your phone and computer without using the internet or external services.

## Features

- Web-based interface accessible from any device with a browser
- Easy file upload and download
- Mobile-friendly design
- QR code generation for quick mobile access
- Works on any local network
- No file size limitations (other than your device's memory)
- No internet connection required
- Supports all file types

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone this repository or download the script:
```bash
git clone [your-repository-url]
# or just save the Python script as file_transfer.py
```

2. Install the required packages:
```bash
pip install flask qrcode pillow
```

## Usage

1. Run the server:
```bash
python file_transfer.py
```

2. The script will print two URLs:
   - The main application URL (e.g., `http://192.168.1.100:5000`)
   - The QR code URL (e.g., `http://192.168.1.100:5000/qr`)

3. To access from another device:
   - Computer: Open the main URL in your web browser
   - Phone: Either scan the QR code or enter the URL manually
   
Note: Both devices must be connected to the same WiFi network.

## How It Works

- The application creates a lightweight web server on your local network
- Files are stored in an 'uploads' folder in the same directory as the script
- The server automatically detects your local IP address
- You can upload files from any device and download them from any other device on the network

## Security Considerations

- The application is intended for use on trusted local networks only
- There is no authentication system - anyone on your network can access the application
- Don't run this on public networks without adding security measures
- The server accepts all file types, so be careful what you download

## Troubleshooting

If you can't connect to the server:
1. Ensure both devices are on the same network
2. Check if your firewall is blocking port 5000
3. If the automatic IP detection fails, you can manually set your IP address in the code
4. Some networks may block device-to-device communication; try using a different network

## Contributing

Feel free to fork this project and submit pull requests with improvements. Some ideas for enhancements:
- Add authentication
- Add file deletion capability
- Add progress bars for large file transfers
- Add drag-and-drop upload support
- Add multiple file selection
- Add file preview capabilities

## License

This project is licensed under the MIT License - feel free to use it for any purpose.

## Acknowledgments

This project uses:
- Flask for the web server
- qrcode for QR code generation
- Python's built-in socket library for network detection
