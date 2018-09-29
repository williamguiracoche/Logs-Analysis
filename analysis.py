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
  cursor.execute("select title, count(*) as num from log, articles where log.path like '%' || articles.slug group by title order by num desc limit 3;")
  results = cursor.fetchall()
  db.close()
  print 'Most Popular Articles:'
  for title, views in results:
      print title + ' -- ' + str(views)  + ' views'


def popular_authors():
  db = psycopg2.connect("dbname=news")
  cursor = db.cursor()
  cursor.execute('''
    select authors.name, subq2.sum from
    (select author, count (*) as sum from
    (select author, path from articles, log
    where log.path like '%' || articles.slug) as subq
    group by author) as subq2, authors
    where authors.id = subq2.author
    order by subq2.sum desc;
    ''')
  results = cursor.fetchall()
  db.close()
  print 'Most Popular Authors:'
  for name, views in results:
      print name + ' -- ' + str(views)  + ' views'

popular_articles()
print '\n'
popular_authors()
