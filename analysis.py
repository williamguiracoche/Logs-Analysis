'''
Questions that must be answered:

1. What are the most popular three articles of all time?
Which articles have been accessed the most? Present this information as a
sorted list with the most popular article at the top.


2. Who are the most popular article authors of all time? That is, when you sum
up all of the articles each author has written, which authors get the most
page views? Present this as a sorted list with the most popular author at
the top.

3. On which days did more than 1% of requests lead to errors? The log table
includes a column status that indicates the HTTP status code that the news
site sent to the ugitser's browser.

'''

import psycopg2

def popular_articles():
  db = psycopg2.connect("dbname=news")
  cursor = db.cursor()
  cursor.execute("select path, count(*) as num from log where status = '200 OK' and not path = '/' group by path limit 3;")
  results = cursor.fetchall()
  db.close()
  return results

print popular_articles()
