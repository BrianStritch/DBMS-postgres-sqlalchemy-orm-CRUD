# __Error fix due to Gitpod change__
If you get the following error after typing psql in the terminal:

psql: error: could not connect to server: No such file or directory

Please use the following command in the terminal to set an environment variable needed for it to work:

set_pg

And then try the psql command again

You will need to do this each time you return to your Gitpod workspace for the Database Management Systems videos.



- Extra Links:

Code Institute Gitpod Template (Important: You must use this Gitpod Template to complete this module)
Chinook Database SQL

wget https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_PostgreSql.sql


-
   # __instructions and commands__

    1. To view, or list, any databases in our environment, we can type \l.

    2. to cvreate a new database , type , CREATE DATABASE chinook;

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








- h
- h
- h
- h
- h
- h
- h
- h
- h
- h
- h
- h
- h
- h
- h





































![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome BrianStritch,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
