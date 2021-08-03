from flask import Flask, render_template, request
import danhdaucau;
app = Flask(__name__)


@app.route("/danhdaucau",methods=["POST","GET"])
def danhdau():
    if request.method == 'POST':
        ip = request.form["inputdt"]
        if ip == "":
            return render_template("danhdaucau.html")
        else:
            inp = danhdaucau.dankdaucau(ip)
            return render_template("danhdaucau.html",inp=inp)
    else:
        return render_template("danhdaucau.html")
    render_template("danhdaucau.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
