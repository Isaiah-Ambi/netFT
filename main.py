import socket
import os
from flask import Flask, request, send_file, render_template_string
import qrcode
from io import BytesIO

app = Flask(__name__)

# HTML template for the upload page
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>File Transfer</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { 
            font-family: Arial, sans-serif; 
            max-width: 800px; 
            margin: 20px auto; 
            padding: 0 20px; 
        }
        .files { 
            margin: 20px 0; 
            padding: 10px; 
            background: #f5f5f5; 
        }
        .upload-form {
            margin: 20px 0;
            padding: 20px;
            background: #e9e9e9;
        }
    </style>
</head>
<body>
    <h1>Local File Transfer</h1>
    
    <div class="upload-form">
        <h2>Upload File</h2>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
    </div>

    <div class="files">
        <h2>Available Files</h2>
        <ul>
            {% for file in files %}
                <li>
                    <a href="/download/{{ file }}">{{ file }}</a>
                </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
'''

def get_local_ip():
    """Get the local IP address of the machine"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # This doesn't actually create a connection
        s.connect(('8.8.8.8', 80))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template_string(HTML_TEMPLATE, files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        return f'File {file.filename} uploaded successfully', 200

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(UPLOAD_FOLDER, filename))

@app.route('/qr')
def get_qr():
    """Generate QR code for easy mobile access"""
    ip = get_local_ip()
    url = f'http://{ip}:5000'
    
    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save to bytes
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    ip = get_local_ip()
    print(f"Server running at http://{ip}:5000")
    print(f"Scan QR code at http://{ip}:5000/qr")
    app.run(host='0.0.0.0', port=5000)