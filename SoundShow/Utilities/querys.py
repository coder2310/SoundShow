USER_EXISTS = "SELECT * FROM user WHERE user_name = %s;"
AUTH_LOGIN = "SELECT * FROM user WHERE user_name = %s and pass_word = %s"
INSERT_USER = "INSERT into user (first_name, last_name, user_name, pass_word, uuid, joined) \
    VALUES (%s, %s,%s, %s,%s,%s);"
GET_UUID = "SELECT uuid FROM user WHERE user_name = %s;"
GET_INFO_USING_USERNAME = "SELECT * FROM user WHERE user_name = %s;"
GET_INFO_USING_UUID = "SELECT * FROM user WHERE UUID = %s;"
DROP_TABLE = "DROP TABLE {};"  # have to use DROP_TABLE.format(table_name)
# have to use TRUNCATE_TABLE.format(table_name)
TRUNCATE_TABLE = "TRUNCATE TABLE {};"
INSERT_CATEGORY = "INSERT INTO category (category_name, img_path) VALUES (%s,%s);"
DROP_DATABASE = "DROP DATABASE {};"

