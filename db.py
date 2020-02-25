import sqlite3

table_question = """
    CREATE TABLE Question(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        option1 TEXT,
        option2 TEXT,
        option3 TEXT,
        option4 TEXT,
        option5 TEXT,
        correct_option TEXT,
        description TEXT
    );
"""


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        create_table(conn, table_question)
        print(sqlite3.version)
        return conn
    except sqlite3.Error as e:
        print(e)


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)


def insert_question(conn, fields):
    query = """
        INSERT INTO Question(question, option1, option2, option3, option4, option5, correct_option, description) 
        VALUES(?,?,?,?,?,?,?,?)
    """
    with conn:
        cur = conn.cursor()
        cur.execute(query, fields)
        return cur.lastrowid
