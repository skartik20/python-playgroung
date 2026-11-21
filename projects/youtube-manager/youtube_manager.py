

import json


def list_all_videos(videos):
    print('\n')
    print('*' * 70)
    for index, video in enumerate(videos, start=1):
        # enumerate is used to get the index of the video in the list, starting from 1.
        # otherwise, we would have to manually keep track of the index.
        # this way both user and developer can easily see the index of the video in the list.
        print(f"{index}. {video['title']} - {video['time']}")

    print('\n')
    print('*' * 70)

def add_video(videos):
    title = input("Enter video title: ")
    time = input("Enter video time: ")
    videos.append({"title": title, "time": time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the number of the video to update: "))

    if 1 <= index <= len(videos):
        title = input("Enter new video title: ")
        time = input("Enter new video time: ")
        videos[index - 1] = {"title": title, "time": time}
        save_data_helper(videos)
    else:
        print("Invalid video number.")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the number of the video to delete: "))
    
    if 1 <= index <= len(videos):
        videos.pop(index - 1)
        save_data_helper(videos)
    else:
        print("Invalid video number.")

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            # print(type (test))
            return test
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

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
        # print(videos)

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
