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
CONTENT =  {
    "music" : ["hip hop", "rock", "heavy metal", "pop music", "country music", "jazz", "rap", "blues"],
    "food"  : ["cooking channels", "restraunts", "popular recipes", "vegan recipes", "brunch spots" ],
    "travel" : ["weekend getaways", "exotic", "warm weather", "hiking", "african safari"],
    "literature" : ["poetry", "recent best sellers", "comic books"],
    "pets" : ["cat videos", "pet shows"],
    "health" : ["weight lifting", "body building", "healthy recipes", "weight loss tips", "keto diet", 
                "muscle gaining tips"],
    "video games": ["first person shooters", "VR/AR games", "upcoming video game releases", "video game consoles"],
    "sports" : ["soccer news", "basketball news", "baseball news", "tennis news", "cricket news", "boxing news",
                "MMA news"],
    "art" : ["street art", "famous paintings", "famous artists", "art shows", "art auctions"],
    "technology": ["2020 smartphones", "new laptop releases", "VR/AR news", "intel", "tesla", "amd", "google", "AI/ML", "apple"],
    "movies" : ["2020 movie releases", "disney", "netflix", "marvel"],
    "religion" : ["islam", "christianity", "judiasm", "spritual", "theology"]
}
CATEGORIES = sorted(["music", "food", "travel", "literature", "pets", "health", "video games",
              "sports", "art", "technology", "movies", "religion"])
