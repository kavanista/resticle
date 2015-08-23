from flask import Flask
from flask.ext.mysql import MySQL
import config

app = Flask(__name__)


mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = config.user
app.config['MYSQL_DATABASE_PASSWORD'] = config.password
app.config['MYSQL_DATABASE_DB'] = config.db
app.config['MYSQL_DATABASE_HOST'] = config.host
mysql.init_app(app)


conn = mysql.connect()
conn = mysql.connect()
cursor = mysql.connect().cursor()

cursor.execute("SELECT * from data")
data = cursor.fetchone()

@app.route('/')
def index():
    return "Hello world"

if __name__ == '__main__':
    app.run(debug=True)
 
