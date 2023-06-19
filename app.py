from flask import Flask,jsonify,render_template
from scrap import fun
app=Flask(__name__)

@app.route('/api/coins')
def bit_route():
    datas=fun()
    return jsonify(datas)
@app.route('/')
def Hello():
    datas=fun()
    return render_template('index.html',datas=datas)


if __name__ == "__main__":
    app.run(debug=True)