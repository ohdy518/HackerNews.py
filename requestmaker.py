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
        return []

def item(item_id):
    """
    Fetches the item details from Hacker News using the provided item ID.

    Args:
        item_id (int): The ID of the item to fetch.

    Returns:
        dict: The JSON data for the item, or an empty dictionary if an error occurs.
    """
    # Base URL for Hacker News items
    base_url = "https://hacker-news.firebaseio.com/v0/item"
    url = f"{base_url}/{item_id}.json"

    try:
        # Make a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        item_data = response.json()

        return item_data

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return {}