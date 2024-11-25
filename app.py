from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Define the directory where the file is stored
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Base directory of the app
DOWNLOAD_DIR = os.path.join(BASE_DIR, 'static')  # Directory containing the PDF file

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download-card")
def download_card():
    # Send the file to the client for download
    filename = "Ibukun_Ogunleye.zip"  # Replace with your actual file name
    return send_from_directory(DOWNLOAD_DIR, filename, as_attachment=True)

if __name__ == "__main__":
    from waitress import serve
    # Uncomment this line for development
    app.run(debug=True, port=5001)
    # Uncomment this line for production
    # serve(app, host='0.0.0.0', port=5001)
