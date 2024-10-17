
# Metaweb:Site improvements (Patrick Tufts)

From the Quicksilver Metaweb.



### MediaWiki 1.3.10 Upgrade



[I](/user-blair) suspect that there will be a few minor customizations that were done to the older MediaWiki code that will need to be applied to the new version of the MediaWiki and that some of these may be missed. If you find any of these, please do let me know.

According to [Patrick](/user-patrick-tufts), the latest stable MediaWiki version has some nice enhancements, including a built-in word processor - users will have the option of using the old-style web text boxes for editing, or they can use an edit button that calls up a miniature Word-style editor.

-- [Blair](/user-blair) Feb 2 17:10:31 PST 2005

 As Blair says, the more recent MediaWiki code (currently in use on [http://www.wikipedia.org)](/http-www-wikipedia-org) has improved editing features and also a cleaner user interface. While Blair upgrades the software, things might be a bit bumpy, but bear with us. The new code is worth it. --[Pat](/user-patrick-tufts) 23:21, 4 Feb 2005 (PST)

 Due to unforseen work that needed to be done on the day of the upgrade, I've rescheduled the upgrade to Tuesday, February 15, 2005 at 10:00 am PST. I'll also be upgrading the server to MediaWiki 1.3.10. -- [Blair](/user-blair) Mon Feb 14 12:11:31 PST 2005

 I tried to upgrade MediaWiki today and I ended up with a large number of broken links the home page. It's not clear what caused this. Here's the text from the upgrade log. It appears that the problem has something to do with "9606 valid titles and 755 invalid titles were processed." -- [Blair](/user-blair) Tue Feb 15 11:50:45 PST 2005

 Check your text editor to see that it isn't adding or subtracting invisble characters. - [Sparky](/user-stsparky)


```
    MediaWiki 1.3.10 installation

```


```
    Please include all of the lines below when reporting installation problems.
    Checking environment...

```


```
    * PHP 4.3.10: ok
    * PHP server API is apache; ok, using pretty URLs (index.php/Page\_Title)
    * Have XML / Latin1-UTF-8 conversion support.
    * PHP's memory\_limit is 32M. If this is too low, installation may fail!
    * Have zlib support; enabling output compression.
    * Found GD graphics library built-in, image thumbnailing will be enabled if you enable uploads.
    * Installation directory: /export/home2/apache/public\_html/metaweb.com/production/wiki
    * Script URI path: /wiki
    * Connected as root (automatic)
    * Connected to database... 4.0.23-standard; enabling MySQL 4 enhancements
    * Database metaweb exists
    * There are already MediaWiki tables in this database. Checking if updates are needed...

```


```
    ...ipblocks is up to date.
    ...already have interwiki table
    ...indexes seem up to 20031107 standards
    ...Adding linkscc table.
    ...linkscc is up to date, or does not exist. Good.
    ...have hitcounter table.
    Adding rc\_ip...ok
    Converting links table to ID-ID...
    Loading IDs from cur table...
        1000 rows of cur table read.
        2000 rows of cur table read.
        3000 rows of cur table read.
    Finished loading IDs.

```


```
    Dropping temporary links table if it exists... done.
    Creating temporary links table... done.

```


```
    Processing 10361 rows from links table...
    Inserting 780 tuples into links\_temp... done. Total 780 tuples inserted.
    Inserting 853 tuples into links\_temp... done. Total 1633 tuples inserted.
    Inserting 977 tuples into links\_temp... done. Total 2610 tuples inserted.
    Inserting 981 tuples into links\_temp... done. Total 3591 tuples inserted.
    Inserting 912 tuples into links\_temp... done. Total 4503 tuples inserted.
    Inserting 937 tuples into links\_temp... done. Total 5440 tuples inserted.
    Inserting 988 tuples into links\_temp... done. Total 6428 tuples inserted.
    Inserting 954 tuples into links\_temp... done. Total 7382 tuples inserted.
    Inserting 957 tuples into links\_temp... done. Total 8339 tuples inserted.
    Inserting 941 tuples into links\_temp... done. Total 9280 tuples inserted.
    Inserting 326 tuples into links\_temp... done. Total 9606 tuples inserted.
    9606 valid titles and 755 invalid titles were processed.

```


```
    Dropping backup links table if it exists... done.
    Swapping tables 'links' to 'links\_backup'; 'links\_temp' to 'links'... done.

```


```
    Conversion complete. The old table remains at links\_backup;
    delete at your leisure.
    Adding user\_real\_name field to table user...ok
    ...have special page querycache table.
    ...have objectcache table.
    ...have categorylinks table.
    Creating redirects
    Gnunote...redirected
    All\_messages...redirected

```


```
    Moving pages...
    Gnunote...moved
    All\_messages...moved

```


```
    Converting text...
    Initialising "MediaWiki" namespace...
    Clearing message cache...Done.

```


```
    * Finished update checks.

```


```
    Creating LocalSettings.php...

```


```
    Success! Move the LocalSettings.php file into the parent directory, then follow this link to your wiki.

```

If anybody has any suggestions, please let me know. I could make a new wiki site and make a copy of the MySQL database to mess around with if needed.

What problems did you have besides the broken links, and how were they broken? Perhaps you just needed to run some refresh script for the links. I would suggest posting to the mediawiki mailing list if you haven't done so already. Tons of helpful people there and it's more visible than this talk page.

### No Neal Stephenson Page


[I](/user-mlorrey) got this wild question in my head about why Neal Stephenson never writes about ANY space travel in his novels, like it doesn't exist, even in the era of [The Diamond Age](/the-diamond-age), when I discovered there is no Neal Stephenson Page in the Metaweb. Should I instead put this qeustion on the Enoch Root page? :)

There is an [Neal Stephenson](/user-nealstephenson) page. But the man is busy writing to put food on his table as it were. - [Sparky](/user-stsparky) 17:36, 2005 Feb 12 (PST)

### Older Discussions


We'll be making some improvements to the layout of the Metaweb over the weekend. The biggest change will be a new layout for the front page. [User:Tpierce](/user-tpierce) and I are working on making this page cleaner and more navigable.

As we roll out these changes, please let us know what you think. Click on the "Discuss this page" link on the right to add your comments.

 See [Metaweb:Meta-metaweb](/metaweb-meta-metaweb) for a preview of the new front page. --[Pat](/user-patrick-tufts) 11:34, 17 Feb 2004 (PST)
