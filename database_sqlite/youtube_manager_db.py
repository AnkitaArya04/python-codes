import sqlite3

conn=sqlite3.connect('youtube_videos.db')

cursor=conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXIST videos(
            id INTEGER PRIMARY KEY,
            name INTEGER NOT NULL,
            time TEXT NOT NULL   
            )
''')
