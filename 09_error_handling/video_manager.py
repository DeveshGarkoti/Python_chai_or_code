import json 

def load_data():
  try:
    with open('video.txt', 'r') as file:
      return json.load(file)
  except FileNotFoundError:
    return []


def list_all_videos(videos):
  print("\n")
  print("*" * 70)
  for index, video in enumerate(videos, start=1):
    print(f"{index}. {video['title']} by {video['creator']}")
  print("\n")
  print("*" * 70)


def save_videos_helper(videos):
  with open('video.txt', 'w') as file:
    json.dump(videos,file)


def add_video(videos):
  title = input("Enter the title of the video: ")
  creator = input("Enter the creator of the video: ")
  videos.append({'title':title,'creator':creator})
  save_videos_helper(videos)


def update_video(videos):
  list_all_videos(videos)
  index = int(input("Enter the number of the video you want to update: "))
  if 1 <= index <= len(videos):
    title = input("Enter the new title of the video: ")
    creator = input("Enter the new creator of the video: ")
    videos[index-1] = {'title':title,'creator':creator}
    save_videos_helper(videos)
    print("\n Video Updated")
  else:
    print("\nInvalid index: Enter a valid number")


def delete_video(videos):
  list_all_videos(videos)
  index = int(input("Enter the number of the video you want to update: "))
  if 1 <= index <= len(videos):
    del videos[index-1]
    save_videos_helper(videos)
    print("\n Video Deleted")
  else:
    print("\nInvalid index: Enter a valid number")


def main():
  videos = load_data()
  while True:

    print("\n Video Manager")
    print("1. List all videos")
    print("2. Add a video")
    print("3. Update a video")
    print("4. Delete a video")
    print("5. Exit \n")

    choice = int(input("Enter your Choice: "))

    match choice:
      case 1:
        list_all_videos(videos)
      case 2:
        add_video(videos)
      case 3:
        update_video(videos)
      case 4:
        delete_video(videos)
      case 5:
        break
      case _:
        print("Invalid choice")

if __name__ == "__main__":
  main()