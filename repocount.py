"""Simple API/scripting challenge for the Customer.io job application.

See: https://boards.greenhouse.io/customerio/jobs/918094

Using the Github API and a scripting language of your choice answer
the following questions about Customer.io's public repositories:

1. How many total open issues are there across all repositories?
2. Sort the repositories by date updated in descending order.
3. Which repository has the most watchers?
"""
import requests
from operator import itemgetter

org = 'customerio'
repos_url = f'https://api.github.com/orgs/{org}/repos'

req = requests.get(repos_url)

# get a Python dict 
repos_dict = req.json()

# Sum up total open issues across all repos.
total_open_issues = sum([repo['open_issues_count'] for repo in repos_dict])

print(f'Total open issues: {total_open_issues}')

repo_tuples = [(x['name'], x['updated_at'], x['open_issues_count'], x['watchers_count']) for x in repos_dict]

# https://docs.python.org/3/howto/sorting.html
# sort by updated_at
sorted_repos = sorted(repo_tuples, key=itemgetter(1), reverse=True)

for r in sorted_repos:
    print(f'{r[0]}, last updated at: {r[1]}')
