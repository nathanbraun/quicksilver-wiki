
# Metaweb:How to use tables

From the Quicksilver Metaweb.


Tables can be useful for a variety of content presentation on Wikipedia. If you are familiar with the [HTML](/http-en-wikipedia-org-wiki-html) code needed to create tables, you can simply insert the code directly into the article as you are editing. Table markup is often difficult to edit, however, especially for those unfamiliar with HTML. There are some situations where tables are inappropriate, and simpler markup should be used instead. This page discusses how to create tables in Wikipedia articles, and when they are appropriate.

**Please note that the use of HTML is no longer necessary. [Metaweb:How to edit a page](/metaweb-how-to-edit-a-page) explains how to use wikicode for creating tables.**

## Example table



### Wikipedia code




> 
> 
> ```
> <table border="1" cellpadding="2">
> <caption>Multiplication table</caption>
> <tr><th>&times;</th><th>1</th><th>2</th><th>3</th></tr>
> <tr><th>1</th><td>1</td><td>2</td><td>3</td></tr>
> <tr><th>2</th><td>2</td><td>4</td><td>6</td></tr>
> <tr><th>3</th><td>3</td><td>6</td><td>9</td></tr>
> <tr><th>4</th><td>4</td><td>8</td><td>12</td></tr>
> <tr><th>5</th><td>5</td><td>10</td><td>15</td></tr>
> </table>
> ```
> 
> 



### What it looks like in your browser




> 
> 
> 
> Multiplication table| × | 1 | 2 | 3 |
> | 1 | 1 | 2 | 3 |
> | 2 | 2 | 4 | 6 |
> | 3 | 3 | 6 | 9 |
> | 4 | 4 | 8 | 12 |
> | 5 | 5 | 10 | 15 |
> 
> 



The important things to note in the example:

* The entire table begins with `<table ...>` and ends with the required `</table>`
* A **Caption** is a succinct way to describe your table, and should go inside the `caption` element just after the initial `<table>` tag
* **Table rows** are horizontal groups of cells in the table. They begin with `<tr>` and end with the optional `</tr>`
* **Table headings** are cells with headings in them, and are often rendered in a bold font. They begin with `<th>` and end with the optional `</th>`
* **Table data** cells fill out the rest of the table. They begin with `<td>` and end with the optional `</td>`


The `td` and `th` elements are sometimes called "cells", somewhat like the cells in a [spreadsheet](/http-en-wikipedia-org-wiki-spreadsheet). Each row must have the same number of cells as the other rows, so that the number of columns in the table remains consistent (unless there are cells which span several columns or rows, but this is not discussed here). For empty cells, use the non-breaking space "`&nbsp;`" as content, otherwise some browsers may not format the table properly.

If your table doesn't look right, make sure that all of the [HTML tag](/http-en-wikipedia-org-wiki-html-tag)s are properly nested. You may find it easier to leave out the optional closing tags for some elements, since they are not strictly required in [HTML](/http-en-wikipedia-org-wiki-html). The best way to find errors in your table, though, is to check the article using the [W3C MarkUp Validation Service](/http-validator-w3-org). Simply copy the URL of your article and paste it into the validator's address box. This service is especially useful for large, complex tables that would be difficult to check visually.

The sample above without the optional closing tags looks as follows:

> 
> 
> ```
> <table border="1" cellpadding="2">
> <caption>Multiplication table</caption>
> <tr><th>&times;<th>1<th>2<th>3
> <tr><th>1<td>1<td>2<td>3
> <tr><th>2<td>2<td>4<td>6
> <tr><th>3<td>3<td>6<td>9
> <tr><th>4<td>4<td>8<td>12
> <tr><th>5<td>5<td>10<td>15
> </table>
> ```
> 
> 


Besides being shorter, this makes the page easier to maintain and less error-prone.

If you are already familiar with HTML tables, you may want to note that the `thead`, `tbody`, `tfoot`, and `colgroup` elements are currently unsupported in Wikipedia.

## Another example



Here's a more advanced example, showing some more options available for making up tables. You can play with these settings in your own table to see what effect they have. Not all of these techniques may be appropriate in all cases; just because you can add colored backgrounds, for example, doesn't mean it's always a good idea. Try to keep the markup in your tables relatively simple -- remember, other people are going to be editing the article too! This example should give you an idea of what is possible, though.

### Wikipedia code




> 
> 
> ```
> <table border="1" cellpadding="5" cellspacing="0" align="center">
> <caption>'''An example table'''</caption>
> <tr>
> <th style="background:#efefef;">First header</th>
> <th colspan="2" style="background:#ffdead;">Second header</th>
> </tr>
> <tr>
> <td>upper left</td>
> <td> </td>
> <td rowspan=2 style="border-bottom:3px solid grey;" valign="top">
> right side</td>
> </tr>
> <tr>
> <td style="border-bottom:3px solid grey;">lower left</td>
> <td style="border-bottom:3px solid grey;">lower middle</td>
> </tr>
> <tr>
> <td colspan="3" align="center">
> <table border="0">
> <caption>''A table in a table''</caption>
> <tr>
> <td align="center" width="150px">[[Image:wiki.png]]</td>
> <td align="center" width="150px">[[Image:wiki.png]]</td>
> </tr>
> <tr>
> <td align="center" colspan="2" style="border-top:1px solid red; 
> border-right:1px solid red; border-bottom:2px solid red; 
> border-left:1px solid red;">
> Two Wikipedia logos</td>
> </tr>
> </table>
> </td>
> </tr>
> </table>
> 
> ```
> 
> 



### What it looks like in your browser




> 
> 
> 
> **An example table**| First header | Second header |
> | upper left |  | 
> right side |
> | lower left | lower middle |
> | 
> 
> *A table in a table*| [Wiki.png](/wiki-png) | [Wiki.png](/wiki-png) |
> | Two Wikipedia logos |
> 
>  |
> 
> 
> 



## Yet Another Example



Here is a sample in a new wikicode, that may be simpler than the usual HTML. The source is somewhat longer (10-20%) than the HTML version.

### Wikipedia code




> 
> 
> ```
> <table border="1" cellpadding="2">
> <caption>Multiplication table</caption>
> 
> {| border="1" cellpadding="2"
> |'''Name:'''
> |'''Effect:'''
> |'''Games Found In'''
> |-
> |Pokeball
> |Regular Pokeball
> |All Versions
> |-
> |Great Ball
> |Better than a Pokeball
> |All Versions
> |-
> |Ultra Ball
> |Better than a Great Ball
> |All Versions
> |-
> |Master Ball
> |Catches any Pokémon without fail.
> |All Versions
> |-
> |}
> </table>
> ```
> 
> 



### What it looks like in your browser




> 
> {| border="1" cellpadding="2"
> |**Name:**
> |**Effect:**
> |**Games Found In**
> |-
> |Pokeball
> |Regular Pokeball
> |All Versions
> |-
> |Great Ball
> |Better than a Pokeball
> |All Versions
> |-
> |Ultra Ball
> |Better than a Great Ball
> |All Versions
> |-
> |Master Ball
> |Catches any Pokémon without fail.
> |All Versions
> |-
> |}
> 



## When tables are appropriate



Tables are perfect for organizing any information that is best presented in a row-and-column format. This might include:

* Mathematical tables
	+ Multiplication tables
	+ Tables of divisors
	+ Lookup tables
* Lists of information
	+ Equivalent words in two or more languages
	+ Person, birthdate, occupation
	+ Artist, album, year, and label


Many times, a list is best left as a list. Some articles include excessively long lists which would be very difficult to edit if they were in table form. Before you format a list in table form, consider whether the information will be more clearly conveyed by virtue of having rows and columns. If so, then a table is probably a good choice. If there is no obvious benefit to having rows and columns, then a table is probably not the best choice.

Tables shouldn't be used simply for layout, either. If the information you're editing isn't tabular in nature, it probably doesn't belong in a table. Try not to use tables for putting a caption under a photograph, arranging a group of links, or other strictly visual features. It makes the article harder to edit for other Wikipedians, and isn't really what tables were designed to do.

## When tables are inappropriate



### Very long lists, or very simple lists



If a list is quite long, or is relatively simple, use one of the standard Wikipedia list formats. Long lists can be hard to maintain if they are inside a table, and simple lists are (simply) too simple to need the row-and-column format that a table provides. Here are some examples of things that might be better done with lists instead of tables.

#### Table formatting (Don't do this)



> 
> 
> 
> |  |  |
> | --- | --- |
> | 1980 | Ultra Wave |
> | 1988 | What's Bootsy Doin'? |
> | 1994 | Blasters of the Universe |
> | 1994 | Fresh Outta 'P' University |
> 
> 
> 



#### Without tables (Do this instead)



> 
> * 1980: Ultra Wave
> * 1988: What's Bootsy Doin'?
> * 1994: Blasters of the Universe
> * 1994: Fresh Outta 'P' University
> 



### Layout of images



Many times, images in an article are placed using a quirk of table rendering. Because a table can be floated to the left or right side of the screen, it has become common practice to utilize a simple one-celled table to place an image in a particular part of the screen. This was a necessary workaround for old browsers, since it generates a consistent rendering of images in browsers which do not adequately support [Cascading Style Sheets](/http-en-wikipedia-org-wiki-cascading-style-sheets). By far, the majority of browsers in use today, however, should do just fine with style sheets. The recommended practice now is to arrange images using an element called `div`.

For detailed instructions, see [Wikipedia:Image Use Policy](/http-en-wikipedia-org-wiki-wikipedia-image-use-policy) and the [Wikipedia:Image markup gallery](/http-en-wikipedia-org-wiki-wikipedia-image-markup-gallery). Here's a brief example, though:

#### Table formatting (Don't do this)



> 
> `<table align="right" border="0" cellpadding="0"><tr><td>[[Image:Covalent.png]]</td></tr></table>`
> 



#### Without tables (Do this instead)



> 
> `<div style="float:right; margin: 0 0 1em 1em;">[[Image:Covalent.png]]</div>`
> 



#### How it looks


In both of these cases, the result is essentially the same; the image is floated to the right-hand side of the screen, and the surrounding text wraps around it. Here is what it looks like in your browser (with text added):


> 
> [![Covalent.png](/web/20060725221205im_/http://www.metaweb.com/wiki/upload/d/d9/Covalent.png)](covalent-png)
> Covalent bonding most frequently occurs between atoms with similar electronegativities, where neither atom can provide sufficient energy to completely remove an electron from the other atom. Covalent bonds are more common between non-metals, whereas ionic bonding is more common between two metal atoms or a metal and a non-metal atom.
>   
>    
> Covalent bonding tends to be stronger than other types of bonding, such as ionic bonding. In addition unlike ionic bonding, where ions are held together by a non-directional coulombic attraction, covalent bonds are highly directional. As a result, covalently bonded molecules tend to form in a relatively small number of characteristic shapes, exhibiting specific bonding angles.
> 



## Possible problems



Tables may cause other difficulties, even when used appropriately. Here are some issues you may want to consider if you use tables in your articles:

* Tables may be hard for other people to edit, especially for people who are new to Wikipedia. New editors may be daunted if they click "Edit this page" and see a large block of unintelligible (to them) HTML code. Try to keep your tables simple, and well-formatted in the code. You might also add a comment (which won't appear in the rendered page) like "<!-- To edit the text of this article, skip past the table. -->" in order to reassure editors.
* It is tricky, even for experienced HTML authors, to make sure that tables render correctly on all (or even many) web browsers. Even the slightest typographical mistake can cause drastic visual problems with the table. You may be confident of your abilities to prevent this from happening, but future editors may not be. Again, keep tables simple and well-formatted, and this is less likely to be a problem.
* Large tables, with lots of information, may run off the right side of the screen on lower resolutions. This is sometimes acceptable, especially if the user is warned beforehand (for example, [Periodic Table (Huge)](/http-en-wikipedia-org-wiki-periodic-table-huge) is deliberately very large). If you find it necessary to create a very large table for an article, you may want to consider creating a simpler, smaller version for users who cannot effectively use the larger version (for example, the periodic table is also available in a [smaller version](/http-en-wikipedia-org-wiki-periodic-table-standard)).
* If you include fixed-width text inside a table (using the HTML `code`, `pre`, or `tt` elements, for example), it may force the page to be wider than necessary. Whenever possible, avoid using fixed-width text inside tables, so the text can flow naturally. A similar problem can happen if you include images inside tables (since images are usually constrained to be a fixed width).
* Cells containing a great deal of information may cause rendering problems on some browsers. In particular, a cell containing a large paragraph may jumble the formatting on text-only browsers such as [Lynx](/http-en-wikipedia-org-wiki-lynx-web-browser). This is often necessary, depending on what sort of table you're creating, but if at all possible, try to limit the amount of content you place in table cells.


## External links


[The Table Sampler](/http-wp-netscape-com-assist-net-sites-table-sample-html) - Various useful example tables

*This entry originally from the [Wikipedia](/http-www-wikipedia-org)*
