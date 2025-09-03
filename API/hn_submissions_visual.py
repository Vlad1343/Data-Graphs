

# import requests
# import json

# # Step 1: Fetch a single Hacker News story
# story_id = 19155826  # Example story ID
# url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
# r = requests.get(url)
# print(f"Status code: {r.status_code}")

# # Step 2: Convert to dictionary
# story_dict = r.json()

# # Step 3: Save dictionary as a JSON file for inspection
# with open('hn_example.json', 'w') as f:
#     json.dump(story_dict, f, indent=4)

# # Step 4: Example of manipulating the dictionary
# print("\nOriginal title:", story_dict['title'])

# # Extract values
# author = story_dict.get('by', 'unknown')
# comments = story_dict.get('descendants', 0)
# url_link = story_dict.get('url', 'no url')

# # Add a new key
# story_dict['hn_link'] = f"https://news.ycombinator.com/item?id={story_dict['id']}"


# # Print manipulated data
# print("Author:", author)
# print("Comments:", comments)
# print("HN Link:", story_dict['hn_link'])










 
import requests
from plotly.graph_objs import Bar
from plotly import offline

# Get top stories (list of IDs)
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')

submission_ids = r.json()

# Fetch details for the first 30 submissions
submission_dicts = []
for submission_id in submission_ids[:30]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    if r.status_code == 200:
        submission_dict = r.json()
        # Only include stories that exist and have a title
        if submission_dict and 'title' in submission_dict:
            submission_dicts.append(submission_dict)

# Sort submissions by number of comments (descendants), descending
submission_dicts.sort(key=lambda x: x.get('descendants', 0), reverse=True)

# Prepare data for visualization
submission_links, comments, labels = [], [], []
for sub in submission_dicts:
    title = sub['title']
    hn_link = f"https://news.ycombinator.com/item?id={sub['id']}"
    submission_link = f"<a href='{hn_link}'>{title}</a>"
    submission_links.append(submission_link)
    
    comments.append(sub.get('descendants', 0))  # Number of comments
    by = sub.get('by', 'unknown')
    label = f"By: {by}"
    labels.append(label)

# Make visualization
data = [{
    'type': 'bar',
    'x': submission_links,
    'y': comments,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60,100,150)',
        'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': 'Top Hacker News Articles by Comment Count',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Article',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Number of Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='API/hn_submissions.html')




