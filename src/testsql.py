import psycopg2

def search_user(username):
    con=psycopg2.connect(dbname="testdb",user="testuser", password="testing", host="123.123.123.123", port=5432)
    query=f"select * from users where username='{username}'"