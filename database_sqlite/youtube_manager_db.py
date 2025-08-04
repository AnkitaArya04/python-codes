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
def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit app")

if __name__ == "__main__":
    main()