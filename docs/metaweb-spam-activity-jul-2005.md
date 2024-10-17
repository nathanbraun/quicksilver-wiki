
# Metaweb:Spam activity (Jul 2005)

From the Quicksilver Metaweb.

A spammer recently began making large numbers of "contributions" to Metaweb articles. The spammer is using several IP address ranges, and is quite agile within those.

I am considering locking the database for a few days to discourage this activity. Please post your thoughts and insights about how to deal with the spam here. --[Pat](/user-patrick-tufts) 13:32, 21 Jul 2005 (PDT)

 Update -- [User:WikiMinion](/user-wikiminion), an anti-spam bot, is now running on the Metaweb and doing a great job of finding and removing spam edits. --[Pat](/user-patrick-tufts) 23:07, 26 Jul 2005 (PDT)

Can we restrict edits to people with logins, or is that an option? Another idea: prevent edits if the POST to commit an edit doesn't have a referer that's equal to the edit URL for the page. - [DaveSeidel](/user-daveseidel) 13:34, 21 Jul 2005 (PDT)

 In our version of the MediaWiki software, it may be possible to restrict to only regisitered users, but as it's trivial to create an account, this is unlikely to be much of a barrier. We've had at least one registered spammer in the past.

 As for more referer based schemes, I agree that those would help, but we don't have resources to modify the MediaWiki code to support this.

Dave, I notice that you've been very active dealing with spam, and I appreciate this. If you would like admin access, let me know. This would give you the ability to add IP addresses to the block list. --[Pat](/user-patrick-tufts) 13:48, 21 Jul 2005 (PDT)

Both Dave and Mike should have my level of admin IMO. One thing we could do is allow new posters to have a *sandbox* to create articles in - that admins would move to protected locations. A 'vetting' process - [Sparky](/user-stsparky) 16:34, 2005 Jul 21 (PDT)

Those things that make you type a lot for letters into a textbox.. those are good human detectors. if make people fill out one of those after every post. unless they're logged in... and new users have to fill out one too.
their acronym is CAPTCHA <- its a terribly acronym. because i can never remember it. 

Thanks, guys. Patrick, I would certainly appreciate having admin access, to whatever level you think is appropriate. I'd like to continue to do what I can and that will help me to do so. - [DaveSeidel](/user-daveseidel) 17:19, 21 Jul 2005 (PDT)

 Dave, you've got sysop access now. This means you can block users and delete entries (as opposed to just reverting them). You can also lock and unlock pages. Use a light touch except when it comes to spam. --[Pat](/user-patrick-tufts) 17:37, 21 Jul 2005 (PDT)

 Thanks, Pat, will do. BTW, I'll be travelling for a couple of days starting tomorrow, but I should still be able to check in a couple of times. - [DaveSeidel](/user-daveseidel) 19:32, 21 Jul 2005 (PDT)


---


Are we winning? I'm protecting after I revert the articles - [Sparky](/user-stsparky) 21:35, 2005 Jul 24 (PDT)

Still protecting pages after reverting them when the spammer hits. Is this a problem for anyone? - [Sparky](/user-stsparky) 21:24, 2005 Jul 29 (PDT)


---


 Update the server please:
* Look at [Spam Blacklist,](/http-cvs-sf-net-viewcvs-py-wikipedia-extensions-spamblacklist) an extension for the server, and [Wikipedia's current blacklist.](/http-meta-wikimedia-org-wiki-spam-blacklist)
* Updating the server software in general might help the [automated solution guy I asked.](/http-www-nooranch-com-synaesmedia-wiki-wiki-cgi-wikiminion-fightingspameverywhere)
* The [SVN server](/http-svn-public-appliedminds-com-8000-repos-metaweb-metaweb) doesn't respond from anywhere I've tried.
 I'd suggest marking the bot crap as either minor changes or bot-made, & default to not showing whichever. -[Pronoiac](/user-pronoiac) 18:34, 21 Jul 2005 (PDT)

 Hi, this is my first post/edit. I've started reading the cycle for the second time and naturally came to metaweb. I noticed some rather odd images in many of the articles, is this the work of the vandal? I would second the sandbox concept - new edits would not be public until a review flag was set by an administrator. I'm suprised the mediawiki package doesn't already support this. I'll install it and have a look at the source. Please let me know if I can help with code changes, I could probably spare a few hours for it. [Monsoon](/user-monsoon) 03:31, 24 Jul 2005 (PDT)

### Information about the spammer


Add any information you have about the spammer here. The IP addresses they're using, and the links that they're posting (post as text rather than actual links, please)

If any of you are interested, you can do an ARIN search to learn the ISP associated with an IP address. Post this info here so we know who to talk to.

Here are the IP addresses we've blocked in July. I'm assuming most if not all of these are the same person or organization behind the recent porn ad spams:
This netblock is a prominent source, but the spammer(s) are using plenty of other IP addresses. 

**80.58.*.*:**

 09:37, 12 Jul 2005, Stsparky blocked 80.58.15.170
 22:01, 16 Jul 2005, Stsparky blocked 80.58.33.170
 20:22, 18 Jul 2005, Stsparky blocked 80.58.51.235
 09:37, 19 Jul 2005, Stsparky blocked 80.58.50.42
 20:27, 18 Jul 2005, Stsparky blocked 80.58.4.107 
 12:23, 20 Jul 2005, Stsparky blocked 80.58.9.237
 10:47, 20 Jul 2005, Stsparky blocked 80.58.4.42
 12:56, 20 Jul 2005, Patrick Tufts blocked 80.58.3.172
 13:25, 21 Jul 2005, Patrick Tufts blocked 80.58.23.235
 07:47, 21 Jul 2005, Stsparky blocked 80.58.50.107
 08:13, 20 Jul 2005, Stsparky blocked 80.58.41.44

**Other addresses:**

 20:21, 18 Jul 2005, Stsparky blocked 211.143.130.20 

 09:05, 5 Jul 2005, Stsparky blocked 205.188.117.65 
 08:14, 8 Jul 2005, Stsparky blocked 218.0.197.201 (Chinese Link Spammer Bot)
 09:53, 9 Jul 2005, Stsparky blocked 60.176.128.117 (Chinese Link Spammer Bot)
 08:12, 11 Jul 2005, Stsparky blocked 195.46.190.118 (commercial link spammer vandal)
 09:34, 12 Jul 2005, Stsparky blocked 68.152.252.74 (Vandalism and link spammer)
 09:34, 12 Jul 2005, Stsparky blocked 81.240.255.226 (vandalism and link spammer)
 09:37, 12 Jul 2005, Stsparky blocked 210.0.200.2 (vandalism and link spammer)

 11:37, 14 Jul 2005, Stsparky blocked 148.244.150.58 
 07:35, 16 Jul 2005, Stsparky blocked 85.250.217.251 

 22:02, 16 Jul 2005, Stsparky blocked 12.170.99.234 

```
    * 23:33, 17 Jul 2005, Stsparky blocked 221.237.200.127
    * 08:04, 18 Jul 2005, Stsparky blocked 195.87.69.26 

```



```
    * 20:22, 18 Jul 2005, Stsparky blocked 194.231.41.166
    * 20:26, 18 Jul 2005, Stsparky blocked 66.242.237.210

```


```
    * 09:37, 19 Jul 2005, Stsparky blocked 65.164.90.166

```


```
    * 09:37, 19 Jul 2005, Stsparky blocked 202.175.234.163
    * 09:40, 19 Jul 2005, Stsparky blocked 12.178.37.235

```


```
    * 17:34, 19 Jul 2005, Stsparky blocked 218.26.157.254
    * 08:13, 20 Jul 2005, Stsparky blocked 81.168.72.70
    * 08:14, 20 Jul 2005, Stsparky blocked 61.221.30.167 
    * 08:14, 20 Jul 2005, Stsparky blocked 212.117.152.70
    * 08:14, 20 Jul 2005, Stsparky blocked 200.10.148.133 
    * 08:17, 20 Jul 2005, Stsparky blocked 203.151.63.130 
    * 08:58, 20 Jul 2005, Stsparky blocked 210.120.60.148 
    * 08:58, 20 Jul 2005, Stsparky blocked 217.219.18.10
    * 10:47, 20 Jul 2005, Stsparky blocked 12.42.48.204 
    * 10:47, 20 Jul 2005, Stsparky blocked 211.138.91.21 

```


```
    * 12:22, 20 Jul 2005, Stsparky blocked 211.150.124.34

```


```
    * 12:31, 20 Jul 2005, Stsparky blocked 200.58.160.146

```


```
    * 12:39, 20 Jul 2005, Patrick Tufts blocked 12.42.48.204

```


```
    * 12:57, 20 Jul 2005, Patrick Tufts blocked 203.146.86.80
    * 12:57, 20 Jul 2005, Patrick Tufts blocked 80.58.2.44 
    * 20:59, 20 Jul 2005, Stsparky blocked 203.146.86.80 
    * 21:03, 20 Jul 2005, Stsparky blocked 66.239.253.66 
    * 07:47, 21 Jul 2005, Stsparky blocked 210.201.171.125
    * 07:47, 21 Jul 2005, Stsparky blocked 198.31.196.178
    * 07:49, 21 Jul 2005, Stsparky blocked 81.8.110.33
    * 07:50, 21 Jul 2005, Stsparky blocked 198.31.196.178
    * 10:51, 21 Jul 2005, Stsparky blocked 220.245.178.135
    * 10:52, 21 Jul 2005, Stsparky blocked 200.93.235.42
    * 13:22, 21 Jul 2005, Patrick Tufts blocked 80.58.42.170
    * 13:24, 21 Jul 2005, Patrick Tufts blocked 220.227.145.153
    * 13:24, 21 Jul 2005, Patrick Tufts blocked 210.212.144.14

```


```
    * 13:25, 21 Jul 2005, Patrick Tufts blocked 210.70.129.250

```


```
    * 13:33, 21 Jul 2005, Patrick Tufts blocked 80.16.191.106

```


---


Someone has posted a link to www.greenfairy.com on [Talk:Stephenson:Neal:Quicksilver:Qwghlm](/talk-stephenson-neal-quicksilver-qwghlm). [bsheryl](/user-80-137-232-3) 06:38, 3 Aug 2005 (PDT)bsherylak


---


### Proposal


Is there any reason why we can't just block off the entire 80.58.###.### and 220.245.###.### netblocks? These seem to have prevalent open relays. Whoever administers them is obviously either complicit or incompetent. What parts of the world do they cover and what companies own those netblocks?[Mike Lorrey](/user-mlorrey) 13:58, 6 Aug 2005 (PDT)


---


Do you have [nofollow](/http-en-wikipedia-org-wiki-blog-spam-nofollow) tags on external links? - [70.18.36.47](/user-70-18-36-47) 10:31, 20 Aug 2005 (PDT)
 No, and I don't know if our version of the Wiki software can use them. I'll inquire. It seems our spammer got bored or is taking a break - [Sparky](/user-stsparky) 13:48, 2005 Aug 20 (PDT)

### [Wikipedia: Link spam: nofollow](/)


In early 2005 [Google](/http-www-google-com) introduced [an HTML attribute](/http-googleblog-blogspot-com-2005-01-preventing-comment-spam-html) that disables the assignment of ranking credits for a particular link. This is a much easier solution that makes the improvised techniques above irrelevant. Most weblog software now comes with this enabled by default (and no option to disable it without code modification) adding the nofollow attribute to reader-submitted links:  

<a href="http://www.wiki.org/" rel="nofollow">Link</a>  

However, some weblog authors object to using the attributes, due to concerns over the motives for its introduction (the large amount of inter-linking between blogs makes search engine algorithms less accurate) and its effectiveness, since a spambot does not know whether its target is using 'nofollow' or not.


20060713.2237 see [http://c2.com/cgi/wiki?DelayedIndexing](/http-c2-com-cgi-wiki-delayedindexing) for how the OriginalWiki combats spamming
