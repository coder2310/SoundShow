import pymysql.cursors
DB_CONN = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'port':8889,
  'database': 'SoundShow',
  'charset' : 'utf8mb4',
  'cursorclass' : pymysql.cursors.DictCursor,
  'autocommit' : True
}