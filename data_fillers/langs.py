def lang(cursor):
    cursor.execute("INSERT INTO lang (langname) VALUES('rus')")
    cursor.execute("INSERT INTO lang (langname) VALUES('ara')")
    cursor.execute("INSERT INTO lang (langname) VALUES('bel')")
    cursor.execute("INSERT INTO lang (langname) VALUES('spa')")
    cursor.execute("INSERT INTO lang (langname) VALUES('fra')")
    cursor.execute("INSERT INTO lang (langname) VALUES('ger')")