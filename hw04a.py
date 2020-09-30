import requests
import json

def Repo(user):
    try:
        url = "https://api.github.com/users/{}/repos".format(user)
    except:
        print("User Id should be a string")
        exit()

    res = requests.get(url)
    repos = json.loads(res.text)

    result = []
    for repo in repos:
        commits = requests.get("https://api.github.com/repos/{}/{}/commits".format(user,repo['name']))
        commits_json = json.loads(commits.text)
        c = 0
        for line in commits_json:
            c += 1
        result.append([repo['name'], c])
        print('Repo: {} Number of commits: {}'.format(repo['name'],c))
    return result

fhand = input("Plz enter your GithubId: ")
Repo(fhand)
