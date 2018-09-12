import psycopg2, csv, sys

conn = psycopg2.connect (database="cwcdb", user="root", password="cwc", host="localhost", port="5432")
cur = conn.cursor()


def process_query(query):
    #print query
    cur.execute(query)
    records = cur.fetchall()
    return records