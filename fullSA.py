import sqlite3


conn = sqlite3.connect('knowledgebase.db')
c = conn.cursor()


def createDB():
    c.execute("CREATE TABLE wordVals (word TEXT, value REAL)")
