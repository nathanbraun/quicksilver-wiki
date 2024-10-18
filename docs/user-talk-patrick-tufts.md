
# User talk:Patrick Tufts

From the Quicksilver Metaweb.

Note: older threads moved to [User talk:Patrick Tufts/Nov 2003](/user-talk-patrick-tufts-nov-2003), [User talk:Patrick Tufts/Feb 2004](/user-talk-patrick-tufts-feb-2004), and [User\_talk:Patrick Tufts/Jun 2005](/user-talk-patrick-tufts-jun-2005)

Can we do something about the serial porn spammers? - [Sparky](/user-stsparky) 11:39, 2005 Jul 14 (PDT)
Pat - the porn spambot is getting worse. Can you notify the various ISPs the jerk is using? -[Sparky](/user-stsparky) 20:37, 2005 Jul 18 (PDT)
 I'd guess there are open proxies being used here. I'm going to ask someone with an anti-spam bot to watch this. -[Pronoiac](/user-pronoiac)

 The current round is very agile - hopping among lots of IP addresses in a few address ranges. It's unclear to me whether these are open proxies or forged IP addresses. Either way, I emailed one of the ISPs associated with the IP addresses and gave them documentation of the abuse. We'll see what happens. --[Pat](/user-patrick-tufts) 13:55, 21 Jul 2005 (PDT)

 Hi, I am the operator of the WikiMinion anti-spam bot. Pronoiac asked me to add this wiki to list of wiki's automatically kept clean of spam by WikiMinion. It took me a bit of time to modify the code to support the ancient version of MediaWiki used by Metaweb, but I think its ready. I don't want to unleash the bot on the wiki without first obtain the permission of either an admin or the Metaweb community. Does anyone have objections? --[RichardP](/user-richardp) 17:59, 22 Jul 2005 (PDT)

 Hi Richard, it sounds interesting. I'd like to learn more about Wikiminion before we run it here. Can you tell me, briefly: 1) how it works and what it does, and 2) what other wikis are using it (esp, is Wikipedia running it?), and, 3) what sort of control do we have over its behavior? (does it have a user interface or a way for taking feedback, and how do we stop it if it behaves badly?) --[Pat](/user-patrick-tufts) 19:08, 22 Jul 2005 (PDT)

 Sure Patrick, your caution is perfectly understandable. 1) WikiMinion examines edits and reverts those made by spammers. It uses a heuristic and relies on a large database of known spammer domains and IP address, as well as some additional smarts along the lines of identifying spam by noticing multiple identical insertions across many wikis. 2) WikiMinion has been in operation for about eight months and is in use on approximately 50 wikis. Examples include UBCWiki, FSF's GnuRadioWiki, KayakWiki, Metafilter's wiki, etc. 3) WikiMinion always edits using a user name (for Metaweb I've configured it to use 'WikiMinion'), so you can always ban that user if you want to stop it and I can't be reached. It also honors the robots exclusion protocol, so you can also use robots.txt to tell WikiMinion to stay away. Furthermore, it always operates from the same IP, so you could, if you wished, ban it by IP address using MediaWiki or at your router (although if you do that, you'd also block communication with me). 5) I'll send you an e-mail at your zippy address so that you'll have my e-mail and phone number. --[RichardP](/user-richardp)

 I'd like to give it a trial run next week. Would you be able to turn it on just for Monday so we can see how it does? --[Pat](/user-patrick-tufts) 20:14, 22 Jul 2005 (PDT)

 Sure, I'd be happy to do so. Has the Metaweb community managed to stay on top of the latest spam, or has fallen behind in cleaning up? If so, another possibility would be for me to make a single run today against the current pages rather than having WikiMinion begin periodic examination of new edits. That would give you a chance to see what it looks like. --[RichardP](/user-richardp) 20:32, 22 Jul 2005 (PDT)

 We've stayed on top of it, though I'm sure some slipped through. I'd like to try a single run Monday to see how it works out. I very much appreciate your offer. One more question -- how do you update WikiMinion's ban list -- do you take additions? --[Pat](/user-patrick-tufts) 02:09, 23 Jul 2005 (PDT)

 OK, Monday it is. Let me know if you'd like me to start sooner. With regards to updates, in the normal course of its activity WikiMinion assembles a report documenting suspected spam edits and the associated metadata (IP, host, user, linked domains, etc.) that it would like to add to its spam corpus. In theory WikiMinion could run completely closed-loop, but currently I investigate and confirm each update that WikiMinion intends to make. I can also manually add a entry, but it is very rare for me to find it necessary to do so, WikiMinion usually notices new spammers before I do. In order to make an addition, just manually revert a spam edit that WikiMinion missed - that will cause WikiMinion to bring the new spammer to my attention. --[RichardP](/user-richardp) 10:29, 23 Jul 2005 (PDT)

 Richard, this is GPL code, right? Can you give us a link to the source? Pat, I'd suggest a little code review, just to get familiar with it and see what it does. I'll be back home Sunday night, so next week I can volunteer some time to give it a read through and report back. - [DaveSeidel](/user-daveseidel) 19:46, 22 Jul 2005 (PDT)

 Dave, sorry, I haven't published the code. It originally my intention to release it, but a prominent wiki administrator contacted me privately and asked me to not do so. He was concerned that, if released, WikiMinion's code could be used to write much more capable spam bots. There is a discussion of the pros and cons of the release of wiki bot code on Meatball wiki. --[RichardP](/user-richardp) 20:32, 22 Jul 2005 (PDT)

 Richard, I understand. I'll take a look at the Meatball wiki. - [DaveSeidel](/user-daveseidel) 17:44, 23 Jul 2005 (PDT)

 In preparation for starting WikiMinion's evaluation period on Monday, this morning I had WikiMinion do a "passive" check of the existing pages listed in [Special:Allpages](/special-allpages) for spam (normally WikiMinion only checks new edits). WikiMinion only found four pages with spam: [Drive](/drive), [Drake](/drake), [Jean-Jacques\_Rousseau](/jean-jacques-rousseau), and [Vandalism\_Archive\_2005-03-29](/vandalism-archive-2005-03-29). I see that [User:Stsparky](/user-stsparky) has already deleted the first two. The last isn't actually spam - it's just a discussion of spammers using live links. I'm going to neuter those live links, no reason to give spammers the benefit of Metaweb's PageRank. --[RichardP](/user-richardp) 12:38, 24 Jul 2005 (PDT)

 As of this morning, WikiMinion is now periodically visiting Metaweb and reverting spam edits. See WikiMinion's [user contributions](/http-www-metaweb-com-wiki-wiki-phtml-title-special-contributions-target-wikiminion) to examine a list of reverts performed by WikiMinion. --[RichardP](/user-richardp) 07:05, 25 Jul 2005 (PDT)

 Thanks, Richard. I'm keeping my fingers crossed that it works out well. One note for admins reading this -- when WikiMinion reverts spam, we'll still need to consider blocking the IP address. --[Pat](/user-patrick-tufts) 10:04, 25 Jul 2005 (PDT)

 I hope it works out well for the Metaweb community as well. As a side note, WikiMinion also has the ability to automate additions to the IP blocklist - if enabled, it will automatically blacklist those IP addresses that WikiMinion notices have become persistent sources of spam on more than one wiki. Naturally, due to an entirely reasonable caution, only a fraction of the wiki's that WikiMinion patrols have chosen to take advantage of this feature. I just wanted to let you know that the feature is available if blocking spammer IP addresses manually becomes an unacceptable burden. --[RichardP](/user-richardp) 10:20, 25 Jul 2005 (PDT)

 Over the course of the last 12 hours or so I've noticed that most of the spam inserted into Metaweb has been reverted by a Metaweb user before WikiMinion got around to it. In order to avoid placing an undue load on a wiki WikiMinion uses an exponential back-off algorithm to determine how frequently to check a wiki, in the case of Metaweb this means that under normal conditions Metaweb will be checked for spam approximately every two hours. Should I consider increasing the frequency? --[RichardP](/user-richardp) 18:17, 25 Jul 2005 (PDT)

Yes. BTW: Is WikiMinion capable of recognising chinese character spam? The stuff I just reverted was all in chinese. The chinese spammers history tends to edit recent legitimately edited pages, so their activities can interfere with legit work. [Mike Lorrey](/user-mlorrey) 18:31, 25 Jul 2005 (PDT)

WikiMinion has no trouble with non-roman characters. For example, for the spam edits you just reverted WikiMinion is very very certain they were spam: they originated from an IP address that in the 100,000 or so edits WikiMinion has examined has only been the source of spam and never the source of legitimate edits, the domains in the links have only been used by spammers and never by legitimate editors, and the text content of the edit contains Chinese keywords that frequently appear in spam. If you hadn't reverted them, WikiMinion most certainly would have done so. --[RichardP](/user-richardp) 19:09, 25 Jul 2005 (PDT)

 Richard, if Wikiminion only gets the pages touched since it last visited, and so doesn't generate a lot of requests, then I have no problem with it checking hourly. Do you have an estimate for how many pages it requests per hour? --[Pat](/user-patrick-tufts) 19:05, 25 Jul 2005 (PDT)

 Pat, if WikiMinion's database has been updated since the last visit it doesn't check just the edits since the previous visit, it looks for spam in the most recent version of all pages modified in the preceding 24 hours. It does this because a database update may cause an edit that was considered legitimate on the previous pass to now be classified as spam. The database is updated often enough, that more often then not, WikiMinion examines more than the very latest edits. I checked the logs, in the last 12 hours or so WikiMinion has requested approximately 160 pages, or a little over 13 per hour. Doubling the rate of its visits would double its requests. --[RichardP](/user-richardp) 19:22, 25 Jul 2005 (PDT)

 Hmm... There doesn't appear to be any established precedent on Metaweb for a mechanism by which a regular user can request a page be deleted by someone with administrative privileges. Any one have any objections with marking all such pages with a *DeleteThisPage* page reference, that way admins can quickly visit the *DeleteThisPage* page and click on *What links here* to see all of the pages awaiting deletion? I've noticed a few very old pages that users have asked to be deleted. --[RichardP](/user-richardp) 09:00, 26 Jul 2005 (PDT)



---


Hi, please have a look at [http://www.metaweb.com/wiki/wiki.phtml?title=Stephenson:Neal:Cryptonomicon:401:HEAP%3F(Alan\_Sinder)](/http-www-metaweb-com-wiki-wiki-phtml-title-stephenson-neal-cryptonomicon-401-heap-3f-alan_sinder) and revert the pr0n spam changes. I don't know how to backout a complete commit within a wiki ...

 Done. And, see [Revert](/revert). - [Pronoiac](/user-pronoiac)



---



Patrick, is there any way we can restrict edits to people with logins, or is that an option? Another idea: prevent edits if the POST to commit an edit doesn't have a referer that's equal to the edit URL for the page. It's sure tiresome cleaning up after this asshole. - [DaveSeidel](/user-daveseidel) 13:33, 21 Jul 2005 (PDT)

 The only way at the moment to take care of this is to upgrade to a newer version of the Mediawiki software. I'm up for other suggestions. One thing I'm considering is turning off write access to the db for a few days to encourage the spammer to move along --[Pat](/user-patrick-tufts) 13:36, 21 Jul 2005 (PDT)



---


I'd also like to see if we can remove all the provocative summary comments from the database. I am concerned that parental control software will block the Metaweb due to the language of these comments.[Mike Lorrey](/user-mlorrey) 12:37, 23 Jul 2005 (PDT)
 Mike is worthy. - [Sparky](/user-stsparky) 00:45, 2005 Jul 26 (PDT)



---


I've protected some pages but the spambot has a workaround to defeat that I think. I'll email you. - [Sparky](/user-stsparky) 23:18, 2005 Aug 3 (PDT)


---


Pat? Could you turn off write access to non-registered users for a day or two? - [Sparky](/user-stsparky) 09:06, 2005 Sep 12 (PDT)

 Unfortunately, I only have the blunt instrument of "turn off all writes." Sorry. --[Pat](/user-patrick-tufts) 23:26, 15 Sep 2005 (PDT)


---


Pat? I have no idea as to how to archive any of this? Can you point me in a direction? - [Sparky](/user-stsparky) 10:29, 2005 Sep 14 (PDT)

 There are two useful programs for archiving web sites. Neither preserves the wikimarkup, but both are better than not having the content at all. The first is wget, which is a command line utility (part of Linux, and available for Windows in the free Cygwin system). There's also a web crawler caller Heretix or Heretrix from the Internet Archive. --[Pat](/user-patrick-tufts) 23:26, 15 Sep 2005 (PDT)


---


Seems we're seeing spammers again. - [Sparky](/user-stsparky) 13:13, 2005 Dec 20 (PST)


## Patrick, did you go to EO Smith?



Patrick,

Did a quick google search for you. We are trying to gather people for the EOS anniversary. Drop me a note at ken@ken.net

ken snyder

 Hi Ken. You've got the right one. I'll send you an email. --[Pat](/user-patrick-tufts) 05:49, 27 Jan 2006 (PST)
### be back annotating soon


Curious if TiddleyWiki is something we could use here. I was working on another project, which is now drooling on me.- [Sparky](/user-stsparky) 01:12, 2006 Feb 14 (PST)

 I haven't used TiddleyWiki. What do you like about it? (and an ever-present soft towel is your friend) --[Pat](/user-patrick-tufts) 08:59, 23 Feb 2006 (PST)

 [TiddlyWiki](/http-www-tiddlywiki-com) example: [The Tough Guide to the Singularity](/http-www-accelerando-org-static-toughguide-html). It's nifty, I could use it as a personal wiki, and it has features I would love to incorporate into another wiki, but as it is, it scales badly... - [Pronoiac](/user-pronoiac) 10:27, 23 Feb 2006 (PST)

## Royal Society Minutes


PATRICK! We need Neal to be a WHITE KNIGHT. Please read:

[[1]](/http-www-guardian-co-uk-science-story-0-1705687-00-html)

If you would please forward this information as immediately as possible to Neal. 

520 pages of Royal Society minutes discovered -- but they're being auctioned and may well end up in a sealed private collection! We need to intercept.
([User:Ankhes](/user-ankhes) 05:12, 12 Feb 2006 (PST))

 Alert noted and forwarded. --[Pat](/user-patrick-tufts) 05:00, 23 Feb 2006 (PST)


---


We're being clobbered by specific spammers who leave spoor. Can they be blocked? - [Sparky](/user-stsparky) 14:26, 2006 Jun 2 (PDT)

### Spamming


You seem to have a serious spamming problem. At Wikinfo we put in a blacklist which keeps many spam addresses from being saved. See [http://wikinfo.org/wiki.php?title=GetWiki:Blacklist](/http-wikinfo-org-wiki-php-title-getwiki-blacklist) Contact Proteus at Wikinfo User talk:Proteus there at Wikinfo, maybe he can help you set this up. [Fred Bauder](/user-fred-bauder) 18:08, 19 Jun 2006 (PDT) (Fred Bauder)
 Pat? Will that work? - [Sparky](/user-stsparky) 13:58, 2006 Jun 22 (PDT)
### Any guidelines


Any ideas at this point? - [Sparky](/user-stsparky) 19:38, 2006 Jul 05 (PDT)
