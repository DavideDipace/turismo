from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def citta():
  return render_template("citta.html")

@app.route('/Venezia')
def Venezia():
    return render_template("Venezia.html")

@app.route('/Milano')
def Milano():
    return render_template("Milano.html")

@app.route('/Firenze')
def Firenze():
    return render_template("Firenze.html")

@app.route('/Napoli')
def Napoli():
    return render_template("Napoli.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
