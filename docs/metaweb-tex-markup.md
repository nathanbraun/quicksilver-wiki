
# Metaweb:TeX markup

From the Quicksilver Metaweb.



**This page is deprecated but will be updated periodically.**
**Please direct edits to the [Meta-Wikimedia version of this page](/)**

*<< [Wikipedia:Multimedia](/wikipedia-multimedia)*

As of January 2003, we have **[TeX](/tex) markup** for mathematical formulas on Wikipedia. It generates either [PNG](/png) images or simple [HTML](/html) markup, depending on user prefs and the complexity of the expression. In the future, as more browsers are smarter, it will be able to generate enhanced HTML or even [MathML](/mathml) in many cases.

Math markup goes inside <math> ... </math>. Line breaks within these tags are fine, and aren't rendered. They're a good idea to keep the raw markup clear (for instance, a line break after each term or row of a matrix).

Discussion, bug reports and feature requests should go to the [Wikitech-l mailing list](/wikipedia-mailing-lists) or to [Wikipedia:TeX requests](/wikipedia-tex-requests).

For style issues regarding the typesetting of math, see [Wikipedia:WikiProject Mathematics](/wikipedia-wikiproject-mathematics). In particular, please avoid using this feature as part of a line of regular text, as the formulas don't align properly and the font is too large.

Regarding color, notice that this page is a special page (its name begins with "Wikipedia:") and has therefore a yellow background. Normal Wikipedia pages are white, just like the formulas, so don't worry.


## Special characters




| Feature | Syntax | How it looks rendered |
| --- | --- | --- |
| std. functions (good) | \sin x + \ln y +\operatorname{sgn} z | \sin x + \ln y +\operatorname{sgn} z |
| std. functions (wrong) | sin x + ln y + sgn z | sin x + ln y + sgn z\, |
| Derivatives | \nabla \partial dx | \nabla \partial dx |
| Sets | \forall x\not\in\empty\subseteq A\cap B\cup \exists \{x,y\}
\times C | \forall x \not\in \empty \subseteq A\cap B\cup \exists
\{x,y\} \times C |
| Logic | p\wedge \bar{q} \rightarrow p\vee \bar{q} \Rightarrow \Leftrightarrow  | p\wedge \bar{q} \rightarrow p\vee \bar{q} \Rightarrow
\Leftrightarrow |
| Root | \sqrt{2}\approx 1.4 | \sqrt{2}\approx 1.4 |
| \sqrt[n]{x} | \sqrt[n]{x} |
| Relations | \sim \simeq \cong \le \ge \equiv \approx \ne |  \sim \ \simeq \ \cong \ \le \ \ge \ \equiv \ \approx \ \ne |
| Geometric | \angle \perp \| | \angle \perp \| |
| Special | \oplus \otimes \pm \mp \hbar \dagger \ddagger \star \circ \cdot
\bullet \infty | \oplus \otimes \pm \mp \hbar \dagger \ddagger \star \circ
\cdot \bullet\ \infty |


## Subscripts, superscripts




| Feature | Syntax | How it looks rendered |
| --- | --- | --- |
| Superscript | a^2 | *a*2 |
| Subscript | a\_2 | *a*2 |
| Grouping | a^{2+2} | *a*2 + 2 |
| a\_{i,j} | *a**i*,*j* |
| Combining sub & super | x\_2^3 | x_2^3 |
| Derivative (good) | x' | *x*' |
| Derivative (wrong in HTML) | x^\prime | x^\prime |
| Derivative (wrong in PNG) | x\prime | x\prime |
| Sum | \sum\_{k=1}^N k^2 | \sum_{k=1}^N k^2 |
| Product | \prod\_{i=1}^N x\_i | \prod_{i=1}^N x_i |
| Limit | \lim\_{n \to \infty}x\_n | \lim_{n \to \infty}x_n |
| Integral | \int\_{-N}^{N} e^x\, dx | \int_{-N}^{N} e^x\, dx |
| Line Integral | \oint\_{C} x^3\, dx + 4y^2\, dy | \oint_{C} x^3\, dx + 4y^2\, dy |


## Fractions, matrices, multilines




| Feature | Syntax | How it looks rendered |
| --- | --- | --- |
| Fractions | \frac{2}{4} or {2 \over 4} | \frac{2}{4} |
| Binomial coefficients | \binom{n}{k} or {n \choose k} | {n \choose k} |
| Matrices | \begin{pmatrix} x & y \\ z & v \end{pmatrix} | \begin{pmatrix} x & y \\ z & v
\end{pmatrix} |
| \begin{bmatrix} 0 & \cdots & 0 \\ \vdots &
\ddots & \vdots \\ 0 & \cdots &
0\end{bmatrix} | \begin{bmatrix} 0 & \cdots & 0 \\ \vdots
& \ddots & \vdots \\ 0 & \cdots &
0\end{bmatrix}  |
| \begin{Bmatrix} x & y \\ z & v \end{Bmatrix} | \begin{Bmatrix} x & y \\ z & v
\end{Bmatrix} |
| \begin{vmatrix} x & y \\ z & v \end{vmatrix} | \begin{vmatrix} x & y \\ z & v
\end{vmatrix} |
| \begin{Vmatrix} x & y \\ z & v \end{Vmatrix} | \begin{Vmatrix} x & y \\ z & v
\end{Vmatrix} |
| \begin{matrix} x & y \\ z & v \end{matrix} | \begin{matrix} x & y \\ z & v
\end{matrix} |
| Case distinctions | f(n)=\left\{\begin{matrix} n/2, & \mbox{if }n\mbox{ is
even} \\ 3n+1, & \mbox{if }n\mbox{ is odd}
\end{matrix}\right. | f(n)=\left\{\begin{matrix} n/2, & \mbox{if }n\mbox{ is even} \\ 3n+1, & \mbox{if }n\mbox{ is odd} \end{matrix}\right.  |
| Multiline equations | \begin{matrix}f(n+1)&=& (n+1)^2 \\ \ &
=& n^2 + 2n + 1\end{matrix} | \begin{matrix}f(n+1)&=& (n+1)^2 \\ \ & =& n^2 + 2n + 1\end{matrix} |


## Fonts




| Feature | Syntax | How it looks rendered |
| --- | --- | --- |
| [Greek letters](/greek-alphabet) | \alpha \beta \gamma \Gamma \phi \Phi \Psi\ \tau \Omega | \alpha\ \beta\ \gamma\ \Gamma\ \phi\ \Phi\ \Psi\ \tau\ \Omega |
| [Blackboard bold](/blackboard-bold) | x\in\mathbb{R}\sub\mathbb{C} | x\in\mathbb{R}\subset\mathbb{C} |
| [boldface](/boldface) (vectors) | \mathbf{x}\cdot\mathbf{y} = 0 | \mathbf{x}\cdot\mathbf{y} = 0 |
| boldface (greek) | \boldsymbol{\alpha}+\boldsymbol{\beta}+\boldsymbol{\gamma} | \boldsymbol{\alpha}+\boldsymbol{\beta}+\boldsymbol{\gamma} |
| [Fraktur typeface](/fraktur-typeface) | \mathfrak{a} \mathfrak{A} \mathfrak{B} | \mathfrak{a} \mathfrak{A} \mathfrak{B} |
| Script | \mathcal{ABC} | \mathcal{ABC} |
| [Hebrew](/hebrew-alphabet) | \aleph \beth \gimel \daleth | \aleph\ \beth\ \gimel\ \daleth |
| non-italicised characters | \mbox{abc} | abc |


## Parenthesizing big expressions




| Feature | Syntax | How it looks rendered |
| --- | --- | --- |
| Not good | ( \frac{1}{2} ) | ( \frac{1}{2} ) |
| Better | \left( \frac{1}{2} \right) | \left ( \frac{1}{2} \right ) |


You can use various delimiters with \left and \right: 


| Feature | Syntax | How it looks rendered |
| --- | --- | --- |
| Parentheses | \left( A \right) | \left( A \right) |
| Brackets | \left[ A \right] | \left[ A \right] |
| Braces | \left\{ A \right\} | \left\{ A \right\} |
| Angle brackets | \left\langle A \right\rangle | \left\langle A \right\rangle |
| Bars | \left| A \right| | \left| A \right| |
| Use \left. and \right. if you don't want a delimiter to
appear: | \left. {A \over B} \right\} \to X | \left. {A \over B} \right\} \to X |


## Spacing


Note that TeX handles most spacing automatically, but you may sometimes want manual control. 


| Feature | Syntax | How it looks rendered |
| --- | --- | --- |
| double quad space | a \qquad b | a \qquad b |
| quad space | a \quad b |  a \quad b |
| text space | a\ b | a\ b |
| large space | a\;b | a\;b |
| medium space | a\>b | [not supported] |
| small space | a\,b | a\,b |
| no space | ab | ab\, |
| negative space | a\!b | a\!b |



## See also:


* Proposed [Wikipedia:GNU LilyPond support](/wikipedia-gnu-lilypond-support)


## External Links


* A [PDF](/portable-document-format) document introducing TeX -- see page 39 onwards for a good introduction to the maths side of things: [http://www.ctan.org/tex-archive/info/gentle/gentle.pdf](/http-www-ctan-org-tex-archive-info-gentle-gentle-pdf)
* Various extensions to LaTeX: [http://www.ams.org/tex/amslatex.html](/http-www-ams-org-tex-amslatex-html)
* A set of public domain fixed-size math symbol bitmaps: [http://us.metamath.org/symbols/symbols.html](/http-us-metamath-org-symbols-symbols-html)
* TeX Wizard: [http://de.geocities.com/richyfourtythree/texwizard.html](/http-de-geocities-com-richyfourtythree-texwizard-html)


*This entry originally from the [Wikipedia](/http-www-wikipedia-org)*
