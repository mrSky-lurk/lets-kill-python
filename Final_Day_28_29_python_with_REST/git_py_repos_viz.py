import requests
import plotly.express as px

base_uri = "https://api.github.com/search/repositories"
query = "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
api_response = requests.get(base_uri + query, headers=headers)
all_repos = api_response.json()
print("# ========================================= Overall Response ==============================================")
print(f"Status code: {api_response.status_code}")
print(f"Complete results: {not all_repos['incomplete_results']}")
print("# ========================================= Repo info ==============================================")
repo_dicts = all_repos['items']
repo_name, repo_stars, hover_texts, repo_urls = [], [], [], []
for repo_dict in repo_dicts:
    repo_name.append(repo_dict['name'])
    repo_stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    desc = repo_dict['description']
    hover_text = f"Owner: {owner}<br />Description: {desc}"
    hover_texts.append(hover_text)
    repo_url = f"<span><a href='{repo_dict['html_url']}'>{repo_dict['name']}</a></span>"
    repo_urls.append(repo_url)
title = "Most Loved repositories in GitHub"
labels = {'x': "Repositories", 'y': 'Stars'}
fig = px.bar(x=repo_name, y=repo_stars, title=title, labels=labels, hover_name=hover_texts, text=repo_urls)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update_traces(textposition='auto', marker_color='grey', marker_opacity=0.4)
fig.show()
