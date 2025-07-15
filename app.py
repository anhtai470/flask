from flask import Flask

app = Flask(trananhtai)

@app.route('/')
def home():
    return "10 diem nha thay!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
