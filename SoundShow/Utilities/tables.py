user = "CREATE TABLE IF NOT EXISTS user( \
        first_name VARCHAR(32) NOT NULL,\
        last_name VARCHAR(32) NOT NULL, \
        user_name VARCHAR(20) NOT NULL,\
        pass_word VARCHAR(256) NOT NULL, \
        uuid VARCHAR(40) NOT NULL, \
        joined TIMESTAMP NOT NULL, \
        PRIMARY KEY(user_name, uuid));"

category = "CREATE TABLE IF NOT EXISTS category(\
        category_name VARCHAR(32) NOT NULL, \
        img_path VARCHAR(50) NOT NULL, \
        num_interested BIGINT DEFAULT 0, \
        PRIMARY KEY (category_name) );"

content = "CREATE TABLE IF NOT exists content(\
           content_name VARCHAR(32) NOT NULL, \
           category_name VARCHAR(32) NOT NULL, \
           num_interested BIGINT NOT NULL, \
           PRIMARY KEY (content_name), \
           FOREIGN KEY (category_name) REFERENCES category(category_name) \
           ON DELETE CASCADE);"

user_interests = "CREATE TABLE IF NOT EXISTS user_interests(\
                  user_name VARCHAR(20) NOT NULL, \
                  uuid VARCHAR(40) NOT NULL, \
                  category_name VARCHAR(32) NOT NULL, \
                  PRIMARY KEY(user_name, uuid, category_name), \
                  FOREIGN KEY (user_name, uuid) REFERENCES user(user_name, uuid), \
                  FOREIGN KEY (category_name) REFERENCES category(category_name) \
                  ON DELETE CASCADE);"


num_interested_view = "CREATE VIEW Num_Interested AS \
                  SELECT category_name, COUNT(user_name) AS \
                  num_interested FROM user_interests WHERE \
                  category_name IN (SELECT category_name FROM CATEGORY) \
                  GROUP BY(category_name);"
