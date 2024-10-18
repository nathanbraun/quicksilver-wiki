
# Metaweb:An explanation of the similarities and differences between Wikipedia and Metaweb

From the Quicksilver Metaweb.

While the Metaweb runs on MediaWiki, the same software as Wikipedia, and so has a similar appearance, the two projects have different philosophies and goals. This page is a summary of the major differences.


## Neutral point of view only (W) vs essays and neutral point of view (M)


The Wikipedia has a policy that all entries must be written from a neutral point of view. By contrast, the Metaweb contains authored content, which can be written from a point of view. 

### Authored pages


[Authored content](/metaweb-authored-entries) is any entry that is tagged with the author's name. In the current interface, this means the title of the entry includes the author's name (e.g. [The Vigenère Cipher (Talith)](/the-vigenère-cipher-talith)).

### Intermediate pages


[Intermediate pages](/metaweb-intermediate-page) serve as rotaries leading to multiple entries on a given topic. An intermediate page must be written from a neutral point of view, but may link to [authored essays](/metaweb-authored-entries) that reflect individual viewpoints and writing styles. 

Intermediate pages may link to parallel entries on the same topic. For example, if one were trying to explain some concept from physics, it might make sense to have one version that was written for people who don't know a lot of math, and a different (probably shorter!) version written for people who know calculus.

An intermediate page may contain a community section. It is called a [community entry](/metaweb-community-entry) because anyone from the Metaweb "community" may edit it. 

The community section is typically a simple introduction to the topic, so people reading the intermediate page have some starting point to work from. The community section is the Metaweb equivalent of a Wikipedia entry.

In the future, we may extend the concept of authorship to groups of writers. But for the moment, we're keeping the model simple for two reasons: 1) we want to see how it works in the basic single-author case, and 2) the current UI does not display authors in a way that scales (in other words, stuffing multiple author names in the title would get ugly fast).

## Single entry per topic (W) vs multiple entries per topic (M)


The Wikipedia does have multiple entries for a given topic, but only where there is a name collision (for instance, it might contain a *disambiguation page* for Cambridge that links to entries for Cambridge, Massachusetts and Cambridge, England). The Metaweb takes this a step further and allows for multiple parallel entries on the same topic (for example, two entries on Cambridge, England by different authors). See the intermediate page discussion above for more on this.

## All entries collaboratively edited (W) vs typical entry edited only by author (M)


On the Metaweb, authored entries should be edited by the author only. Well, that's not entirely true. It is acceptable to add links by bracketing some text so that readers can follow links to concepts mentioned in the entry, but that's it. It is not acceptable to modify another author's content.

That said, the current software does not enforce this. Instead, this is an editorial policy.

It is acceptable to make changes to an authored entry's *talk page* via the "discuss this page" link.

## Goal: encyclopedia (W) vs goal: structured, typed-link database (M)


The Wikipedia knows what it is. It is an encyclopedia. 

The Metaweb is an experiment. We want to create something initially useful enough that people will contribute knowledge to it, but one of our long-term goals is to try out new ways of presenting instructive and useful information to users. The current incarnation of the Metaweb is our first step in that direction. 

For more on typed links see [Metaweb:Semantics](/metaweb-semantics).
