USER_EXISTS = "SELECT * FROM user WHERE user_name = %s;"
AUTH_LOGIN = "SELECT * FROM user WHERE user_name = %s and pass_word = %s"
INSERT_USER = "INSERT INTO user (first_name, last_name, user_name, pass_word, uuid, joined) \
    VALUES (%s, %s,%s, %s,%s,%s);"
GET_UUID = "SELECT uuid FROM user WHERE user_name = %s;"
GET_INFO_USING_USERNAME = "SELECT * FROM user WHERE user_name = %s;"
GET_INFO_USING_UUID = "SELECT * FROM user WHERE UUID = %s;"
# have to use DROP_TABLE.format(table_name)
DROP_TABLE = "DROP TABLE IF EXISTS {};"
DROP_VIEW = "DROP VIEW IF EXISTS {};"
GET_FULL_NAME = "SELECT first_name, last_name FROM user WHERE user_name = %s;"
# have to use TRUNCATE_TABLE.format(table_name)

TRUNCATE_TABLE = "TRUNCATE TABLE {};"
INSERT_CATEGORY = "INSERT INTO category (category_name, img_path) VALUES (%s,%s);"
DROP_DATABASE = "DROP DATABASE {};"

ADD_INTEREST = "INSERT INTO user_interests (user_name, uuid, content_name) \
                VALUES (%s, %s, %s);"
ADD_CONTENT = "INSERT INTO content (content_name, category_name, num_interested) \
                VALUES (%s, %s,0);"
ADD_CATEGORY = "INSERT INTO category (category_name) VALUES (%s);"

INCREASE_CONTENT_COUNT = "UPDATE content \
                        SET num_interested = num_interested + 1\
                        WHERE content_name = %s;"
DECREASE_CONTENT_COUNT = "UPDATE content \
                        SET num_interested = num_interested - 1\
                        WHERE content_name = %s;"
RESET_CONTENT_COUNT = "UPDATE content\
                        SET num_interested = 0;"
RETRIEVE_RELATED_CONTENT = "SELECT content_name FROM content WHERE category_name = %s;"
RETRIEVE_TOP_CONTENT = "SELECT content_name FROM content ORDER BY(num_interested) DESC LIMIT %s;"
GET_USERS_INTERESTS = "SELECT content_name FROM user_interests WHERE user_name = %s;"
INSERT_INTO_HISTORY = "INSERT INTO user_search_history (user_name, search_term, searched_at) \
                    VALUES(%s, %s, %s);"
GET_USER_SEARCH_HISTORY = "SELECT search_term, searched_at FROM user_search_history WHERE user_name = %s;"
USER_SESSION_CATEGORIES = "SELECT DISTINCT category_name FROM content NATURAL JOIN \
                    (SELECT content_name FROM \
                    user_interests WHERE user_name = %s) as T2;"

GET_TOP_TEN_CATEGORIES = "SELECT DISTINCT category_name FROM content NATURAL JOIN \
                        (SELECT user_interests.content_name FROM user_interests) \
                        as T2 LIMIT 10;"

CLEAR_SEARCH_HISTORY = "DELETE FROM user_search_history WHERE user_name =%s;"

DELETE_USER_INTEREST = "DELETE FROM user_interests \
                        WHERE user_name = %s AND \
                        content_name = %s;"
ADD_USER_FAVORITE = "INSERT INTO \
                    user_favorites(user_name, title, hashed_link)\
                    VALUES(%s,%s,%s);"

ADD_LINK = "INSERT INTO favorites \
            (link, hashed_link) VALUES(%s, %s);"
