import os, re
import praw
from requests import Session
from rich import print
from yahoo_fin import stock_info as si
from dotenv import load_dotenv, find_dotenv



load_dotenv(find_dotenv())
start_price = si.get_live_price("gme")
showfluff = os.getenv('SHOW_FLUFF')
session = Session()
# session.verify = "/path/to/certfile.pem"
reddit = praw.Reddit(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('SECRET'),
    username=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    user_agent="simple stream app by u/devdevgoat",
)

fluffstuff = ['Shitpost', 'Meme', 'Fluff', 'Art & Writing', 'Opinion']
important = ['Discussion','DD','Possible DD','Education']

def teststring():
    tests = ['abcgme','gamestops','gamestop\'s',' this is a gme.', 'this is a gamestop, damnit',' gme ',' gamestop ',' GME ',' Gamestop ']
    for test in tests:
        if string_found('gme',test):
            print(f'Found gme in: {test}')
        if string_found('gamestop',test):
            print(f'Found gamestop in: {test}')

def string_found(string1, string2):
   if re.search(r"\b" + re.escape(string1) + r"\b", string2, re.IGNORECASE):
      return True
   return False

teststring()

for comment in reddit.subreddit('all').stream.comments(): #skip_existing=True
    if comment.subreddit.display_name not in ["GMEJungle","Superstonk","gme_meltdown","GME","GMEdk","DDintoGME",]:
        if string_found('gme',comment.body):
            print(f'[italic rgb(96, 96, 96)]https://reddit.com{comment.permalink} [/italic rgb(96, 96, 96)]')
            print(comment.body.replace('gme',f'[bold red]GME[/bold red]'))
        elif string_found('gamestop',comment.body):
            print(f'[italic rgb(96, 96, 96)]https://reddit.com{comment.permalink} [/italic rgb(96, 96, 96)]')
            print(comment.body.replace('gme',f'[bold red]gamestop[/bold red]'))