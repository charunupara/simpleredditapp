import praw
import json




def main():
	#Change the text of each argument to reddit's api information
	reddit = praw.Reddit(client_id='CLIENT_ID',
						 client_secret='CLIENT_SECRET',
						 password='REDDIT PASSWORD',
						 user_agent='USER_AGENT',
						 username='REDDIT_USERNAME'
							)


	posts = int(input("How many posts: "))
	curSubreddit = reddit.subreddit("all")
	hot = curSubreddit.hot(limit=posts)
	
	#an array to store submissions information
	subs = []

	for submission in hot:
		subs.append(f"{submission.subreddit}")
	topSubs = analyzeReddit(subs)
	print(topSubs)



'''
Procedure:
	analyzeReddit
Parameters:
	arr, an array
Produces:
	topSubs, a dictionary
Purpose:
	to find out how many posts are in each subreddit on r/all


'''
def analyzeReddit(arr):
	topSubs = {}
	for i in range(len(arr)):
		if arr[i] in topSubs:
			topSubs[f"{arr[i]}"] += 1
		else:
			topSubs[f"{arr[i]}"] = 1
	return topSubs


if __name__ == '__main__':
	main()