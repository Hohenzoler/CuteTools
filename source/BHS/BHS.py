#Browsing History Scraper or BHS
import sqlite3
import os
import shutil
import datetime

def get_browsing_history(browser_name):
    if browser_name == "Chrome":
        if os.name == "posix":
            history_db = os.path.expanduser("~/.config/google-chrome/Default/History")
        elif os.name == "nt":
            history_db = os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History")
        else:
            raise NotImplementedError("Unsupported operating system")
    elif browser_name == "Firefox":
        if os.name == "posix":
            history_db = os.path.expanduser("~/.mozilla/firefox/*.default-release/places.sqlite")
        elif os.name == "nt":
            history_db = os.path.expanduser("~\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*.default-release/places.sqlite")
        else:
            raise NotImplementedError("Unsupported operating system")
    elif browser_name == "Edge":
        if os.name == "posix":
            history_db = os.path.expanduser("~/.config/microsoft-edge/Default/History")
        elif os.name == "nt":
            history_db = os.path.expanduser("~\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\History")
        else:
            raise NotImplementedError("Unsupported operating system")
    elif browser_name == "Opera":
        if os.name == "posix":
            history_db = os.path.expanduser("~/.config/opera/History")
        elif os.name == "nt":
            history_db = os.path.expanduser("~\\AppData\\Roaming\\Opera Software\\Opera Stable\\History")
        else:
            raise NotImplementedError("Unsupported operating system")
    else:
        raise ValueError("Invalid browser name")
    if not os.path.isfile(history_db):
        return []

    temp_db = "./temp_history"
    shutil.copy2(history_db, temp_db)
    conn = sqlite3.connect(temp_db)
    cursor = conn.cursor()
    cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls")
    rows = cursor.fetchall()
    conn.close()
    return rows

def save_history_to_file(history_rows, browser_name):
    file_path = f"{browser_name.lower()}_history.txt"
    with open(file_path, "w", encoding="utf-8", errors="ignore") as file:
        for row in history_rows:
            url = row[0]
            title = row[1]
            visit_count = row[2]
            last_visit_time = row[3]

            last_visit_time = datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=last_visit_time)

            file.write(f"URL: {url}\n")
            file.write(f"Title: {title}\n")
            file.write(f"Visit Count: {visit_count}\n")
            file.write(f"Last Visit Time: {last_visit_time}\n")
            file.write("-" * 50)
            file.write("\n")


browsers = ["Chrome", "Firefox", "Edge", "Opera"]

for browser in browsers:
    history = get_browsing_history(browser)
    save_history_to_file(history, browser)
