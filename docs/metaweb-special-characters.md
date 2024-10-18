
# Metaweb:Special characters

From the Quicksilver Metaweb.



**This page is deprecated but will be updated periodically.**
**Please direct edits to the [Meta-Wikimedia version of this page](/)**

A useful list can be found in the german version of this text.

Many characters not in the repertoire of standard [ASCII](/ascii) will be useful -even necessary - for Wiki pages, especially the international pages. This page contains my recommendations for which characters are safe to use and how to use them. There are three ways to enter a non-ASCII character into a Wiki page:


1. Enter the character directly from a foreign keyboard, or by cut and paste from a "character map" type application, or by some special means provided by the operating system or text editing application. The web server should then be configured to announce which 8-bit character set is being used.
2. Use an HTML named character entity reference like `&agrave;`. This is unambiguous even when the server does not announce the use of any special character set, and even when the character does not display properly on some browsers. However it may cause difficulties with searches (see below).
3. Use an HTML numeric character entity reference like `&#161;`. This is not recommended, because many browsers incorrectly interpret these as references to the native character set. It is, however, the only way to enter [Unicode](/unicode) values for which there is no named entity, such as the [Turkish](/wikipedia-turkish-characters) letters. Note that because the code points 128 to 159 are unused in both ISO-8859-1 and [Unicode](/unicode), character references in that range such as `&#131;` are illegal and ambiguous, though they are commonly used by many web sites.


Generally speaking, Western European languages such as Spanish, French, and German pose few problems. For specific details about other languages, see: [Turkish](/wiki-special-characters-turkish) (more will be added to this list as contributors in other languages appear).

For the purpose of searching, a word with a special character can best be written using the first method. If the second method is used a word like Odiliënberg can only be found by searching for Odili, euml and/or nberg; this is actually a bug that should be fixed -- the entities should be folded into their raw character equivalents so all searches on them are equivalent. See also [Wikipedia:Searching](/wikipedia-searching).


## ISO-8859-1 Characters


The following [extended ASCII](/extended-ascii) characters are safe for use in all Wiki pages. The table below shows the character itself, lists the code for each character in hexadecimal and decimal, shows the HTML entity name, and gives the common name of the character.



|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Literal](/literal) Hex Dec Entity Character
|  00A0  0160  &nbsp;  [no-break space](/no-break-space)| ¡  00A1  0161  &iexcl;  [inverted exclamation](/inverted-exclamation)| ¢  00A2  0162  &cent;  [cent sign](/cent-sign)| £  00A3  0163  &pound;  [pound sign](/pound-sign)| ¤ 00A4  0164  &curren; [intl. currency sign](/intl-currency-sign)| ¥  00A5  0165  &yen;  [yen sign](/yen-sign)| §  00A7  0167  &sect;  [section sign](/section-sign)| ¨  00A8  0168  &uml;  [diaeresis](/diaeresis) ([umlaut](/umlaut))
| ©  00A9  0169  &copy;  [copyright sign](/copyright-sign)| ª  00AA  0170  &ordf;  [feminine ordinal](/feminine-ordinal)| «  00AB  0171  &laquo;  [left double-angle quote](/left-double-angle-quote)| ¬  00AC  0172  &not;  [not sign](/not-sign)| ®  00AE  0174  &reg;  [registered trademark sign](/registered-trademark-sign)| ¯  00AF  0175  &macr;  [macron](/macron)| °  00B0  0176  &deg;  [degree sign](/degree-sign)| ± 00B1  0177  &plusmn; [plus-minus sign](/plus-minus-sign)| ´  00B4  0180  &acute;  [acute accent](/acute-accent)| µ  00B5  0181  &micro;  [micro sign](/micro-sign)| ¶  00B6  0182  &para;  [pilcrow](/pilcrow) (paragraph) sign
| · 00B7  0183  &middot; [middle dot](/middle-dot) (Georgian comma)
| ¸  00B8  0184  &cedil;  [cedilla](/cedilla)| º  00BA  0186  &ordm;  [masculine ordinal](/masculine-ordinal)| »  00BB  0187  &raquo;  [right double-angle quote](/right-double-angle-quote)| ¿ 00BF  0191  &iquest; [inverted question](/inverted-question)| À 00C0  0192  &Agrave; [A grave](/a-grave)| Á 00C1  0193  &Aacute; [A acute](/a-acute)| Â  00C2  0194  &Acirc;  [A circumflex](/a-circumflex)| Ã 00C3  0195  &Atilde; [A tilde](/a-tilde)| Ä  00C4  0196  &Auml;  [A diaeresis](/a-diaeresis)| Å  00C5  0197  &Aring;  [A ring](/a-ring)| Æ  00C6  0198  &AElig;  [AE ligature](/ae-ligature)| Ç 00C7  0199  &Ccedil; [C cedilla](/c-cedilla)| È 00C8  0200  &Egrave; [E grave](/e-grave)| É 00C9  0201  &Eacute; [E acute](/e-acute)| Ê  00CA  0202  &Ecirc;  [E circumflex](/e-circumflex)| Ë  00CB  0203  &Euml;  [E diaeresis](/e-diaeresis)| Ì 00CC  0204  &Igrave; [I grave](/i-grave)| Í 00CD  0205  &Iacute; [I acute](/i-acute)| Î  00CE  0206  &Icirc;  [I circumflex](/i-circumflex)| Ï  00CF  0207  &Iuml;  [I diaeresis](/i-diaeresis)| Ñ 00D1  0209  &Ntilde; [N tilde](/n-tilde)| Ò 00D2  0210  &Ograve; [O grave](/o-grave)| Ó 00D3  0211  &Oacute; [O acute](/o-acute)| Ô  00D4  0212  &Ocirc;  [O circumflex](/o-circumflex)| Õ 00D5  0213  &Otilde; [O tilde](/o-tilde)| Ö  00D6  0214  &Ouml;  [O diaeresis](/o-diaeresis)| Ø 00D8  0216  &Oslash; [O stroke](/o-stroke)| Ù 00D9  0217  &Ugrave; [U grave](/u-grave)| Ú 00DA  0218  &Uacute; [U acute](/u-acute)| Û  00DB  0219  &Ucirc;  [U circumflex](/u-circumflex)| Ü  00DC  0220  &Uuml;  [U diaeresis](/u-diaeresis)| ß  00DF  0223  &szlig;  [sharp s](/sharp-s) (ess-zed)
| à 00E0  0224  &agrave; [a grave](/a-grave)| á 00E1  0225  &aacute; [a acute](/a-acute)| â  00E2  0226  &acirc;  [a circumflex](/a-circumflex)| ã 00E3  0227  &atilde; [a tilde](/a-tilde)| ä  00E4  0228  &auml;  [a diaeresis](/a-diaeresis)| å  00E5  0229  &aring;  [a ring](/a-ring)| æ  00E6  0230  &aelig;  [ae ligature](/ae-ligature)| ç 00E7  0231  &ccedil; [c cedilla](/c-cedilla)| è 00E8  0232  &egrave; [e grave](/e-grave)| é 00E9  0233  &eacute; [e acute](/e-acute)| ê  00EA  0234  &ecirc;  [e circumflex](/e-circumflex)| ë  00EB  0235  &euml;  [e diaeresis](/e-diaeresis)| ì 00EC  0236  &igrave; [i grave](/i-grave)| í 00ED  0237  &iacute; [i acute](/i-acute)| î  00EE  0238  &icirc;  [i circumflex](/i-circumflex)| ï  00EF  0239  &iuml;  [i diaeresis](/i-diaeresis)| ñ 00F1  0241  &ntilde; [n tilde](/n-tilde)| ò 00F2  0242  &ograve; [o grave](/o-grave)| ó 00F3  0243  &oacute; [o acute](/o-acute)| ô  00F4  0244  &ocirc;  [o circumflex](/o-circumflex)| õ 00F5  0245  &otilde; [o tilde](/o-tilde)| ö  00F6  0246  &ouml;  [o diaeresis](/o-diaeresis)| ÷ 00F7  0247  &divide; [divide sign](/divide-sign)| ø 00F8  0248  &oslash; [o stroke](/o-stroke)| ù 00F9  0249  &ugrave; [u grave](/u-grave)| ú 00FA  0250  &uacute; [u acute](/u-acute)| û  00FB  0251  &ucirc;  [u circumflex](/u-circumflex)| ü  00FC  0252  &uuml;  [u diaeresis](/u-diaeresis)| ÿ  00FF  0255  &yuml;  [y diaeresis](/y-diaeresis) | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |
 | | | | |



These characters are a subset of the most common [extended ASCII](/extended-ascii) character set in use on the [Internet](/internet), [ISO 8859-1](/iso-8859-1). Wikipedia pages are identified by the server as containing ISO-8859-1 text. The characters above are a subset selected to improve compatibility with other machines.

For example, the [Apple Macintosh](/apple-macintosh) is in common use on the Internet, is not limited to any specific language, and its native character set (which is not ISO-8859-1) contains many of the common international characters. Many Macintosh browsers will correctly translate ISO text into the native character set, as long as the characters used are available. So the table above is the subset of ISO-8859-1 characters that are also available on the native Macintosh character set. [Microsoft Windows](/microsoft-windows) standard code page 1252 set is a superset of ISO-8859-1, so these characters will be readable as is on Windows machines. The most common Latin character sets other than ISO-8859-1 are MS-DOS (pre-Windows) code page 437, Macintosh Roman, and other ISO sets such as ISO-8859-2. The number of pre-Windows MS-DOS machines with web browsers is small and they are often dedicated-purpose machines that wouldn't be using Wikipedia anyway, so it is reasonably safe to sacrifice compatibility with them for the sake of needed foreign characters. Other ISO sets are generally intended to be read by other browsers using those same sets in the same country, and so those pages should use a language-specific set.

These characters can be entered either as HTML named character entity references such as **&agrave;**, directly from foreign keyboards, or with whatever facilities are available to the Wiki author for entering these characters. For example, Wiki authors using Windows machines can enter these by holding down the Alt key while typing the 4-digit decimal code of the character on the numeric pad of the keyboard. It is important that all 4 digits (including the leading 0) be typed; typing a 3-digit code will enter characters from the obsolete code page 437. Wiki authors using Macintosh machines should take care to either use special facilities to enter these in ISO-8859-1 format rather than with the native character set, or else use HTML named character entity references. Note that some Windows users may have trouble with versions of Microsoft Internet Explorer that use "Alt-Left-Arrow" and "Alt-Right-Arrow" for page movement. These will interfere with entering codes that contain the digits 4 and 6. Use HTML named character entity references in this case.

The characters from the table above can be used directly as 8-bit characters in all Wiki pages, and are sufficient for all pages primarily in English, Spanish, French, German, and languages that require no more special characters than those (such as Catalan). These are also generally safe to use in titles, except for a few characters like double quotes, less than and greater than, and a few others.

### Unsafe characters


Note especially what is missing here from the full ISO-8859-1 set: The broken bar (`0166=&brvbar;`), soft hyphen (`0173=&shy;`), superscript digits (`0178=&sup2;, 0179=&sup3;`), vulgar fractions (`0188=&frac14;, 0189=&frac12;, 0190=&frac34;`), Old English (and [Icelandic](/icelandic-language) and [Old Norse language](/old-norse-language)) eth and thorn (`0208=&ETH;, 0240=&eth;, 0222=&THORN;, 0254=&thorn;`), and multiply sign (`0215=&times;`). These should be considered unsafe (and adequate substitutes are available for most of them).

Special care should be taken with characters that do exist in the native character set of popular machines but not in the above set. These are not safe, even though they may display correctly to you when you use them. Characters from Windows code page 1252 not in ISO-8859-1 include the euro sign (`&euro;`), dagger and double dagger (`&dagger;, &Dagger;`), bullet (`&bull;`), trade mark sign (`&trade;`), typeset-style punctuation (see below), per mille sign (`&permil;`), some Eastern European caron-accented letters, and the oe ligatures. Characters from the Macintosh Roman set not in ISO-8859-1 include dagger and double dagger, bullet, trade mark sign, a few math symbols such as infinity (`&infin;`) and not equal (`&ne;`), a few commonly-used Greek letters such as pi (`&pi;`), ligatures like oe and fl, typeset-style punctuation, per mille sign, and lone accents such as the breve, [ogonek](/ogonek), and caron.

[HTML 4.0](/http-www-w3-org-tr-html4) defines named character entities for some Latin characters not in ISO-8859-1 that are used by popular languages, such as OE ligature (`&OElig;, &oelig;`), uppercase Y with diaeresis (`&Yuml;`), and some Eastern European accented characters like `&scaron;`. These are also unsafe, though if they entered as HTML named character entity references, they may display on some machines.

In short, don't assume that it is safe to use a special character just because it looks correct on your machine. Use the ones from the table above, and read and understand how to use others shown below.


## Possibly usable non-ISO characters


Some characters not listed as safe above may still be usable when entered as named HTML character entity references, because web browsers will recognize them and render them correctly, perhaps by switching to alternate fonts as needed. All of these should be considered less safe to use than those above, but only in the sense that they may not display properly, though in the form of HTML character entity references they are unambiguous, and preserve data integrity.

For many of these, adequate substitutes and workarounds are available, and should be used when the value of making the text available to users of older computers and software exceeds the value of good presentation to those with newer software (in the judgment of the author or editor).

### Typeset-style Punctuation


Absent from the ISO-8859-1 character set, but commonly used and present in both Macintosh Roman and Windows code page 1252 character sets, are proper English quotation marks and dashes. These can be entered as character entity references, and should appear correctly on most machines running recent software. Even on ISO-based machines such as Unix/X, browsers should be able to interpret these references and make appropriate substitutes using plain ASCII straight quotes and hyphens (Mozilla does this correctly, for example). These references were not present in older versions of HTML, so may not be recognized by older software. Since using these characters maintains data integrity even on those machines that may not display them correctly, it should be considered safe to use these unless proper display on old software is critical. German "low-9" quotation marks are a similar case, but are less commonly translated by browsing software, and so are not quite as safe. The table below shows these characters next to a capital letter "O" for better visibility:



|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ‘O | &lsquo; | left single quote | —O | &mdash; | em dash |
| ’O | &rsquo; | right single quote | –O | &ndash; | en dash |
| “O | &ldquo; | left double quote | ‚O | &sbquo; | single low-9 quote |
| ”O | &rdquo; | right double quote | „O | &bdquo; | double low-9 quote |



Many web sites targeted for a Windows-using audience use code page 1252 references for these characters: for example, using `&#151;` for the em dash. This is not a recommended practice. To ensure future data integrity and maximum compatibility, recode these as named references such as `&mdash;`. If you really want to use a number, you can use `&#8210;`. Still, many obscure characters, such as mdash, are incompatible with certain computers and are not recommended. It is preferable to use '-' or '--'.

Be aware that if you edit text in a separate word processor or other program to cut and paste into your browser, and it "automatically" converts quotes to the left and right "smart quotes" for you, you may unknowingly mangle markup, either your own or already existing, by replacing the standard quotes in HTML tags & properties with the smart quotes, which will cause the tags to fail in various ways. Furthermore, some people consider the extra encoding of smart quotes, fancy "&rsquo;" apostrophes used in possessives and contractions, etc., to be a waste of bytes that could be put to better use, and will replace them with the standard single characters at will.

Set your wordprocessor options such as Auto Edit and Auto Correction such that undesired replacements do not occur.

## Greek letters and math symbols


*Note: much of the text below regarding mathematical symbols is obsolete now that Wikipedia supports embedded [TeX](/tex) within articles. Non-trivial mathematical equations are probably best notated in TeX using the Wikipedia math tags. See the article [Wikipedia:TeX support](/wikipedia-tex-support) for more on this.*

Web standards for writing about mathematics are very recent (in fact MathML 2.0 was just released in February of 2001), so many browsers made before these standards were in place try to compensate by at least allowing characters commonly used in mathematics, including most of the [Greek alphabet](/greek-alphabet). These are necessarily entered as character entity references. Browsers often render these by switching to a "Symbol" font or something similar.

Upper- and lowercase Greek letters simply use their full names for character entities. These should, of course, only be used for occasional Greek letters in primarily-Latin text. (Large quantities of Greek-language text should be written using an editor with native [UTF-8](/utf-8) [Unicode](/unicode) support to facilitate editing and reduce article bloat). Here are a few samples:



|  |  |  |  |
| --- | --- | --- | --- |
| [α](/alpha) &alpha; Γ &Gamma; | | | |
| [β](/beta) &beta; Λ &Lambda; | | | |
| [γ](/gamma) &gamma; Σ &Sigma; | | | |
| [π](/pi) &pi; Π &Pi; | | | |
| [σ](/sigma) &sigma; Ω &Omega; | | | |
| [ς](/sigmaf) &sigmaf; ("final" sigma, lowercase only) | |



Other common math symbols:



|  |  |  |  |
| --- | --- | --- | --- |
| ≠ | &ne; | ′ | &prime; |
| ≤ | &le; | ″ | &Prime; |
| ≥ | &ge; | ∂ | &part; |
| ≡ | &equiv; | ∫ | &int; |
| ≈ | &asymp; | ∑ | &sum; |
| ∞ | &infin; | ∏ | &prod; |
| √ | &radic; |  |



Many of the symbols in the Windows "Symbol" font commonly used for rendering mathematics (such as the expandable bracket parts) are not present on most other machines, and not even present in [Unicode](/unicode) 3.1 or as HTML named entities (though they are planned for Unicode 3.2). These are used by products such as [TtH](/tth) to render equations. You should be aware that if you use these symbols, you are restricting your audience to Windows users (whether or not that's acceptable is a judgment you will have to make as an author).

## Other common symbols


Some characters such as the bullet, [Euro](/euro) currency sign, and trade mark sign are special cases. They are likely to be understood and rendered in some way by many browsers. Because they are important for international trade, many computers specifically add them to fonts at some non-standard location and render them when requested, or else render them in special ways that don't require them to be present in a font. See below for how your browser renders these:



|  |  |  |
| --- | --- | --- |
| • | &bull; | [bullet](/bullet-typography) |
| € | &euro; | [euro currency sign](/euro-currency-sign) |
| ™ | &trade; | [trade mark sign](/trade-mark-sign) |



Other somewhat less commonly used symbols include these:



|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| † | &dagger; | [dagger](/dagger-typography) |  | ♠ | &spades; | black spade suit |
| ‡ | &Dagger; | [double dagger](/dagger-typography) | ♣ | &clubs; | black club suit |
| ◊ | &loz; | lozenge | ♥ | &hearts; | black heart suit |
| ← | &larr; | leftward arrow | ♦ *or* ♦ | &diams; *or* (see below) | red diamond suit |
| ↑ | &uarr; | upward arrow | ‹ | &lsaquo; | single left-pointing angle quote |
| → | &rarr; | rightward arrow | › | &rsaquo; | single right-pointing angle quote |
| ↓ | &darr; | downward arrow | ‰ | &permil; | [per mille sign](/per-mille-sign) |



These should be considered unsafe to use except perhaps on pages intended for a specific audience likely to have very up-to-date software on popular machines. Even then, in some cases, [IE](/internet-explorer) 6.0 does not show the diamond symbol above. The regular diamond ♦ displays in [IE](/internet-explorer) 5 but not 6. The alternative code for the red diamond ♦, which works in IE 6 but not 5, is <font face="Sans-serif" color="red">&diams;</font>.

## Unicode


The official [character set](/character-set) of [HTML 4.01](/http-www-w3-org-tr-html4-charset-html) is the [ISO 10646](/iso-10646) [Universal Character Set](/ucs), which is equivalent to the character set defined by [Unicode](/unicode).
Many browsers, though, are only capable of displaying a small subset of the full UCS [repertoire](/repertoire).

For example, the codes `&#1049; &#1511; &#1605;` display on your browser as **Й**, **ק**, and **م**, which ideally look like the [Cyrillic](/cyrillic-alphabet) letter "Short I", the [Hebrew](/hebrew-alphabet) letter "Qof", and the [Arabic](/arabic-alphabet) letter "Meem", respectively.
It is unlikely that your computer has all of those fonts and will display them all correctly, though it may display a subset of them. Because they are encoded according to the standard, though, they *will* display correctly on any system that is compliant and has the characters available.

Numeric character entity references are the only way to enter these characters into a Wiki page at present.
Note that encoding them using decimal rather than hexadecimal (e.g. `&#1049;` instead of `&#x419;`) will increase the number of browsers on which they will work.

These characters should not be used in Wikipedia pages unless they make no
difference to the understanding of the text, and are just extra information.

See [Unicode and HTML](/unicode-and-html) for character entities tables.

See [Wikipedia:Unicode numeric converter script](/wikipedia-unicode-numeric-converter-script) for a utility which generates the Wikipedia-compatible numeric encoding automatically.

## Advanced Entities



The following additional entities are available. On some browsers, these are converted to Unicode equivalents.

*[table missing]*

Special Note: The Del symbol ("nabla;"), among others, is not supported on Windows 95 or 98. It has been uploaded as an image, and can be referenced as [[Image:Del.gif]], which looks like this: [![Del.gif](/web/20060725221336im_/http://www.metaweb.com/wiki/upload/d/db/Del.gif)](del-gif).
However, the del symbol is usually found in formulae which are better facilitated using [Wikipedia:TeX markup](/wikipedia-tex-markup).

## [CJK](/cjk) characters



The Esperanto, Polish, Czech, Bosnian, Serb, Croat, Malayalam, Japanese, Chinese, and Korean wikis use UTF-8, so they can store CJK characters directly. The English wikipedia can not; instead, numerical codes for them (in the form &#xxxxx;) can be stored. CJK characters can automatically be converted to the numerical codes to be stored, but a special procedure has to be followed (a trick):

* put one or more CJK characters in the edit box;
* click "Show preview"; the result is "garbage" ([mojibake](/mojibake)) in the edit box as well as in the preview;
* enter the desired text in the edit box while leaving the garbage there;
* click "Show preview" again; as a result, in addition to the previously seen garbage, numerical codes appear in the edit box, and the CJK characters in the preview;
* delete the garbage and save (if you want to be sure, click "Show preview" again before you save).


*This entry originally from the [Wikipedia](/http-www-wikipedia-org)*
