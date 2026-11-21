import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            time TEXT NOT NULL
        )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(f"ID: {row[0]}, Title: {row[1]}, Time: {row[2]}")

def add_video(title, time):
    cursor.execute("INSERT INTO videos (title, time) VALUES (?, ?)", (title, time))
    conn.commit()
    print("Video added successfully.")

def update_video(video_id, title, time):
    cursor.execute("UPDATE videos SET title = ?, time = ? WHERE id = ?", (title, time, video_id))
    conn.commit()
    print("Video updated successfully.")

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()
    print("Video deleted successfully.")


def main():
    while True:
        print("\nYouTube Video Manager with DB")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            title = input("Enter video title: ")
            time = input("Enter video time: ")
            add_video(title, time)
        elif choice == "3":
            video_id = input("Enter the ID of the video to update: ")
            title = input("Enter new video title: ")
            time = input("Enter new video time: ")
            update_video(video_id, title, time)
        elif choice == "4":
            video_id = input("Enter the ID of the video to delete: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()