import requests

def top():
    URL = "https://hacker-news.firebaseio.com/v0/topstories.json"

    try:
        # Make a GET request to the URL
        response = requests.get(URL)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        top_stories = response.json()

        # Return the list of top stories
        return top_stories

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        raise e

def item(item_id):
    URL = "https://hacker-news.firebaseio.com/v0/item"
    url = f"{URL}/{item_id}.json"

    try:
        # Make a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        item_data = response.json()

        return item_data

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        raise e

def comment(comment_id):
    return item(comment_id)