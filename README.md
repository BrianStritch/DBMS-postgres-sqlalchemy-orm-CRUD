# __POSTGRESQL / SQLALCHEMY / PSYCOPG2 __

## __Error fix due to Gitpod change__
If you get the following error after typing psql in the terminal:

psql: error: could not connect to server: No such file or directory

Please use the following command in the terminal to set an environment variable needed for it to work:

set_pg

And then try the psql command again

__You will need to do this each time you return to your Gitpod workspace for the Database Management Systems videos.__



- Extra Links:

Code Institute Gitpod Template (Important: You must use this Gitpod Template to complete this module)
Chinook Database SQL

wget https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_PostgreSql.sql


# __initial setup__
To launch the Postgres CLI, we can simply type "psql" and hit enter.
To view, or list, any databases in our environment, we can type \l.
By default, the Postgres CLI comes with 3 databases out of the box; 'postgres', 'template0', and 'template1'.
Instead of using any of these default databases, let's create a new database for our Chinook lessons.
CREATE DATABASE chinook; Don't forget the semicolon at the end of the command,
which is the standard way to separate each SQL statement, since you can theoretically
combine multiple commands in a single entry.
If you've hit enter without adding the semicolon, it will assume you're wanting to add additional
commands, so just add your semicolon now, and hit enter.
We now have a fourth database, called Chinook, which is currently empty.
If we needed to switch between databases, we can simply type \c followed by the name
of the database we want to switch over to.
\c postgres - now we're on the default postgres database.
\c chinook - and now we're connected to our new database.
The \c stands for 'connect' in case you're wondering, telling it which database to connect to.
Finally, while we're connected to our new chinook database, we need to initialize or
install the downloaded sample Chinook PostgreSQL database.
\i Chinook_PostgreSql.sql The \i generally means include, integrate, install, or initialize.

-
   # __instructions and commands__

    1. To view, or list, any databases in our environment, we can type \l.

    2. to create a new database , type , CREATE DATABASE chinook;

    3.  the standard way to separate each SQL statement is by adding a semicolon at the end of the statement, since you can theoretically
    combine multiple commands in a single entry.

    4. If we needed to switch between databases, we can simply type \c followed by the name
    of the database we want to switch over to.
    \c postgres - now we're on the default postgres database.
    \c chinook - and now we're connected to our new database.
    The \c stands for 'connect' in case you're wondering, telling it which database to connect to.

    5. to install the downloaded sample Chinook PostgreSQL database.
    you use : \i Chinook_PostgreSql.sql The \i generally means include, integrate, install, or initialize.

    6. to exit the database type \q to exit, or quit, the Postgres CLI, taking us out of the server and back
        to the normal workspace terminal.
    7. When we start the Postgres shell, we can actually include a flag to specify which database we'd
        like to connect to once Postgres is loaded.
        'psql -d chinook' . This will start the server, and tell it that
        the database we want to connect to is the one called "chinook", as declared by using
        the -d flag to specify a database name.
    8. to confirm that all tables and data were successfully added to the database.
        '\dt' . This will allow us to display tables on our database.

    9. Technically you don't need to write the SQL commands in capital letters, but it's standard
        practice to distinguish between the different pieces of your query string.
        The asterisk is a common programming method to signify a wildcard, which essentially means
        to select anything and everything.

            Also note, I've used double-quotes intentionally, because using single-quotes will throw a 'syntax error',
            - example used : SELECT * FROM "Artist";

    10. Finally, the command must end with a semicolon, to specify that this is the end of our query.
        If you omit the semicolon and hit enter, nothing happens, but in reality, it's waiting for
        you to finish building your query, which can span multiple lines.

    11. after entering the query above we are presented with two columns on this Artist table.
        ArtistId, which acts as our primary key for each individual row on the table, and Name,
        which is the name of the artists on the table.

    12. In order to exit this query search, simply type the letter "q" and hit enter, but not
        to be confused with \q which will quit the Postgres CLI.

    13. Next, let's query the same table, but this time, only retrieve the "Name" column.
        Again, I'm specifically using double-quotes, and an ending semicolon.
        As you can see, we get the same data, but this time only from the column with a title of "Name".

            - example used : SELECT "Name" FROM "Artist";  -- this just displays the list of artist names.
            - typing q will return us to the command prompts

    14. to use a more specific query we can use the where clause as follows ,

            - example used : SELECT * FROM "Artist" WHERE "Name" = 'Queen';  -- displays only search resiults for any artis with name  Queen

    15. I'll perform the same exact query, but this time we'll specify the ArtistId of 51 instead of the artist name.
        Since 51 is a primary key and integer, we don't need the single-quotes, but it will
        still work if you include them.
        Next, we'll perform the same exact query one more time, but instead of looking within the
        Artist table, we're going to look at the Album table.
        This time, it has a list of any album on the database whose ArtistId is 51, which we already
        know is the primary key for Queen.
            
            - SELECT * FROM "Album" WHERE "ArtistId" = 51;

    16. For our final sample query, I'm going to look within the table called "Track", and use the
        column header of "Composer" to search for all tracks by Queen.

            - SELECT * FROM "Track" WHERE "Composer" = 'Queen';     -- this returns all queens tracks in the database


    17. I'm going to do is use that same command once again, but this time I'll copy the results into sample CSV and JSON
        files. You don't need to understand these commands, they're simply to demonstrate our database
        content into a format you might be more familiar with.
        When I open each of these new files, you can see that we have a standard CSV file with
        our results, as well as a standard JSON file with the same results.
        I've taken the liberty of pasting the CSV data into a generic spreadsheet program, such
        as Microsoft Excel, LibreOffice Calc, or Google Sheets.
        As you can see, it's the same data, just presented in a more familiar everyday method, with the
        spreadsheet columns and rows.
        The same can be said with our JSON file, and once I've applied some quick formatting, our
        data is now presented in a standard JSON layout.
        Taking those into consideration, ultimately we could do the same thing reversed, if we
        have existing CSV or JSON files, we could perform a data dump and have it create our database for us.

            - example used by instructor: \copy (SELECT * FROM "Track" WHERE "Composer" = 'Queen') TO 'Test.csv' WITH CSV DELIMITER ',' HEADER;   -- created a new file test.csv and copied the data into it

            - \o test.json  --- creates a new test.json file

            - SELECT json_agg(t) from (SELECT * FROM "Track" WHERE "Composer" = 'Queen')t;  -- copies the data in to the json
              file in json format

            - __all the above was done by the instructor as an example of what you can do with the data__



# __sql-psycopg2.py__
    - instructions-psql-psycopg2.py
       - this file contains the entry level instructions to execute basic queries on a DB
       - see the sql-psycopg2.py file for further instructions and notes

# __instructions-sqlAlchemy.py__
    - instructions-sqlAlchemy.py for installing sqlAlchemy

# __sql-expression.py__
       - this file contains the middle level instructions to execute queries on a DB using sql statements written in a more pythonic way.
       - see the sql-expression.py file for further instructions and notes
# __sql-orm.py__
       - this file contains the top level instructions to execute queries on a DB using python classes instead of using tables and connections.
       - see the sql-orm.py file for further instructions and notes

.
.
.
.
.
.
.
# __DBMS CODE ALONG__
.
.
.
# __CRUD__
  - Create
  - Read
  - Update
  - Delete

## __Create and Read

