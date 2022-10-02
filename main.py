from flask import Flask, jsonify
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'containers-us-west-20.railway.app'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'A7'
app.config['MYSQL_DB'] = 'railway'
app.config['MYSQL_PORT'] = '6348'
 
mysql = MySQL(app)


@app.route('/')
def index():
    return jsonify({"Its Me": " Welcome Thewakar"})










if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
