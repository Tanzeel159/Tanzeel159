import requests
import sys

# Your Readwise API key
api_key = sys.argv[1]

# Define the API endpoint for fetching highlights
endpoint = "https://readwise.io/api/v2/highlights/"

# Parameters to fetch the latest 5 articles
params = {
    "limit": 5,
    "book_type": "article",
}

# Set the Authorization header with your API key
headers = {
    "Authorization": f"Token {api_key}",
}

# Make the API request
response = requests.get(endpoint, params=params, headers=headers)

# Parse the response data
if response.status_code == 200:
    data = response.json()
    articles = data["results"]

    # Format the articles in markdown
    markdown_content = "### Latest Articles from Readwise\n\n"
    for article in articles:
        title = article["title"]
        url = article["url"]
        markdown_content += f"- [{title}]({url})\n"

    # Write the markdown content to a file
    with open("latest_articles.md", "w", encoding="utf-8") as file:
        file.write(markdown_content)

else:
    print("Error fetching data from Readwise")
