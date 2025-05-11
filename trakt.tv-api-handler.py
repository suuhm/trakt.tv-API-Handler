import requests
from prettytable import PrettyTable

# Trakt.tv API-Config
#CLIENT_ID = 'YOUR_CLIENT_ID'
#CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
#API_ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'

# === Trakt API Konfiguration ===
BASE_URL = 'https://api.trakt.tv/'

HEADERS = {
    "Authorization": "Bearer API_ACCESS_TOKEN",
    "trakt-api-version": "2",
    "trakt-api-key": "YOUR_CLIENT_SECRET"
}

def print_ascii_logo():
    logo = r"""
'########'########::::'###:::'##:::'##'########::::'########'##::::'##:::::::::::'###:::'########:'####::::::::'##::::'##:::'###:::'##::: ##'########:'##::::::'########'########::
... ##..::##.... ##::'## ##:::##::'##:... ##..:::::... ##..::##:::: ##::::::::::'## ##:::##.... ##. ##::::::::::##:::: ##::'## ##:::###:: ##:##.... ##:##:::::::##.....::##.... ##:
::: ##::::##:::: ##:'##:. ##::##:'##::::: ##:::::::::: ##::::##:::: ##:::::::::'##:. ##::##:::: ##: ##::::::::::##:::: ##:'##:. ##::####: ##:##:::: ##:##:::::::##:::::::##:::: ##:
::: ##::::########:'##:::. ##:#####:::::: ##:::::::::: ##::::##:::: ##'#######'##:::. ##:########:: ##:'#######:#########'##:::. ##:## ## ##:##:::: ##:##:::::::######:::########::
::: ##::::##.. ##:::#########:##. ##::::: ##:::::::::: ##:::. ##:: ##:........:#########:##.....::: ##:........:##.... ##:#########:##. ####:##:::: ##:##:::::::##...::::##.. ##:::
::: ##::::##::. ##::##.... ##:##:. ##:::: ##:::'###::: ##::::. ## ##:::::::::::##.... ##:##:::::::: ##::::::::::##:::: ##:##.... ##:##:. ###:##:::: ##:##:::::::##:::::::##::. ##::
::: ##::::##:::. ##:##:::: ##:##::. ##::: ##::::###::: ##:::::. ###::::::::::::##:::: ##:##:::::::'####:::::::::##:::: ##:##:::: ##:##::. ##:########::########:########:##:::. ##:
:::..::::..:::::..:..:::::..:..::::..::::..::::...::::..:::::::...::::::::::::..:::::..:..::::::::....:::::::::..:::::..:..:::::..:..::::..:........::........:........:..:::::..::
"""
    return logo



MOVIE_ENDPOINTS = {
    "1": ("Trending Movies", "movies/trending"),
    "2": ("Popular Movies", "movies/popular"),
    "3": ("Most Played", "movies/played"),
    "4": ("Most Watched", "movies/watched"),
    "5": ("Most Collected", "movies/collected"),
    "6": ("Recommended", "movies/recommended"),
    "7": ("Box Office", "movies/boxoffice"),
}

SHOW_ENDPOINTS = {
    "1": ("Trending Shows", "shows/trending"),
    "2": ("Popular Shows", "shows/popular"),
    "3": ("Most Played", "shows/played"),
    "4": ("Most Watched", "shows/watched"),
    "5": ("Most Collected", "shows/collected"),
    "6": ("Recommended", "shows/recommended"),
    "7": ("Anticipated", "shows/anticipated"),
}

SYNC_ENDPOINTS = {
    "1": ("Last Activities", "sync/last_activities", "raw"),
    "2": ("Playback History", "sync/playback", "raw"),
    "3": ("Collection", "sync/collection", "media"),
    "4": ("Watched", "sync/watched", "media"),
    "5": ("History", "sync/history", "media"),
    "6": ("Ratings", "sync/ratings", "rating"),
    "7": ("Watchlist", "sync/watchlist", "media"),
    "8": ("Recommendations", "sync/recommendations", "media"),
}

USER_ENDPOINTS = {
    "1": ("Collection", "collection", "media"),
    "2": ("Watched", "watched", "media"),
    "3": ("History", "history", "media"),
    "4": ("Ratings", "ratings", "rating"),
    "5": ("Watchlist", "watchlist", "media"),
    "6": ("Comments", "comments", "comment"),
    "7": ("Lists", "lists", "list"),
    "8": ("Followers", "followers", "follow"),
    "9": ("Following", "following", "follow"),
}


# === Core Functions ===

def fetch_data(endpoint):
    try:
        response = requests.get(BASE_URL + endpoint, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error fetching data: {e}")
        return None


def display_media_table(data, title):
    if not data:
        print(f"No data available for {title}")
        return

    table = PrettyTable()
    table.field_names = ["Title", "Year", "Rating", "Genres"]

    for item in data:
        item_data = item.get("movie") or item.get("show") or item.get("episode") or item
        title_ = item_data.get("title", "Unknown")
        year = item_data.get("year", "-")
        rating = item_data.get("rating", "N/A")
        genres = ', '.join(item_data.get("genres", [])) if item_data.get("genres") else "N/A"
        table.add_row([title_, year, rating, genres])

    print(f"\n📊 {title}")
    print(table)


def display_comment_table(data, title):
    if not data:
        print(f"No comments found for {title}")
        return

    table = PrettyTable()
    table.field_names = ["Type", "Title", "Year", "Comment", "Likes", "Spoiler"]

    for item in data[:10]:
        content_type = item.get("type", "N/A")
        comment = item.get("comment", {}).get("comment", "")
        likes = item.get("comment", {}).get("likes", 0)
        spoiler = "Yes" if item.get("comment", {}).get("spoiler") else "No"
        media = item.get("show") or item.get("episode") or item.get("movie") or {}
        title_ = media.get("title", "Unknown")
        year = media.get("year", "-")

        table.add_row([
            content_type.title(),
            title_,
            year,
            comment[:60] + ("..." if len(comment) > 60 else ""),
            likes,
            spoiler
        ])

    print(f"\n💬 {title}")
    print(table)


def display_rating_table(data, title):
    if not data:
        print(f"No ratings available for {title}")
        return

    table = PrettyTable()
    table.field_names = ["Type", "Title", "Year", "Rating"]

    for item in data:
        media_type = "Movie" if "movie" in item else "Show" if "show" in item else "Episode"
        media = item.get("movie") or item.get("show") or item.get("episode") or {}
        title_ = media.get("title", "Unknown")
        year = media.get("year", "-")
        rating = item.get("rating", "N/A")

        table.add_row([media_type, title_, year, rating])

    print(f"\n⭐ {title}")
    print(table)


def display_list_table(data, title):
    if not data:
        print(f"No lists found for {title}")
        return

    table = PrettyTable()
    table.field_names = ["Name", "Description", "Privacy", "Item Count"]

    for item in data:
        name = item.get("name", "Unknown")
        desc = item.get("description", "")
        privacy = item.get("privacy", "N/A")
        count = item.get("item_count", 0)
        table.add_row([name, desc[:40] + ("..." if len(desc) > 40 else ""), privacy, count])

    print(f"\n📚 {title}")
    print(table)


def display_follow_table(data, title):
    if not data:
        print(f"No users found for {title}")
        return

    table = PrettyTable()
    table.field_names = ["Username", "Name", "VIP", "Private"]

    for item in data:
        user = item.get("user", item)
        username = user.get("username", "N/A")
        name = user.get("name", "")
        vip = "Yes" if user.get("vip") else "No"
        private = "Yes" if user.get("private") else "No"
        table.add_row([username, name, vip, private])

    print(f"\n👥 {title}")
    print(table)


def display_raw_data(data, title):
    print(f"\n📂 {title}")
    if not data:
        print("No data.")
        return
    if isinstance(data, dict):
        for k, v in data.items():
            print(f"- {k}: {v}")
    elif isinstance(data, list):
        for i, item in enumerate(data[:10], 1):
            print(f"\n🔸 Entry {i}:")
            if isinstance(item, dict):
                for key, value in item.items():
                    print(f"  {key}: {value}")
            else:
                print(item)


def select_from_menu(menu, title, default_type):
    while True:
        print(f"\n📚 {title}")
        for k, (label, *_rest) in menu.items():
            print(f"{k}. {label}")
        print("A. Show all")
        print("0. Back")

        choice = input("Choose: ").strip().lower()
        if choice == "0":
            break
        elif choice == "a":
            for _, (label, endpoint, *optional_type) in menu.items():
                dtype = optional_type[0] if optional_type else default_type
                data = fetch_data(endpoint)
                display_by_type(data, label, dtype)
        elif choice in menu:
            label, endpoint, *optional_type = menu[choice]
            dtype = optional_type[0] if optional_type else default_type
            data = fetch_data(endpoint)
            display_by_type(data, label, dtype)
        else:
            print("Invalid input.")


def select_user_menu():
    username = input("\n👤 Enter Trakt.tv username: ").strip()
    if not username:
        print("❌ No username entered.")
        return

    while True:
        print(f"\n👤 User: {username}")
        for k, (label, _, _) in USER_ENDPOINTS.items():
            print(f"{k}. {label}")
        print("A. Show all")
        print("0. Back")

        choice = input("Choose: ").strip().lower()
        if choice == "0":
            break
        elif choice == "a":
            for _, (label, endpoint, dtype) in USER_ENDPOINTS.items():
                data = fetch_data(f"users/{username}/{endpoint}")
                display_by_type(data, label, dtype)
        elif choice in USER_ENDPOINTS:
            label, endpoint, dtype = USER_ENDPOINTS[choice]
            data = fetch_data(f"users/{username}/{endpoint}")
            display_by_type(data, label, dtype)
        else:
            print("Invalid input.")


def display_by_type(data, title, dtype):
    if dtype == "media":
        display_media_table(data, title)
    elif dtype == "comment":
        display_comment_table(data, title)
    elif dtype == "rating":
        display_rating_table(data, title)
    elif dtype == "list":
        display_list_table(data, title)
    elif dtype == "follow":
        display_follow_table(data, title)
    else:
        display_raw_data(data, title)


def main():
    while True:
        print(print_ascii_logo()+"\n")
        print("1. Movies")
        print("2. Shows")
        print("3. Sync")
        print("4. User")
        print("0. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            select_from_menu(MOVIE_ENDPOINTS, "Movies", "media")
        elif choice == "2":
            select_from_menu(SHOW_ENDPOINTS, "Shows", "media")
        elif choice == "3":
            select_from_menu(SYNC_ENDPOINTS, "Sync", "media")
        elif choice == "4":
            select_user_menu()
        elif choice == "0":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid input.")


if __name__ == "__main__":
    main()
