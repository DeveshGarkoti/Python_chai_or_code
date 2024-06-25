from pymongo import MongoClient
from bson import ObjectId

# Not a good idea to include id and password in code files
url = "mongodb+srv://youtubepy:youtubepy@cluster0.rsnk8ld.mongodb.net/"

# Not a good idea tlsAllowInvalidCertificate = True
client = MongoClient(url)

print(client)

db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)


def add_video(name, time):
  video_collection.insert_one({"name":name, "time":time})


def get_all_videos():
  for video in video_collection.find():
    print(f"ID: {video["_id"]} Name: {video["name"]} Time: {video["time"]}")


def update_video(index, new_name, new_time):
  video_collection.update_one({'_id': ObjectId(index)}, {"$set": {"name":new_name, "time":new_time}})


def delete_video(index):
  video_collection.delete_one({"_id": ObjectId(index)})


def main():
  while True:
    print("/n Youtube manager app by MongoDB")
    print("1. Get all videos")
    print("2. Add video")
    print("3. Update video")
    print("4. Delete video")
    print("5. Exit")
    choice = input("Choose an option: ")

    match choice:
      case "1":
        get_all_videos()
      case "2":
        name = input("Enter the video name: ")
        time = input("Enter the video time: ")
        add_video(name, time)
      case "3":
        index = input("Enter the video id to update: ")
        name = input("Enter the video name: ")
        time = input("Enter the video time: ")
        update_video(index, name, time)
      case "4":
        index = input("Enter the video id to update: ")
        delete_video(index)
      case "5":
        break
      case _:
        print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
  main()