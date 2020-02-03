#! usr/bin/env python3
import praw
from praw.models import MoreComments
import pandas as pd
import datetime as dt
import uuid
import json

reddit = praw.Reddit(client_id='clientid', \
                     client_secret='clientsecret', \
                     user_agent='myredditcrawler', \
                     username='username', \
                     password='redditpassword')

subreddit = reddit.subreddit('army')


relevant_subreddit = subreddit.search("Army Combat Fitness Test")

submission_titles = dict()
first_level_comments = dict()
second_level_comments = dict()
list1 = []
list2 = []
list3 = []


for submission in relevant_subreddit:
    local_dict1 = dict()
    #TODO check if there is a body.
    #print(submission.title)
    local_dict1['id'] = str(uuid.uuid1())
    local_dict1['language'] = 'en'
    local_dict1['text'] = submission.selftext[0:5000]
    if submission.selftext != '':
        list1.append(local_dict1)

    submission.comments.replace_more(limit=None)

    #TODO Because i hit a payload error with azure by list() all of the comments, I am gonna only retain 1st and 2nd level comments.
    for top_level_comment in submission.comments:
        local_dict2 = dict()

        local_dict2['id'] = str(uuid.uuid1())
        local_dict2['language'] = 'en'
        local_dict2['text'] = top_level_comment.body

        list2.append(local_dict2)
        for second_level_comment in top_level_comment.replies:
            local_dict3 = dict()

            local_dict3['id'] = str(uuid.uuid1())
            local_dict3['language'] = 'en'
            local_dict3['text'] = second_level_comment.body
    ''' This is the code for retaining all comments, which causes payload error.
    for comment in submission.comments.list():
        local_dict2 = dict()

        local_dict2['id'] = str(uuid.uuid1())
        local_dict2['language'] = 'en'
        local_dict2['text'] = comment.body

        list2.append(local_dict2)
        #print(comment.body)
    '''
#TODO need to get the comments of the submissions, create a dict of comments.

submission_titles['documents'] = list1
first_level_comments['documents'] = list2
second_level_comments['documents'] = list3

submissions_json = json.dumps(submission_titles)
first_level_comments_json = json.dumps(first_level_comments)
second_level_comments_json = json.dumps(second_level_comments)


with open('submissions.json', 'w') as f:
    json.dump(submissions_json, f)

with open('first_level_comments.json', 'w') as f:
    json.dump(first_level_comments_json, f)

with open('second_level_comments.json', 'w') as f:
    json.dump(second_level_comments_json, f)


