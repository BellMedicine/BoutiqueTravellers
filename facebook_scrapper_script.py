from facebook_scraper import get_group_info
from facebook_scraper import get_posts
import json
import datetime

group_id = 106503496676216

keep_items = [
    "post_id",
    "text",
    "time",
    "post_url",
    "username",
    "user_url",
    "likes",
    "comments",
    "shares",
    "user_id",
    "username",
    "comments_full",
    "reactors",
    "reactions",
]

infos = get_group_info(group_id)
posts = get_posts(
    group=group_id,
    page_limit=1,
    extra_info=True,
    cookies="facebook.com_cookies.txt",
    options={"comments": True, "reactors": True},
)

i = 0
post_list = []
for post in posts:
    post = {item: post[item] for item in keep_items if item in post.keys()}
    post_list.append(post)
    if i == 1:
        break
    i += 1

print("We got some Data")

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
    else: 
        return o

_=0
with open("2_posts.json", "w") as fout:
    json.dump(post_list, fout, default = myconverter)
    #json.dump(json.dumps(post_list, default = myconverter), fout)

print("See you next time!")