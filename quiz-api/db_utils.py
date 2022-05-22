import sqlite3

def callDb_oneResult(request):
    """
    Calls db with request in param
    """
    try:
        db_connection = sqlite3.connect("..\quiz-app-db.db")
        db_connection.isolation_level = None
        cur = db_connection.cursor()
        cur.execute("begin")
        res = cur.execute(request)
        res = res.fetchone()
        cur.execute("commit")
        return res
    except sqlite3.OperationalError:
        cur.execute("rollback")
        raise sqlite3.OperationalError("Error while inserting data to db")

def callDb_multipleResults(request):
    """
    Calls db with request in param
    """
    try:
        db_connection = sqlite3.connect("..\quiz-app-db.db")
        db_connection.isolation_level = None
        cur = db_connection.cursor()
        cur.execute("begin")
        res = cur.execute(request)
        res = res.fetchall()
        cur.execute("commit")
        return res
    except sqlite3.OperationalError:
        cur.execute("rollback")
        raise sqlite3.OperationalError("Error while inserting data to db")

