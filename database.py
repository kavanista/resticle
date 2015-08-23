import MySQLdb
from config import *


def connectDB():
    db = MySQLdb.connect(host,user, password, database)
    return db

def get_all(db=None):
    if not db:
        db = connectDB()
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    query = """ SELECT * FROM data  """
    cursor.execute(query)
    data = cursor.fetchall()
    return data
