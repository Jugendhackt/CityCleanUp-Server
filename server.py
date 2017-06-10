from flask import Flask
from flask import request
import sqlite3
import os
from flask import jsonify

if os.path.exists("citycleanup.db")==False:
    conn = sqlite3.connect('citycleanup.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE Verschmutzung
    (
    ID INTEGER NOT NULL,
    LAENGE FLOAT,
    BREITE FLOAT,
    VERSCHMUTZUNGSGRAD INTEGER,
    BESCHREIBUNG TEXT,
    PRIMARY KEY (ID)
    )''')
else:
    conn = sqlite3.connect('citycleanup.db')
    c = conn.cursor()

app = Flask(__name__)

#@app.route('/api/submit', methods=['POST'])
#def submit():
#    c.execute("insert into user(username, password) values(?, ?)", (request.form['laenge'], request.form['breite'], request.form['verschmutzungsgrad'], request.form['verschmurtungsgrad']))
#    return 'success', 200

@app.route('/api/get_markers', methods=['GET'])
def get_markers():
    c.execute("SELECT * FROM Verschmutzung;")
    out=''
    test=["wfewfewq", "fffaf"]
    for table_row in c:
        out=out+jsonify(id=row[0], laenge=row[1], breite=row[2], verschmutzungsgrad=row[3], beschreibung=row[4]+","
    return out, 200

if __name__ == "__main__":
    app.run()
