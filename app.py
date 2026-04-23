from flask import Flask
import os

app = Flask(__name__)
STORAGE_PATH = "/data/visits.txt"

@app.route('/')
def hello():
    # Ensure directory exists
    os.makedirs(os.path.dirname(STORAGE_PATH), exist_ok=True)
    # Read/Write visit count from Persistent Volume
    count = 0
    if os.path.exists(STORAGE_PATH):
        with open(STORAGE_PATH, "r") as f:
            count = int(f.read())
    count += 1
    with open(STORAGE_PATH, "w") as f:
        f.write(str(count))

    return f"""
    <html>
        <body style="font-family: sans-serif; text-align: center; margin-top: 50px;">
            <h1>Custom Web App on AKS</h1>
            <p>This application is serving custom content and tracking visits.</p>
            <div style="font-size: 24px; color: #0078d4;">
                Total Visits: <b>{count}</b>
            </div>
            <p><small>Data is stored on an Azure Managed Disk via Persistent Volume.</small></p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
