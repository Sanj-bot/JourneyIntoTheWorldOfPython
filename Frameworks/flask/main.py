from random import randint
import sqlite3
from flask import Flask, jsonify
import time

#defining a flask app instance
app = Flask(__name__)

# connecting database to sql lite
#conn for overall connection
conn = sqlite3.connect('v_c.db')
#cursor executes specific sql statements.
c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS vehicle_counts (timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, auto INTEGER, car INTEGER, bus INTEGER, truck INTEGER, motorcycle INTEGER )''')

def generate_counts():
  return {
      "auto": randint(0, 10),
      "car": randint(1, 10),
      "bus": randint(1, 10),
      "truck": randint(1, 10),
      "motorcycle": randint(1, 10),
      
  }
while True:
  counts = generate_counts()
  c.execute("INSERT INTO vehicle_counts (auto, car, bus, truck, motorcycle) VALUES (?, ?, ?, ?, ?)", (counts["auto"], counts["car"], counts["bus"], counts["truck"], counts["motorcycle"]))
  conn.commit()
  c.execute("SELECT * FROM vehicle_counts ORDER BY timestamp DESC LIMIT 10")
  data = c.fetchone()
  print(f"latest: {data}")
  
if __name__ == '__main__':
  
  app.run(debug=True)