# Logs Analysis Project
The purpose of this project is create an internal reporting tool from a given database in a way that is easy to understand. With the completion of this project, I hope to practice my SQL skills by building a reporting tool that summarizes data from a large database.

In this project, I worked with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

## Getting Started
The main project is run on python version 2 and the database is on a SQL file. To run the project, you can use PostgreSQL to use the SQL queries necessary. I used a virtual machine with a vagrant directory to run PostgreSQL. The main file, analysis.py, imports the psycopg2 library to manage the SQL database.

You can download the database from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip (provided by Udacity.) To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql

To create the report, simply run 'python analysis.py' in your running virtual machine.

## Report Objectives
The report is created by three main functions: popular_articles(), popular_authors(), and high_error().

### popular_articles()

Finds the top three articles that have been accessed the most. The information is presented as a sorted list with the most popular article at the top.

### popular_authors()
Finds the most popular article authors. That is, when you sum up all of the articles each author has written, this function finds which authors had the most page views. This information is presented as a sorted list with the most popular author at the top.

### high_error()
Finds the days in which more than 1% of requests lead to errors.

## The data
The database was provided by Udacity and can be downloaded with the link https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip. Make sure that the folder is in the same directory as your analysis.py file.

The database includes three tables:

* The authors table includes information about the authors of articles.
* The articles table includes the articles themselves.
* The log table includes one entry for each time a user has accessed the site.

##Author
William Guiracoche

## Acknowledgments and Resources used
* The project assignment and the database in newsdata.sql was provided by Udacity's Full Stack Web Developer Nanodegree Program Curriculum
