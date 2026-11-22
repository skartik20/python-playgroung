from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://<db_username>:<db_password>@cluster0.vampmsk.mongodb.net/")

#Should not be included in code, but for the sake of this example, we will include it here. In a real-world scenario, you should use environment variables or a configuration file to store sensitive information like database credentials.

db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Title: {video['title']}, Time: {video['time']}")

def add_video(title, time):
    video_collection.insert_one({"title": title, "time": time})

def update_video(video_id, title, time):
    video_collection.update_one({"_id": ObjectId(video_id)}, {"$set": {"title": title, "time": time}})

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})
    #ObjectId is used to convert the string representation of the ObjectId back to an ObjectId instance, which is required for querying the MongoDB collection.


def main():
    while True:
        print("\nYouTube Video Manager")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_videos()
            case "2":
                title = input("Enter video title: ")
                time = input("Enter video time: ")
                add_video(title, time)
            case "3":
                video_id = input("Enter video ID to update: ")
                title = input("Enter video title: ")
                time = input("Enter video time: ")
                update_video(video_id, title, time)
            case "4":
                video_id = input("Enter video ID to delete: ")
                delete_video(video_id)
            case "5":
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()