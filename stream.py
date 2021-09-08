import os
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

for sub in reddit.subreddit('superstonk').stream.submissions(): #skip_existing=True
    color = 'yellow'
    printt = True
    for flair in fluffstuff:
        if flair in sub.link_flair_text:
            printt = showfluff
            color = 'brown'
    for flair in important:
        if flair in sub.link_flair_text:
            printt = True
            color = 'green'
    if (printt):
        curr_price = si.get_live_price("gme")
        change = start_price-curr_price
        pcolor = 'green'
        emoji = ':up_arrow:'
        if change < 0:
            pcolor = 'red'
            emoji = ':down_arrow:'
        print(f'[bold {pcolor}]{"${:,.2f}".format(change)}{emoji}[/bold {pcolor}][{sub.link_flair_text}][bold {color}]\n\t{sub.title}[/bold {color}]')
        print(f'[italic rgb(96, 96, 96)]\t\thttps://reddit.com{sub.permalink} [/italic rgb(96, 96, 96)]')