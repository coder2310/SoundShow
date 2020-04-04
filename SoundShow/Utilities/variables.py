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
CONTENT = {
    "Music": ["Hip Hop", "Rock", "Heavy Metal", "Pop Music", "Country Music", "Jazz", "Rap", "Blues",
              "Billoard Top 100", "Billboard Top 200", "Latin Trap", "Reggaeton", "Spotify News", "Apple Music News"],
    "Food": ["Cooking Channels", "Restraunts", "Popular Recipes", "Vegan Recipes", "Brunch Spots"],
    "Travel": ["Weekend Getaways", "Exotic Islands", "Warm Weather", "Hiking", "African Safari", "City Touring"],
    "Literature": ["Poetry", "Recent Best Sellers", "Comic Books"],
    "Pets": ["Cat Videos", "Pet Shows", "Best Pet Foods"],
    "Health": ["Weight Lifting", "Body Building", "Healthy Recipes", "Weight Loss Tips", "Keto Diet",
               "Muscle Gaining Tips", "At Home Workouts"],
    "Games": ["First Person Shooters", "VR Games", "AR Games", "VR Consoles", "AR Consoles", "Upcoming Video Game Releases", "Video Game Consoles"],
    "Sports": ["Soccer News", "Basketball News", "Baseball News", "Tennis News", "Cricket News", "Boxing News",
               "MMA News"],
    "Art": ["Street Art", "Famous Paintings", "Famous Artists", "Art Shows", "Art Auctions", "Art Forgerys"],
    "Technology": ["2020 Smartphones", "New Laptop Releases", "VR News", "AR News", "Intel", "Tesla", "AMD", "Google", "AI/ML", "Apple"],
    "Movies": ["2020 Movie Releases", "Disney", "Netflix", "Marvel", "Warner Bros", "Indie Movies"],
    "Religion": ["Islam", "Christianity", "Judiasm", "Spritual", "Theology", "Vatican City"],
    "News": ["Current Events", "Today in History", "Politcal News", "Congress", "State Elections",
             "Country Election", "International Relations"],
    "Science": ["Medicine", "Nasa", "New Space Discoveries", "Cancer Research"],
    "Economics": ["World Economy", "Usa Economy", "Nyse", "Dow Jones", "Wall Street", "Fiscal Year"]
}
CATEGORIES = sorted(CONTENT.keys())
