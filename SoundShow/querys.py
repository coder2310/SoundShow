user_exists = "SELECT * FROM user WHERE user_name = %s;"
auth_login = "SELECT * FROM user WHERE user_name = %s and pass_word = %s"
insert_user = "INSERT into user (first_name, last_name, user_name, pass_word, uuid, joined) \
    VALUES (%s, %s,%s, %s,%s,%s);"