from operator import itemgetter
import requests
import plotly.express as px

# make an API call and check the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status Code: {r.status_code}")

# process information about each submission
submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:30]:
    # make a new API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # build a dictionary for each article
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict.get('descendants', 0)

    }

    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion Link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

# build empty lists for titles, comments, and links
titles = [item['title'] for item in submission_dicts]
comments = [item['comments'] for item in submission_dicts]
links = [item['hn_link'] for item in submission_dicts]

# create HTML clickable titles
linked_titles = []
for title, link in zip(titles, links):
    linked_title = f"<a href='{link}'>{title}</a>"
    linked_titles.append(linked_title)

# make visualization
title = "Most Active Discussions on Hacker News"
labels = {'x': 'Article', 'y': 'Comments'}

fig = px.bar(x=linked_titles, y=comments, title=title, labels=labels)
fig.update_layout(xaxis={'tickangle': -45})

fig.show()