import psycopg2


def popular_articles():
    ''' Prints the titles of the top 3 articles that have been viewed the
    most and how many views they each had.
    '''
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute('''
    select title, count(*) as num from log, articles
    where log.path like '%' || articles.slug
    group by title
    order by num desc
    limit 3;
    ''')
    results = cursor.fetchall()
    db.close()
    print 'Most Popular Articles:'
    for title, views in results:
        print title + ' -- ' + str(views) + ' views'


def popular_authors():
    ''' Prints the names of the authors in order of whose articles have been
    viewed the most. This answers, when you sum up all of the articles each
    author has written, which authors get the most page views?
    '''
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute('''
    with subq as (
    select author, path from articles, log
    where log.path like '%' || articles.slug
    ),

    subq2 as (
    select author, count (*) as sum from subq
    group by author
    )

    select authors.name, subq2.sum from subq2, authors
    where authors.id = subq2.author
    order by subq2.sum desc;
    ''')
    results = cursor.fetchall()
    db.close()
    print 'Most Popular Authors:'
    for name, views in results:
        print name + ' -- ' + str(views) + ' views'


def high_error():
    '''Returns a list of which days had more than 1% of requests lead to errors
    and what the percentage of error was.
    '''

    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute('''
    with subq as (
    select count (*) as sum, date_trunc('day',time) as day,status from log
    group by date_trunc('day', time), status
    ),

    subq2 as (
    select a.day as day, a.sum as successful , b.sum as error
    from  subq as a, subq as b
    where b.status = '404 NOT FOUND'
    and not a.status = b.status
    and a.day = b.day
    ),

    subq3 as (
    select
    to_char(day,'FMMonth DD, YYYY'), round(error * 100.0 / successful, 2)
    as percentage_error from subq2
    )

    select * from subq3
    where percentage_error > 1;

    ''')
    results = cursor.fetchall()
    db.close()
    for day, percentage in results:
        print 'Days with more than 1% errors:'
        print (day + ' -- ' + str(percentage) + '% errors')

popular_articles()
print '\n'
popular_authors()
print '\n'
high_error()
