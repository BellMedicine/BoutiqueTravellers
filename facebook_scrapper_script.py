from facebook_scraper import get_group_info
from facebook_scraper import get_posts
import json
import datetime
import time
import random

# BoutiqueTravellers Group ID
group_id = 106503496676216

# Set number of posts wanted. Use -1 to try to get all
n_posts = 1000

# Post items that are interesting to keep
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

# Get group info from Facebook. Currently not used
# TODO #2
infos = get_group_info(group_id)

posts = get_posts(
    group=group_id,
    page_limit=50,
    extra_info=True,
    cookies="facebook.com_cookies.txt",
    options={"comments": True, "reactors": True},
)

i = 1
post_list = []
for post in posts:
    post = {item: post[item] for item in keep_items if item in post.keys()}
    post_list.append(post)
    if i == n_posts:
        break
    if i % 20 == 0:
        print(f"We have {i} posts")
        time.sleep(180 * random.uniform(0.5, 1))
    i += 1

print(f"We got some {len(post_list)} posts")


def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
    else:
        return o


_ = 0

# TODO #3
with open(f"{n_posts}_posts.json", "w") as fout:
    json.dump(post_list, fout, default=myconverter)

print("See you next time!")
