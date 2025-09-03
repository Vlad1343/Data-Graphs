
import requests

# Make a call through the GitHub API and save the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

# Store the API response in a variable
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)

# Print selected information about each repository
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository URL: {repo_dict['html_url']}")
    print(f"Created at: {repo_dict['created_at']}")
    print(f"Updated at: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
