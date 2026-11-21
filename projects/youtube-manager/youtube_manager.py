

import json


def list_all_videos(videos):
    pass  # Implement the logic to list all videos

def add_video(videos):
    pass  # Implement the logic to add a new video

def update_video(videos):
    pass  # Implement the logic to update video details

def delete_video(videos):
    pass  # Implement the logic to delete a video

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def main():
    videos = load_data()  # This would load the existing video data into the 'videos' variable

    while True:
        print("\n YouTube Manager")
        print("1. List all Youtube Videos")
        print("2. Add a new video")
        print("3. Update a video details")
        print("4. Delete a video")
        print("5. Exit the app")
        choice = input("Enter your choice (1-5): ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("Exiting the app...")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
