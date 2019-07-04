import requests
from url_settings import Settings


url_setting = Settings()
url = url_setting.url_github_python
r = requests.get(url)
print("Status code:",r.status_code)

reponse_dict = r.json()
print("Total repositories:",reponse_dict['total_count'])

repo_dicts = reponse_dict['items']
print("Number of items:",len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value':repo_dict['stargazers_count'],
        'label':repo_dict['description']
    }
    plot_dicts.append(plot_dict)
print(names)
print("\n",plot_dicts)

