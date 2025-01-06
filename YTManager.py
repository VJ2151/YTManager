import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()
cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL    
            )
''')


def list_all_videos():
    print("*"*70)   
    cursor.execute('SELECT * FROM videos')
    for rows in cursor.fetchall():
        if rows == "":
            print("k")
        else:
            print(rows)
    print("*"*70)   


def add_video(video_name, video_duration):
    print("*"*70)   
    cursor.execute('INSERT INTO videos (name, time) VALUES (?,?)', (video_name, video_duration))
    conn.commit()
    list_all_videos()
    print("*"*70)   


def update_video(new_name, new_duration, video_id):
    print("*"*70)   
    cursor.execute('UPDATE videos SET name = ?, time = ? WHERE id=?', (new_name,new_duration, video_id) )
    conn.commit()
    list_all_videos()
    print("*"*70)   


def delete_video(video_id): 
    print("*"*70)   
    cursor.execute('DELETE FROM videos WHERE id = ?', (video_id, ))
    conn.commit()
    list_all_videos()
    print("*"*70)   
    


def main():
    while True:
        print("\n Welcome to YTManager")
        print("\n 1. List all Videos:")
        print("\n 2. Add Video:")
        print("\n 3. Update Video:")
        print("\n 4. Delete Video:")
        print("\n 5. Exit")
        choice = input("\n Enter Your Choice: ")

        match choice:
            case "1":
                list_all_videos()
            case "2":
                video_name = input("\nEnter name of the Video: ")
                video_duration = input("\nEnter Time Duration of Video: ")
                add_video(video_name, video_duration)
                print(f"Video of {video_name} Added Successfully")
            case "3":
                video_id = input("\nEnter ID of your Video: ")
                video_name = input("\nEnter name of the Video: ")
                video_duration = input("\nEnter Time Duration of Video: ")
                update_video(video_name, video_duration, video_id)
                print(f"Video of {video_name} Updated Successfully")
            case "4":
                delete_video(video_id)
                print(f"Video of {video_id} Updated Successfully")
            case "5":
                break
            case _:
                print("\nInvalid Choice")
    conn.close()


if __name__ == "__main__":
    main()
