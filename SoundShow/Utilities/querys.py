USER_EXISTS = "SELECT * FROM user WHERE user_name = %s;"
AUTH_LOGIN = "SELECT * FROM user WHERE user_name = %s and pass_word = %s"
INSERT_USER = "INSERT INTO user (first_name, last_name, user_name, pass_word, uuid, joined) \
    VALUES (%s, %s,%s, %s,%s,%s);"
GET_UUID = "SELECT uuid FROM user WHERE user_name = %s;"
GET_INFO_USING_USERNAME = "SELECT * FROM user WHERE user_name = %s;"
GET_INFO_USING_UUID = "SELECT * FROM user WHERE UUID = %s;"
DROP_TABLE = "DROP TABLE {};"  # have to use DROP_TABLE.format(table_name)
# have to use TRUNCATE_TABLE.format(table_name)
TRUNCATE_TABLE = "TRUNCATE TABLE {};"
INSERT_CATEGORY = "INSERT INTO category (category_name, img_path) VALUES (%s,%s);"
DROP_DATABASE = "DROP DATABASE {};"

ADD_INTEREST = "INSERT INTO user_interests (user_name, uuid, content_name) \
                VALUES (%s, %s, %s);"
ADD_CONTENT = "INSERT INTO content (content_name, category_name, num_interested) \
               VALUES (%s, %s,0);"
UPDATE_CATEGORY_COUNT = "UPDATE category\
                        SET num_interested = \
                        (SELECT num_interested FROM num_interested \
                        WHERE category_name = %s) \
                        WHERE category_name = %s;" 
                        # Will try to come up with a better way to write this
                        # Seems veryt redunadt and perhaps ineffeicient, but it
                        # works for now
RETRIEVE_RELATED_CONTENT = "SELECT content_name FROM content WHERE category_name = %s;"
