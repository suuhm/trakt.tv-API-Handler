# 🎬 trakt.tv-API-Handler

A powerful and interactive Python CLI tool to explore the [Trakt.tv API](https://trakt.docs.apiary.io/). View trending movies and shows, explore user activity, collections, watchlists, ratings, and more — all from your terminal.

---

## 🚀 Features

- ✅ Browse trending, popular, and anticipated **movies** and **TV shows**
- ✅ View **sync history**, **watchlist**, **ratings**, and **collections**
- ✅ Explore **user data** (watched, ratings, lists, followers, comments, etc.)
- ✅ PrettyTables for clean terminal display
- ✅ Modular and easily extensible

---

## 📷 Preview

---

![grafik](https://github.com/user-attachments/assets/f8f42ac6-3e4c-4947-8a89-d86391762b3f)

---

## 🛠️ Requirements

- Python 3.7+
- [Trakt.tv API key](https://trakt.tv/oauth/applications) (Client ID only)

Install dependencies:
```bash
pip install requests prettytable
````

---

## 🔧 Setup

1. Clone the repo:

```bash
git clone https://github.com/suuhm/trakt.tv-API-Handler.git
cd trakt.tv-API-Handler
```

2. Open the script and insert your Trakt.tv API key:

```python
HEADERS = {
    'Content-Type': 'application/json',
    'trakt-api-version': '2',
    'trakt-api-key': 'YOUR_CLIENT_ID_HERE'  # ← replace this
}
```

Absolutely! Here's an additional section you can add to your `README.md` file that explains **how to get a Trakt.tv API token (Client ID)** step-by-step:

---

## 🔑 How to Get a Trakt.tv API Client ID

To use the Trakt.tv API, you need a free **Client ID**. Here's how to get one:

### 🧭 Step-by-Step

1. **Create an account (if you don’t have one):**
   Go to [https://trakt.tv/join](https://trakt.tv/join) and sign up.

2. **Log in to your account** at [https://trakt.tv](https://trakt.tv)

3. **Go to the Developer Applications page:**
   Visit 👉 [https://trakt.tv/oauth/applications](https://trakt.tv/oauth/applications)

4. **Click "New Application"**

5. **Fill in the application form:**

   | Field            | Value                                            |
   | ---------------- | ------------------------------------------------ |
   | **Name**         | Trakt.tv API Handler                             |
   | **Redirect URI** | `urn:ietf:wg:oauth:2.0:oob` *(for testing only)* |
   | **Description**  | CLI tool to explore Trakt.tv content             |
   | **Permissions**  | Leave as-is (read-only is fine for public APIs)  |

6. **Click Save Application**

7. After saving, you'll see:

   * **Client ID**
   * **Client Secret**
  
8. Run the python script `python trakt.tv-oauth.py`


### 📝 Update the script

In the Python file, find this line:

```python
"Authorization": "Bearer API_ACCESS_TOKEN",
'trakt-api-key': 'YOUR_CLIENT_ID_HERE'
```

Replace `'YOUR_CLIENT_ID'` and `'API_ACCESS_TOKEN'` with your actual **Client ID** and **API_ACCESS_TOKEN** from the step above.

---

3. Run the tool:

```bash
python trakt_api_explorer.py
```

---

## 🧩 Menu Overview

```
🎬 Trakt.tv API Explorer
1. Movies          → Submenu (Trending, Popular, Recommended, etc.)
2. Shows           → Submenu (Trending, Played, Anticipated, etc.)
3. Sync            → Submenu (Watched, History, Collection, etc.)
4. User            → Enter a username, explore their profile data
0. Exit
```

Each submenu offers an option to fetch individual endpoints or **"A. Show all"** to fetch all related endpoints at once.

---

## 🧪 Example

```bash
Choose: 1
📚 Movies
1. Trending Movies
2. Popular Movies
...
A. Show all
0. Back
```

Select an item to see a clean terminal table:

```
📊 Trending Movies
+---------------------+------+---------+-----------------------+
| Title               | Year | Rating  | Genres                |
+---------------------+------+---------+-----------------------+
| Dune: Part Two      | 2024 | 8.7     | sci-fi, adventure     |
| The Batman          | 2022 | 7.9     | action, crime, drama  |
+---------------------+------+---------+-----------------------+
```

---

## 🙌 Acknowledgements

* [Trakt.tv API](https://trakt.docs.apiary.io/)

---

## 📫 Contributions

Pull requests and suggestions welcome!
Want a GUI version or OAuth support next? Open an issue!
