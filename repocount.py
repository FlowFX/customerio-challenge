"""Simple API/scripting challenge for the Customer.io job application.

See: https://boards.greenhouse.io/customerio/jobs/918094

Using the Github API and a scripting language of your choice answer
the following questions about Customer.io's public repositories:

1. How many total open issues are there across all repositories?
2. Sort the repositories by date updated in descending order.
3. Which repository has the most watchers?
"""
import requests

org = 'customerio'
repos_url = f'https://api.github.com/orgs/{org}/repos'

req = requests.get(repos_url)

# get a Python dict 
repos = req.json()

# Sum up total open issues across all repos.
total_open_issues = sum([repo['open_issues_count'] for repo in repos])

print(f'Total open issues: {total_open_issues}')
