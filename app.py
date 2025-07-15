import os
from flask import Flask

app = Flask(__name__)  # phải là __name__ (chuỗi có 2 dấu gạch dưới)

@app.route('/')
def home():
    return "10 diem nha thay!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
