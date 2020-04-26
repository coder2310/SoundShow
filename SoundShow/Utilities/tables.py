USER = "CREATE TABLE IF NOT EXISTS user( \
        first_name VARCHAR(32) NOT NULL,\
        last_name VARCHAR(32) NOT NULL, \
        user_name VARCHAR(20) NOT NULL,\
        pass_word VARCHAR(256) NOT NULL, \
        uuid VARCHAR(40) NOT NULL, \
        joined TIMESTAMP NOT NULL, \
        PRIMARY KEY(user_name, uuid));"

CATEGORY = "CREATE TABLE IF NOT EXISTS category(\
        category_name VARCHAR(32) NOT NULL, \
        PRIMARY KEY (category_name) );"

CONTENT = "CREATE TABLE IF NOT EXISTS content(\
        content_name VARCHAR(32) NOT NULL, \
        category_name VARCHAR(32) NOT NULL, \
        num_interested BIGINT NOT NULL, \
        PRIMARY KEY (content_name), \
        FOREIGN KEY (category_name) REFERENCES category(category_name) \
        ON DELETE CASCADE);"

USER_INTERESTS = "CREATE TABLE IF NOT EXISTS user_interests(\
                user_name VARCHAR(20) NOT NULL, \
                uuid VARCHAR(40) NOT NULL, \
                content_name VARCHAR(32) NOT NULL, \
                PRIMARY KEY(user_name, uuid, content_name), \
                FOREIGN KEY (user_name, uuid) REFERENCES user(user_name, uuid) \
                ON DELETE CASCADE);"

USER_SEARCH_HISTORY = "CREATE TABLE IF NOT EXISTS user_search_history(\
                        user_name VARCHAR(20) NOT NULL, \
                        search_term VARCHAR(40) NOT NULL, \
                        searched_at TIMESTAMP NOT NULL,\
                        FOREIGN KEY(user_name) REFERENCES user(user_name) \
                        ON DELETE CASCADE);"

NUM_INTERESTED_VIEW = "CREATE VIEW Num_Interested AS \
                        SELECT category_name, SUM(num_interested) AS amount \
                        FROM content GROUP BY(category_name) ORDER BY amount DESC;"


USER_FAVORITES = "CREATE TABLE IF NOT EXISTS user_favorites( \
                user_name VARCHAR(20) NOT NULL, \
                title VARCHAR(300) NOT NULL, \
                hashed_link VARCHAR(256) NOT NULL, \
                PRIMARY KEY (user_name, hashed_link),\
                FOREIGN KEY(user_name) REFERENCES user(user_name) \
                ON DELETE CASCADE);"

FAVORITES =    "CREATE TABLE IF NOT EXISTS favorites( \
                link varchar(50) NOT NULL, \
                hashed_link VARCHAR(256) NOT NULL,\
                PRIMARY KEY(hashed_link));"