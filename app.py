from flask import Flask, render_template, request
import webbrowser
from threading import Timer
import os
import signal


app = Flask(__name__)
browser_opened = False  # Flag petru a preveni deschiderea browserului de 2 ori

@app.route("/", methods=["GET", "POST"])
def declaratie():
    if request.method == "POST":
        # Preia datele introduse de utilizator
        data = request.form
        return render_template("pv_defiscalizare.html", submitted_data=data)
    return render_template("pv_defiscalizare.html", submitted_data=None)

@app.route("/shutdown", methods=["POST"])
def shutdown():
    #Oprește serverul
     os.kill(os.getpid(), signal.SIGTERM)
     return "Server stopped."

def open_browser():
    webbrowser.open("http://127.0.0.1:5000/")

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=False) # se pune True cand rulezi in python iar false ca executabil



