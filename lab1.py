def create_youtube_video(title,description):
	video = {
		"title" : title, "description" : description, "likes" : 0, "dislikes" : 0, "username" : ""
		}
def like(video):
	if "likes" in video():
		video["likes"]+=1

