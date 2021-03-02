import praw
import pandas as pd
from psaw import PushshiftAPI

client_id = 'SD1LEcWxcsGNlg'
client_secret = 'EsSJPHjZfpZYWgFXNHwqubtPEQmehg'
password = 'Piotrek99'
username = 'Bitter-Word'
user_agent = 'Titles Scraper by Bitter-Word'
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret,
                     password=password, user_agent=user_agent,
                     username=username)
api = PushshiftAPI(reddit)

if __name__ == '__main__':
    politics_titles = []
    posts = list(api.search_submissions(subreddit='movies', limit=10000))

    for id in posts:
        politics_titles.append(reddit.submission(id=id).title)

    titles = pd.DataFrame(politics_titles, columns=['Title'])
    titles['Category'] = 'movies'
    print(titles.head())
    titles.to_csv('movies_titles.csv')
