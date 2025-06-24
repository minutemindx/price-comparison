from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
return "Fiyat karsilastirma sistemi basariyla calisiyor!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
