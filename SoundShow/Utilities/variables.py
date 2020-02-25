import pymysql.cursors
DB_CONN = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'port': 8889,
    'database': 'SoundShow',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
    'autocommit': True
}
CATEGORIES = sorted(["music", "food", "travel", "literature", "pets", "health", "video games",
              "sports", "art", "technology", "movies", "religion"])
