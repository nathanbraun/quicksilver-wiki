
# Metaweb talk:So long, and thanks for all the fish

From the Quicksilver Metaweb.

Ouch. Any idea as to when? How much storage would be needed to store all the articles? - [Sparky](/user-stsparky) 09:06, 2005 Sep 14 (PDT)

Pat, you suggest wget as a archival mechanism, unfortunately that would not preserve the wiki markup. Furthermore it would involve a huge effort to retype the content and formatting into a new site. Is it possible to upgrade the site to a newer version of MediaWiki and then making use of the [MediaWiki export functionality](/http-meta-wikimedia-org-wiki-help-export) to export the site content to an XML file that can be imported into a new MediaWiki host? That would greatly ease the transition to another host. -- [RichardP](/user-richardp) 16:02, 14 Sep 2005 (PDT)

 Unfortunately, there's no chance of upgrading the site's software. There is a *slim* chance that I could do a database dump of the site, though, if someone sent me the (presumably SQL) commands I would need to type. --[Pat](/user-patrick-tufts) 23:22, 15 Sep 2005 (PDT)

To dump the contents of MySQL to a backup file, try the following at the command line:

mysqldump --opt --all-databases > backup-file.sql

Undoubtedly the file produced will be huge.

I'm not sure how useful that would be when trying to move to a new MediaWiki host, since I 'm positive the database format for MediaWiki has changed (MediaWiki includes migration tools, but they'd be almost impossible to use on another host as opposed to running the migration tools on the current MetaWeb installation).

As I've mentioned to [Sparky](/user-stsparky), if upgrading the wiki to support exporting the wiki data is impractical, I'm willing to do a remote "poor man's export." To do so I would write some code, combine it with the code I developed for [WikiMinion](/user-wikiminion), and crawl the entire MetaWeb wiki grabbing the wiki markup (by invoking the edit action and grabbing the markup from the edit box) for each page and saving each page to a separate file. This would preserve the content and wiki markup, but not the page histories. I could then create a zip archive and distribute it to Sparky or anyone else willing to hold onto an archived copy of the MetaWeb wiki. Similarly, I'm willing to do the reverse, namely a "poor man's import" if a new host for the wiki is found. 

However, to do so I'd need two things: permission from you Patrick to do the crawl (since it is may consume considerable resources from the web server) and permission to use an account with admin privileges (since this technique relies on being able to invoke the edit pages and there are quite a few protected pages for which only an admin can view the edit page). -- [RichardP](/user-richardp) 07:44, 16 Sep 2005 (PDT) 

 **Newsflash** -- our system administrator created a db dump of the Metaweb. I am downloading it now. It is huge -- 200MB -- and I need to review it to make sure it has all the data (and no user passwords). But it sounds like I'll have a backup that I can put on line for anyone to download. I will keep you informed.

 Richard, I don't think you'll need to crawl the wiki, but just in case, I'll make you a sysop today. We're on a T1, so please don't hammer the site. If you could get the main articles first, I think that's the highest priority. Ping me in email on Monday and I'll let you know if the db dump has what we want. --[Pat](/user-patrick-tufts) 17:19, 16 Sep 2005 (PDT)

 OK. I'll crawl Metaweb this weekend and keep bandwidth limits in mind (details sent to you via e-mail). By the way, do you know what Metaweb's monthly bandwidth consumption is? If not, can you ask Metaweb's system administrator? It would be very handy to know when trying to choose an appropriate hosting plan at an alternate provider. -- [RichardP](/user-richardp) 18:19, 16 Sep 2005 (PDT)

 In advance of doing a crawl, I'm going to delete the pages created by the latest spammer. I'm not sure how many there are, but there are more than 500. -- [RichardP](/user-richardp) 13:02, 17 Sep 2005 (PDT)

 (it turns out there were 854 of the UserTalk:n.n.n.n pages.) -- [RichardP](/user-richardp) 13:41, 17 Sep 2005 (PDT)
Pat? Would it be possible to keep the Metaweb at Applied Minds locked as a archive until Mike, Richard and I figure out a place to host it and keep it running as a Wiki? - [Sparky](/user-stsparky) 08:17, 2005 Sep 15 (PDT)

 For the moment, all that's going is the link from the front page on metaweb.com to the wiki. I do not know how long the wiki will be up -- it could go down tomorrow, or it could stay up for some time. I wouldn't count on the latter, though. --[Pat](/user-patrick-tufts) 23:22, 15 Sep 2005 (PDT)

I would be happy to offer any hosting you need. I have several dedicated servers, and am currently on my third pass through the Baroque Cycle ;) Pls let me know. [Monsoon](/user-monsoon) 04:51, 20 Sep 2005 (PDT)


---


This would a good place to make note of progress. - [Sparky](/user-stsparky) 09:02, 2005 Oct 1 (PDT)


---


Just getting to the end of System of the World and thought I'd have a quick catch up with this wiki. Horrified to think it might just disappear!! Hope someone can host it on another server.

I'm not an expert, but one thought I had about preserving the Wiki in some form was converting the recent database dump mentioned above to a TomeRaider 3 file using the script by Erik Zachte - details at [http://members.chello.nl/epzachte/Wikipedia/ProcedureTR3.html](/http-members-chello-nl-epzachte-wikipedia-proceduretr3-html) It says it will work with other MediaWiki databases so maybe it will work with the Metaweb? It basically preserves a snapshot of the Wiki with the internal links intact and can also include images. I have the exported TomeRaider file of the Wikipedia (approx 900MB) on my Pocket PC PDA - very cool. It would be great to have the Metaweb on my PDA while I'm reading Neal's books on the London underground! But the main reason would be to keep this superb content available! - Iain C 18:00, 2005 Oct 21 (GMT)
