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

ADD_INTEREST = "INSERT INTO user_interests (user_name, uuid, category_name) \
                VALUES (%s, %s, %s);"

GET_NUMBER_INTERESTED_VIEW = "CREATE VIEW NumInterested AS \
                  SELECT category_name, COUNT(user_name) AS \
                  num_interested FROM user_interests WHERE \
                  category_name IN (SELECT category_name FROM CATEGORY) \
                  GROUP BY(category_name);"
UPDATE_CATEGORY_COUNT = "" # This will be written later
