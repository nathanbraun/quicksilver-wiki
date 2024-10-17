
# Metaweb:Namespaces and names

From the Quicksilver Metaweb.

Discussion of **namespaces** to prevent accidental collisions between fiction, reality, etc. moved here from [Quicksilver and reality](/quicksilver-and-reality). --[Patrick](/user-patrick-tufts) 12:08, 17 Sep 2003 (PDT)


---



I have a feeling that in order to address the question of novel-specificity in entries here, we need some sort of namespace mechanism. Quicksilver:CABAL is related to CABAL in some ways, and different in others. In order to have maximum utility as an annotation site, entries will have to be able to be very specific to a particular work. In order to have maximum utility as a general reference, entries will also have to be able to be general, and the distinction will have to be abundantly clear. Namespaces are one way to do that.

We could implement namespaces by convention, if we choose--or we could reify them by editing the code. I think that we should do it by convention. We could also extend this convention to do entries linked to page numbers, as in Quicksilver:p31:Frobnitz Industries. 

I just noticed that some pages here already use single colons pretty much as I was imagining, so I'm guessing that there is already some support for namespaces or namespace-like entities in this software.

--[Jeremy](/user-jeremybornstein)

 Yes, the default wikipedia configuration includes at least five namespaces: the main namespace (no prefix), User (user pages, i.e. [User:Patrick Tufts](/user-patrick-tufts)), Talk (the parallel discussion pages, i.e. [Talk:CABAL](/talk-cabal)), Wikipedia (Meta-discussions about the site), and Special (maintenance and administration, i.e. [Special:Allpages](/special-allpages)). The config file comments suggest that we can add more. --[Patrick](/user-patrick-tufts) 08:04, 15 Sep 2003 (PDT)

 Neal, what do you think about this change? I volunteer to make the change if there is no dissent. --[Jeremy](/user-jeremybornstein) 21:05, 15 Sep 2030 (PDT)

 It'll be necessary to do something like this anyway when subsequent volumes of the series are published, otherwise we'll have namespace collisions between page n of Quicksilver and page n of The Confusion. Note that not all book titles are one-word, so we need to check whether spaces are permitted in these things, and if not, we need a convention for that--perhaps using underscores instead of spaces, or something. When you say that you volunteer to make the change, what do you have in mind? Editing the existing pages one by one, or writing some code to do it?--[Nealstephenson](/user-nealstephenson) 22:36, 15 Sep 2003 (PDT)

 Spaces seem to be permitted in page names, so I don't think that's an issue. I imagine that tedious manual editing is really the only way to do it, unless I have access to the back end machine and can interact with the data structures in a more direct fashion. Patrick? --[Jeremy](/user-jeremybornstein) 11:20, 16 Sep 2003 (PDT)

 Spaces are fine in page names and usernames. (If anyone would like me to move their username to a spaced version, let me know). The wikipedia software has a simple concept of namespaces (see my note above) that I now suspect would require hacking to make easily extensible. 

 Whatever method we use to indicate the namespace of an article, I recommend that it be a short text string to make it easier for editors. This software is the current, imperfect vehicle for the Metaweb. What we create or move to in the future will have, for instance, form support for things like namespace and author and more key fields for tagging documents and relationships.

 For now, what do you think of a "QS" prefix for Quicksilver articles while we design and build a more general system?

 Jeremy (and anyone else interested in digging), would you have time to investigate the wikipedia software documentation and see how much of this the namespace mechanism can handle? Useful start points are [[1]](/http-meta-wikipedia-org-wiki-mediawiki-architecture) and [[2]](/http-meta-wikipedia-org-wiki-mediawiki)

 The MySQL backend for the Wikipedia software appears to use a one byte value for the namespace, which probably means that we can have over a hundred of them at least (and up to somewhere around 250 at maximum, since there are some already existing). --[Jeremy](/user-jeremybornstein) 21:15, 16 Sep 2003 (PDT) (This isn't indenting properly. Can anyone see what I'm doing wrong?)

 Also, I'll ask about ssh access. --[Patrick](/user-patrick-tufts) 12:11, 16 Sep 2003 (PDT)

 How about "QS" for the first volume (Quicksilver), TC for the second (The Confusion), SW for the third (System of the World). This is pretty crude and would lead to collisions very soon if the thing got much bigger, bum ofut as Patrick points out, it might migrate to a different platform later. --[Nealstephenson](/user-nealstephenson) 17:18, 16 Sep 2003 (PDT)

 Writing an article is enough of a major step that I don't think it unreasonable to spell out the volume names. (Is *System of the World* what used to be known as *The Juncto*?) I realize that I may be off the deep end here, but the scheme I'd really prefer is one like [Neal Stephenson:Quicksilver:p256:Caravanserai](/neal-stephenson-quicksilver-p256-caravanserai) --[Jeremy](/user-jeremybornstein) 21:02, 16 Sep 2003 (PDT)

 Agreed that making the author's name first in the namespace will be the most general way of doing it; this makes it far easier to put in annotations of many different books by many different authors. If we carry that to its logical conclusion, though, the author's family name should come first, followed by the given name, thus: Stephenson:Neal:Quicksilver:p256:Caravanserai.

 I like this. It occurs to me that namespaces might not be nestable. I will investigate the Wikipedia software to see what our options are in this regard, unless Patrick already knows. --[Jeremy](/user-jeremybornstein) 11:33, 17 Sep 2003 (PDT)

 There are Namespaces, and then there are namespaces. The MediaWiki software (aka the wikipedia engine) has 7 preconfigured Namespaces. These are represented in the underlying MySQL database. MediaWiki can do rather unexciting things with these Namespaces, like allow the user to select which ones they want to search over, and what default background color is associated with pages in each space. A page's Namespace is determined by it's prefix. [User:Patrick Tufts](/user-patrick-tufts) is different than [Patrick Tufts](/patrick-tufts) is different than [Metaweb:Patrick Tufts](/metaweb-patrick-tufts).

 However, it really doesn't matter to us whether the MediaWiki recognizes a page as being in a Namespace, because the software lets us put any text in these page names. As long as two pages have different titles, they are distinct entities. So I can say [Quicksilver: page annotations](/quicksilver-page-annotations) and [Cryptonomicon: page annotations](/cryptonomicon-page-annotations) and these are two separate pages. There's nothing special about how I named these. I could just as well have used [QS:page annotations](/qs-page-annotations) or [page annotations/quicksilver](/page-annotations-quicksilver) or whatever other convention we choose.

 Now to nesting. The MediaWiki's Namespaces are not nestable, but our namespaces can be, again because we can do whatever we want in the titles. --[Patrick](/user-patrick-tufts) 12:04, 17 Sep 2003 (PDT)

 To answer your question about volume names, the second volume will be entitled *The Confusion* and will contain two books, *Bonanza* and *Juncto*. The third volume will be entitled *The System of the World* and will contain either two or three books, none of which has been seen yet by anyone save myself.

 At the risk of carrying this discussion of article titles to the point of absurdity, I would like to add one remark of a basically aesthetic nature, which is that I'm getting a little tired of seeing my name in parentheses at the end of the title of every single page that I have written. If you look at the list of all annotations by page number, this gets a bit monotonous. We might opt for a convention in which the default page author is assumed to be the author of the book. Annotations posted by other people might then have the contributor's name appended to the page title. Or perhaps we can come up with some other solution that's even better. Suggestions welcome--[Nealstephenson](/user-nealstephenson) 21:35, 16 Sep 2003 (PDT)

 I think the best option would be one which would show special formatting for titles of (and links to) articles written by the book's author. I expect that this could be done dynamically based on a naming convention we assign, such as a standard suffix (akin to " (Neal Stephenson)" but the same for every author: perhaps just " OFFICIAL".

 How willing are we to hack Wikipedia in any serious fashion? At least some of the mechanisms that we're evolving really want to be supported in code. --[Jeremy](/user-jeremybornstein) 11:33, 17 Sep 2003 (PDT)

 Pretty willing. There is a lot we can do by modifying this software. For instance, I think we could auto-fill content or add author names to entries. I spoke to [Blair](/user-blair), who is the administrator setting up the public site. He says the machine running the Metaweb PHP is going to live in a DMZ, meaning outside coders should be able to log in to it. The original plan was to use an existing machine that was on our private net, but that would have been inaccessible to outside coders. I'm lobbying for you (Jeremy) to get access. --[Patrick](/user-patrick-tufts) 17:18, 17 Sep 2003 (PDT)
