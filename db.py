import sqlite3




def CreateDatabase():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE data(
            id INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
            assignment TEXT NOT NULL
        )
    """)
    conn.close()


def PostAssignmet(data):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute(""" 
        INSERT INTO data(id,assignment)
        VALUES(null, ?)""", (data,))
    conn.commit()
    conn.close()


def Assignment(id):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, assignment  FROM data
        WHERE id = ?;
    """, (id,))
    for row in cursor:
        return row
    conn.close()

def GetAssignments():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM data;
    """)
    data = []
    for line in cursor.fetchall():
        data.append(line)
    conn.close()
    return data



def PutAssignment(id, assignment):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE data
        SET assignment = ? 
        WHERE id = ?
    """,(assignment,id,))
    print(Assignment(id))
    conn.commit()
    conn.close()

def DeleteAssignment(id):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM data 
        WHERE id = ?
    """, (id,))
    conn.commit()
    conn.close()


if __name__=="__main__":
    CreateDatabase()