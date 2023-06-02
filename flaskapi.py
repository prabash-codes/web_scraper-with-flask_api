from flask import Flask, jsonify
import  sqlite3

app = Flask(__name__)
@app.route('/api', methods=['GET'])

def get_data():
    conn = sqlite3.connect('database.sqlite3')
    cursor = conn.cursor()
    data = cursor.execute("SELECT * FROM flaskapi_table").fetchall()


    return jsonify({'data': data})

@app.route('/api/<int:id>', methods=['GET'])
def get_id(id):
    conn = sqlite3.connect('database.sqlite3')
    cursor = conn.cursor()
    data = cursor.execute("SELECT * FROM flaskapi_table WHERE id = ?", (id,)).fetchall()

    return jsonify({'data': data})

if __name__ == '__main__':
    app.run(debug=True)