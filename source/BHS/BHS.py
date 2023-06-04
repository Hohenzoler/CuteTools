#Browsing History Scraper or BHS
import sqlite3
import os
import shutil

def get_chrome_history():
    if os.name == "posix":
        history_db = os.path.expanduser("~/.config/google-chrome/Default/History")
    elif os.name == "nt":
        history_db = os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History")
    else:
        raise NotImplementedError("Unsupported operating system")

    temp_db = "./temp_history"
    shutil.copy2(history_db, temp_db)

    conn = sqlite3.connect(temp_db)
    cursor = conn.cursor()
    cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls")
    rows = cursor.fetchall()
    conn.close()
    return rows


def save_history_to_file(history_rows, file_path):
    with open(file_path, "w", encoding="utf-8", errors="ignore") as file:
        for row in history_rows:
            url = row[0]
            title = row[1]
            visit_count = row[2]
            last_visit_time = row[3]

            file.write(f"URL: {url}\n")
            file.write(f"Title: {title}\n")
            file.write(f"Visit Count: {visit_count}\n")
            file.write(f"Last Visit Time: {last_visit_time}\n")
            file.write("-" * 50)
            file.write("\n")

history = get_chrome_history()
file_path = "browsing_history.txt"
save_history_to_file(history, file_path)
