import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read configuration from environment variables
owner = os.getenv('GITHUB_OWNER')
repo = os.getenv('GITHUB_REPO')
token = os.getenv('GITHUB_TOKEN')

# GitHub API endpoint for code scanning alerts
url = f'https://api.github.com/repos/{owner}/{repo}/code-scanning/alerts'

# Headers for authentication
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

def get_code_scanning_alerts(url, headers):
    alerts = []
    while url:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        alerts.extend(response.json())
        # Check if there is a next page
        url = response.links.get('next', {}).get('url')
    return alerts

# Fetch the alerts
alerts = get_code_scanning_alerts(url, headers)

# Print the alerts
#for alert in alerts:
#    print(f"Alert ID: {alert['number']}, State: {alert['state']}, Rule: {alert['rule']['id']}, Ref: {alert['most_recent_instance']['ref']}")

## filter the alerts where state is fixed and Ref is refs/heads/master
closed_alerts = [alert for alert in alerts if alert['state'] == 'fixed' and alert['most_recent_instance']['ref'] == 'refs/heads/master']

## print closed alerts
for alert in closed_alerts:
    print(f"Alert ID: {alert['number']}, State: {alert['state']}, Rule: {alert['rule']['id']}, Ref: {alert['most_recent_instance']['ref']}")