from facebook_scraper import get_group_info
from facebook_scraper import get_posts
import json

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

infos = get_group_info(106503496676216)
posts = get_posts(
    group=106503496676216,
    page_limit=3,
    extra_info=True,
    cookies="facebook.com_cookies.txt",
    options={"comments": True, "reactors": True},
)

i = 0
post_list = []
for post in posts:
    post = {item: post[item] for item in keep_items if item in post.keys()}
    post_list.append(post)
    if i == 3:
        break

with open("3_posts", "w") as fout:
    json.dump(post_list, fout)
