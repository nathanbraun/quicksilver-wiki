
# Metaweb:FAQ

From the Quicksilver Metaweb.


This is a list of **Frequently Asked Questions** about the Metaweb. If you have a question and it is not answered here, post it on the [FAQ talk page](/metaweb-talk-faq).

## Isn't this redundant with Wikipedia?


No. See [Metaweb:An explanation of the similarities and differences between Wikipedia and Metaweb](/metaweb-an-explanation-of-the-similarities-and-differences-between-wikipedia-and-metaweb). [Metaweb:governance ideas](/metaweb-governance-ideas) are also necessarily somewhat different, if only because it is not running in 40 languages at once.

## Is this software downloadable?


Yes. We are running the GPLed software MediaWiki, a PHP/MySQL-based WikiWiki, the same software as the [Wikipedia](/http-www-wikipedia-org). The software is on Sourceforge at [wikipedia.sourceforge.net](/http-wikipedia-sourceforge-net).

## Can a non-technical user run this software himself/herself?


Almost certainly not. It relies on MySQL and has numerous flakiness problems that will prevent a non-technical user from keeping it going reliably.

The evolution of a [wikitext standard](/wikitext-standard) may give users an option of different [wiki software](/wiki-software) to read and edit [open content](/open-content) through, eventually.

## What's the server setup that the Metaweb is running on?


The server is a HP/Compaq DL360 G2 with dual Pentium III processors running at
1.4 Ghz with 1 Gbyte of memory. It has two 72 Gbyte disks which are mirrored
to each other in case either one fails.

Software wise, we're running the latest RedHat 9 with all security RPMs
applied, using MySQL's MySQL 4.0.15 RPMs and our self-compiled Apache 1.3.28
and PHP 4.3.3.

## What internet connectivity do we have?


We're on a T1, so be nice to us. Our php.ini has
zlib.output\_compression turned on, which will reduce bandwidth usage.

## Do you have web site statistics?


See [Special:Statistics](/special-statistics) for numbers related to Metaweb website and backend 
database.

See [Metaweb Orca
Statistics](http-www-metaweb-com-statistics-orca-procallator) for statistics regarding the physical server the Metaweb is on.
This shows statistics such as CPU, memory, IO, swap usage and much more.
