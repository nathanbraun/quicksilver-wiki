
# Metaweb:How to edit a page

(Redirected from [Metaweb:How does one edit a page](/metaweb-how-does-one-edit-a-page))


## Introduction


The Metaweb is a WikiWiki, meaning that anyone can easily edit any article and have those changes posted immediately. This page is the reference for **Wiki markup**. 

You may also want to learn about:
* [How to start a page](/metaweb-how-to-start-a-page)
* [How to use tables](/metaweb-how-to-use-tables)
* [Naming conventions](/metaweb-naming-conventions) for how to name articles themselves
* [Authored entries](/metaweb-authored-entries) for when you want to create articles that should be attributed to you alone
* [Intermediate pages](/metaweb-intermediate-page) for linking articles on the same topic together
* Preferred layout of your article at [Guide to Layout](/metaweb-guide-to-layout)
* Style conventions in the [Manual of Style](/metaweb-manual-of-style)


It's very easy to edit a Wiki page. Simply click on the "**Edit this page**" link at the top or bottom (also on the sidebar) of a Wiki page to change the page itself, or click on "**Discuss this page**" link and then on "Edit this page" to write on the corresponding [talk page](/metaweb-talk-page). This will bring you to a page with a text box containing the editable text of that Wiki page.

Then type away, write a short edit summary on the small field below the edit-box and when finished press "Save". You can also preview your changes before saving if you like. Depending on your system, pressing Enter while the edit box is not active (there is no typing cursor in it) may have the same effect as pressing Save.

## Minor edits


When editing a page, a logged-in user has the option of flagging the edit as a "minor edit". When to use this is somewhat a matter of personal preference. The rule of thumb is that an edit of a page that is spelling corrections, formatting, and minor rearranging of text should be flagged as a "minor edit". A major edit is basically something that makes the entry worth relooking at for somebody who wants to watch the article rather closely, so any "real" change, even if it is a single word is a major edit. This feature is important, because users can choose to *hide* minor edits in their view of the Recent Changes page, to keep the volume of edits down to a manageable level.

The reason for not allowing a user who is not logged in to mark an edit as minor is that vandalism could then be marked as a minor edit, in which case it would stay unnoticed longer. This limitation is another reason to log in.

## The wiki markup


In the left column of the table below, you can see what effects are possible. In the right column, you can see how those effects were achieved. In other words, to make text look like it looks in the left column, type it in the format you see in the right column.

You may want to keep this page open in a separate browser window for reference. If you want to try out things without danger of doing any harm, you can do so in the [scratchpad](/metaweb-scratchpad).


### Sections, paragraphs, lists and lines




| What it looks like | What you type |
| --- | --- |
| 
Start your sections with header lines:
New Section
Subsection
Sub subsection
Sub-sub-subsection

 | 
```

=New Section=

== Sub section ==

=== Sub-subsection ===

==== Sub-sub-subsection ====

```
 |

| 
A single newline
has no effect on the layout. 
These can be used to separate
sentences within a paragraph.
Some editors find that this aids editing
and improves the *diff* function.

But an empty line
starts a new paragraph.
 | 
```
A single newline
has no effect on the layout. 
These can be used to separate
sentences within a paragraph.
Some editors find that this aids editing
and improves the ''diff'' function.

But an empty line
starts a new paragraph.
```
 |

| You can break lines
without starting a new paragraph. | 
```
You can break lines<br>
without starting a new paragraph.
```
 |


| * Lists are easy to do:
	+ start every line with a star
	+ more stars means deeper levels
 | 
```
* Lists are easy to do:
** start every line with a star
** more stars means deeper levels

```
 |


| 1. Numbered lists are also good
	1. very organized
	2. easy to follow
 | 
```
# Numbered lists are also good
## very organized
## easy to follow
```
 |


| * You can even do mixed lists
	1. and nest them
		+ like this
 | 
```
* You can even do mixed lists
*# and nest them
*#* like this
```
 |


|  Definition list  list of definitions
 item  the item's definition
 | 
```
; Definition list : list 
of definitions
; item : the item's definition
```
 |


|  A colon indents a line or paragraph.
A manual newline starts a new paragraph.

* This is primarily for displayed material, but is also used for discussion on  [Talk pages](/metaweb-talk-page).
 | 
```
: A colon indents a line or paragraph.
A manual newline starts a new paragraph.


```
 |


| 
```
IF a line starts with a space THEN
  it will be formatted exactly 
    as typed;
  in a fixed-width font;
  lines won't wrap;
ENDIF
this is useful for:
  * pasting preformatted text;
  * algorithm descriptions;
  * program source code
  * ascii art;
```


WARNING: If you make it wide,
you [force the whole page to be wide](/http-en-wikipedia-org-wiki-page-widening) and
hence less readable. Never start ordinary lines with spaces.
 | 
```
 IF a line starts with a space THEN
   it will be formatted exactly 
     as typed;
   in a fixed-width font;
   lines won't wrap;
 ENDIF
 this is useful for:
   * pasting preformatted text;
   * algorithm descriptions;
   * program source code
   * ascii art;
```
 |


| Centered text. | 
```
<center>Centered text.</center>
```
 |


| A [horizontal dividing line](/http-en-wikipedia-org-wiki-horizontal-dividing-line): this is above it


---


and this is below it.

Mainly useful for separating threads on Talk pages.
 | 
```
A horizontal dividing line: this is above it
----
and this is below it. 
```
 |























## Links, URLs, images





| What it looks like | What you type |
| --- | --- |
| London has good
[public transport](/http-en-wikipedia-org-wiki-public-transport).
* First letter of target is automatically capitalized.
* Internally spaces are automatically represented as underscores (typing an underscore has the same effect as typing a space, but is not recommended).

Thus the link above is to http://www.metaweb.com/wiki/wiki.phtml?title=Public\_transport, which is the article with the name "Public transport".
 | London has good
[http://en.wikipedia.org/wiki/Public\_transport public transport]

*Seems many think London has good [public transport](/http-en-wikipedia-org-wiki-public-transport) but itdoesn't measure up to even a small city in [Japan](/http-en-wikipedia-org-wiki-japan) like [Fukuoka](/http-en-wikipedia-org-wiki-fukuoka)*.
 |
| 
Link to a section on a page, e.g. 
[List\_of\_cities\_by\_country#Morocco](/list-of-cities-by-country) (links to non-existent sections aren't really broken, they are treated as links to the page, i.e. to the top) | 
[[List\_of\_cities\_by\_country#Morocco]] |
| Same target, different name:
[answers](/metaweb-faq).
(This is a [piped link](/http-en-wikipedia-org-wiki-piped-link).)
 | 
```
Same target, different name: 
[[Metaweb FAQ|answers]]
```
 |
| Endings are blended into the link: [test](/http-en-wikipedia-org-wiki-test)ing, [gene](/http-en-wikipedia-org-wiki-test)s
 | 
```
Endings are blended 
into the link: [http://en.wikipedia.org/wiki/Test test]ing, [http://en.wikipedia.org/wiki/Test gene]s
```
 |
| 
Automatically hide stuff in parentheses: [Daniel Waterhouse](/daniel-waterhouse-alan-sinder).
Automatically hide namespace: [How does one edit a page](/metaweb-how-does-one-edit-a-page). 

The server fills in the part after the | when you save the page. Next time you open the edit box you will see the expanded piped link. A preview interprets the abbreviated form correctly, but does not expand it yet in the edit box. Press Save and again Edit, and you will see the expanded version. The same applies for the following feature.

 | 
```
Automatically hide stuff in parentheses:
[[Daniel Waterhouse (Alan Sinder)|]]. 
```


```
Automatically hide namespace: 
[[metaweb:How does one edit a page|]].
```
 |
| When adding a comment to a Talk page,
you should sign it. You can do this by
adding three tildes for your user name:
 [Tpierce](/user-tpierce)
or four for user name plus date/time:
 [Tpierce](/user-tpierce) 08:10 Oct 5, 2002 (UTC)
 | 
```
When adding a comment to a Talk page,
you should sign it. You can do this by
adding three tildes for your user name:
: ~~~
or four for user name plus date/time:
: ~~~~
```
 |
| [The weather in Victorian London](/the-weather-in-victorian-london) is a page that doesn't
exist yet.

* You can create it by clicking on the link.
* To create a new page:
	1. Create a link to it on some other page.
	2. Save that page.
	3. Click on the link you just made. The new page will open for editing.
* Have a look at [how to start a page](/metaweb-how-to-start-a-page) guide and Metaweb's [naming conventions](/metaweb-naming-conventions).
* After creating a page, search for its title and make sure that everyone correctly links to it.
 | 
```
[[The weather in Victorian London]] is a page
that doesn't exist yet.
```
 |
| [Redirect](/metaweb-redirect) one article title to another by putting text like this in its first line.
 | 
```
#REDIRECT [[United States]]
```
 |
| External link: [Main](/http-www-nupedia-com) | 
```
External link: 
[http://www.nupedia.com Nupedia]
```
 |
| Or just give the URL: [http://www.nupedia.com](/http-www-nupedia-com).

* In the [URL](/url) all symbols must be among: A-Z a-z 0-9 .\_\/~%-+&#?!=()@ \x80-\xFF. If a URL contains a different character it should be converted; for example, ^ has to be written %5E (to be looked up in [ASCII](/http-en-wikipedia-org-wiki-ascii)).
 | 
```
Or just give the URL: 
http://www.nupedia.com.
```
 |
| A picture: [Quicksilver Metaweb](/quicksilver-metaweb)* Only images that have been uploaded to Metaweb can be used. To upload images, use the [upload page](/special-upload). You can find the uploaded image on the [image list](/special-imagelist). See [Metaweb:Image use policy](/metaweb-image-use-policy) for many more hints.
 | 
```

A picture: [[Image:Wiki.png]]
```

or, with alternate text (*strongly* encouraged) 

```
[[Image:Wiki.png|Quicksilver Metaweb]] 

```


Browsers render alternate text when not displaying an image -- for example, when the image isn't loaded, or in a text-only browser, or when spoken aloud. See [Alternate text for images](/metaweb-alternate-text-for-images) for help on choosing alternate text.
 |
| 
Clicking on an uploaded image displays a description page, which you can also link directly to: [:Image:Wiki.png](/image-wiki-png) | 
```



[[:Image:Wiki.png]]

```
 |
| 
To include links to non-image uploads such as sounds, or to images shown as links instead of drawn on the page, use a "media" link.

[Sound](/sound)

[Image of a Tornado](/image-of-a-tornado) | 
```



[[media:Sg\_mrob.ogg|Sound]]

[[media:Tornado.jpg|Image of a Tornado]]


```
 |
| 
To link to books, you can use [metaweb:ISBN](/metaweb-isbn) links.

[ISBN 0123456789X](/) | 
ISBN 0123456789X
 |



## Character formatting





| What it looks like | What you type |
| --- | --- |
| *Emphasize*, **strongly**, ***very strongly***.
* These are double and triple apostrophes, not double quotes.
 | 
```
''Emphasize'', '''strongly''', 
'''''very strongly'''''.
```
 |
| 
You can also write *italic* and **bold**
if the desired effect is a specific font style
rather than emphasis, as in mathematical formulae:

**F** = *m***a**
* However, the difference between these two methods is not very important for graphical browsers, and many people choose to ignore it.
 | 
```
You can also write <i>italic</i> and <b>bold</b>
if the desired effect is a specific font style
rather than emphasis, as in mathematical formulas:

:<b>F</b> = <i>m</i><b>a</b>
```
 |
| A typewriter font for technical terms.
 | 
```
A typewriter font for <tt>technical terms</tt>.
```
 |
| You can use small text for captions.
 | 
```
You can use <small>small text</small> for captions.
```
 |
| You can strike out deleted material
and underline new material.
 | 
```
You can <strike>strike out deleted material</strike>
and <u>underline new material</u>.
```
 |
| **Umlauts and accents:** (See [metaweb:Special characters](/metaweb-special-characters))
À Á Â Ã Ä Å 
Æ Ç È É Ê Ë 
Ì Í
Î Ï Ñ Ò 
Ó Ô Õ
Ö Ø Ù 
Ú Û Ü ß
à á 
â ã ä å æ
ç 
è é ê ë ì í
î ï ñ ò ó ô 
œ õ
ö ø ù ú 
û ü ÿ
 | 
```



&Agrave; &Aacute; &Acirc; &Atilde; &Auml; &Aring; 
&AElig; &Ccedil; &Egrave; &Eacute; &Ecirc; &Euml; 
&Igrave; &Iacute; &Icirc; &Iuml; &Ntilde; &Ograve; 
&Oacute; &Ocirc; &Otilde; &Ouml; &Oslash; &Ugrave; 
&Uacute; &Ucirc; &Uuml; &szlig; &agrave; &aacute; 
&acirc; &atilde; &auml; &aring; &aelig; &ccedil; 
&egrave; &eacute; &ecirc; &euml; &igrave; &iacute;
&icirc; &iuml; &ntilde; &ograve; &oacute; &ocirc; 
&oelig; &otilde; &ouml; &oslash; &ugrave; &uacute; 
&ucirc; &uuml; &yuml;
```
 |
| **Punctuation:**
¿ ¡ « » § ¶
† ‡ • —
 | 
```


&iquest; &iexcl; &laquo; &raquo; &sect; &para;
&dagger; &Dagger; &bull; &mdash;
```
 |
| **Commercial symbols:**
™ © ® ¢ € ¥ 
£ ¤ | 
```


&trade; &copy; &reg; &cent; &euro; &yen; 
&pound; &curren;

```
 |
| Subscript: x2
Superscript: x2 or x²
* The latter method of superscript can't be used in the most general context, but is preferred when possible (as with units of measurement) because most browsers have an easier time formatting lines with it.

ε0 =
8.85 × 10−12
C² / J m. | 
```
Subscript: x<sub>2</sub>
Superscript: x<sup>2</sup> or x&sup2;

&epsilon;<sub>0</sub> =
8.85 &times; 10<sup>&minus;12</sup>
C&sup2; / J m.
```
 |
| **Greek characters:** 
α β γ δ ε ζ 
η θ ι κ λ μ ν 
ξ ο π ρ σ ς 
τ υ φ χ ψ ω
Γ Δ Θ Λ Ξ Π 
Σ Φ Ψ Ω
 | 
```


&alpha; &beta; &gamma; &delta; &epsilon; &zeta; 
&eta; &theta; &iota; &kappa; &lambda; &mu; &nu; 

&xi; &omicron; &pi; &rho;  &sigma; &sigmaf;
&tau; &upsilon; &phi; &chi; &psi; &omega;
&Gamma; &Delta; &Theta; &Lambda; &Xi; &Pi; 
&Sigma; &Phi; &Psi; &Omega;

```
 |
| **Math characters:** 
∫ ∑ ∏ √ − ± ∞
≈ ∝ ≡ ≠ ≤ ≥ →
× · ÷ ∂ ′ ″
∇ ‰ ° ∴ ℵ ø
∈ ∉ ∩ ∪ ⊂ ⊃ ⊆ ⊇
¬ ∧ ∨ ∃ ∀ ⇒ ⇔
→ ↔ | 
```

&int; &sum; &prod; &radic; &minus; &plusmn; &infin;

&asymp; &prop; &equiv; &ne; &le; &ge; &rarr;
&times; &middot; &divide; &part; &prime; &Prime;
&nabla; &permil; &deg; &there4; &alefsym; &oslash;
&isin; &notin; &cap; &cup; &sub; &sup; &sube; &supe;
&not; &and; &or; &exist; &forall; &rArr; &hArr;
&rarr; &harr;
```
 |
| *x*2   ≥   0 true.
* To space things out, use non-breaking spaces - &nbsp;.
* &nbsp; also prevents line breaks in the middle of text, this is useful in formulas.
 | 
```

<i>x</i><sup>2</sup>&nbsp;&nbsp;&ge;&nbsp;&nbsp;0 true.

```
 |
| **Complicated formulae:**
  \sum_{n=0}^\infty \frac{x^n}{n!}* See [metaweb:TeX markup](/metaweb-tex-markup)
 | 
```
  
<math>\sum\_{n=0}^\infty \frac{x^n}{n!}</math>

```
 |
| **Suppressing interpretation of markup:**
Link → (<i>to</i>) the [[Metaweb FAQ]]
* Used to show literal data that would otherwise have special meaning.
* Escapes all  [wiki markup](/metaweb-faq), including that which looks like HTML tags.
* Does not escape HTML character entities.
 | 
```
<nowiki>Link &rarr; (<i>to</i>) 
the [[Metaweb FAQ| wiki markup]]</nowiki>
```
 |
| **Commenting page source:**
*not shown in page** Used to leave comments in a page for future editors.
 | 
```
<!-- comment here -->
```
 |



### Placement of the Table of Contents (TOC)


At the current status of the wiki markup language, at least four headers trigger the TOC in front of the first header (or after introductory sections). Putting \_\_NOTOC\_\_ anywhere forces the TOC to disappear.

*This entry originally from the [Wikipedia](/http-www-wikipedia-org)*
