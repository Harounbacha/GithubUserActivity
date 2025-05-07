import click
import requests
import json
from datetime import datetime

# GitHub API base URL
GITHUB_API = "https://api.github.com"

# CLI command definition
@click.command()
@click.argument('username')
def fetch_activity(username):
    """Fetch recent GitHub activity for a USERNAME."""
    # Create the API URL
    url = f"{GITHUB_API}/users/{username}/events"

    # Send a GET request to GitHub
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        events = response.json()
        if not events:
            click.echo(f"No recent activity found for {username}")
            return
            
        # Display the last 5 activities
        click.echo(f"\nRecent GitHub activity for {username}:")
        for event in events[:5]:
            # Format the timestamp
            created_at = datetime.strptime(event['created_at'], '%Y-%m-%dT%H:%M:%SZ')
            formatted_date = created_at.strftime('%Y-%m-%d %H:%M:%S')
            
            # Print event details
            click.echo(f"\n🔹 {event['type']} on {formatted_date}")
            click.echo(f"   Repository: {event['repo']['name']}")
    else:
        click.echo(f"Error: Unable to fetch data for {username}")
        click.echo(f"Status code: {response.status_code}")

# Entry point
if __name__ == '__main__':
    fetch_activity()