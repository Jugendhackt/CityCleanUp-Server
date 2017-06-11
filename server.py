from flask import Flask
from flask import request
import sqlite3
import os
from flask import jsonify
import json

if os.path.exists("citycleanup.db")==False:
    conn = sqlite3.connect('citycleanup.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE Verschmutzung
    (
    id INTEGER NOT NULL,
    LAENGE FLOAT,
    BREITE FLOAT,
    VERSCHMUTZUNGSGRAD INTEGER,
    BESCHREIBUNG TEXT,
    PRIMARY KEY (ID)
    )''')
else:
    conn = sqlite3.connect('citycleanup.db')
    c = conn.cursor()


c.execute("SELECT * FROM Verschmutzung")
print(c.fetchall())

app = Flask(__name__)

@app.route('/api/submit', methods=['POST'])
#TODO: Begrenzungen für Anfragen
def submit():
    c.execute('insert into Verschmutzung (LAENGE, BREITE, VERSCHMUTZUNGSGRAD, BESCHREIBUNG) values(?, ?, ?, ?)', (request.form['laenge'], request.form['breite'], request.form['verschmutzungsgrad'], request.form['beschreibung']))
    conn.commit()
    print(request.form)
    return 'success', 200

@app.route('/api/get_markers', methods=['GET'])
def get_markers():
#TODO: Nur in der Nähe anzeigen
    c.execute("SELECT * FROM Verschmutzung;")
    #Geklaut von Stackoverflow
    rows = [x for x in c]
    cols = [x[0] for x in c.description]
    markers = []
    marker = {}
    for row in rows:
        marker = {}
        for prop, val in zip(cols, row):
            marker[prop] = val
        markers.append(marker)

    # Create a string representation of your array of songs.
    print(markers)
    return json.dumps(markers), 200


if __name__ == "__main__":
    app.run()
