#main program
import requests
import json
from cred import githubtoken


#variables for the program
username = input("username for github account: ")
repo_name = input("name of the repository that is being created: ")
description = input("What is the description for the repo? ")

headers = {'Accept': 'application/vnd.github.v3+json'}

githuburl = ("https://api.github.com/user/repos")

payload = {'name': repo_name, 'description': description, 'auto_init': 'true'}

pushgitrepo = requests.post(githuburl, auth=(username, githubtoken), headers=headers, data=json.dumps(payload))

if pushgitrepo.status_code == 201:
    print("Repository successfully created")
else:
    print("Not so much try again")