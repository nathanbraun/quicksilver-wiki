
# Hyperreal number

From the Quicksilver Metaweb.

I'm sure these all come into play in cracking codes - a page for the **hyperreal number**
### Hyperreal number

 
From Wikipedia, the free encyclopedia. 

The **hyperreal numbers** or **nonstandard reals** (usually denoted as ***R**) are an extension of the [real numbers](/real-number) **R** that adds infinitely large as well as [infinitesimal](/infinitesimal) numbers to **R**. The study of these numbers, their functions and properties is called [non-standard analysis](/non-standard-analysis) which some find more intuitive than standard real analysis. When [Isaac Newton](/isaac-newton) and [Gottfried Leibniz](/gottfried-wilhelm-von-leibniz) introduced differentials, they used infinitesimals and these were still regarded as useful by Leonhard Euler and Augustin Louis Cauchy. Nonetheless these concepts were from the beginning seen as suspect, notably by [Bishop Berkeley](/george-berkeley), and when in the 1800s [calculus](/calculus) was put on a firm footing through the development of the epsilon-delta definition of a limit by Augustin Louis Cauchy, Karl Weierstrass and others, they were largely abandoned.

However, in the 1960s Abraham Robinson showed how infinitely large and infinitesimal numbers can be rigorously defined and used to develop the field of nonstandard analysis. Because his theory in its full-fledged form makes unrestricted use of classical logic and set theory and, in particular, of the axiom of choice, it is suspected to be nonconstructive from the outset. The construction given below is a simplified version of Robinson's more general construction and is due to Lindstrom.

### Properties


The hyperreals ***R** form an ordered field containing the reals **R** as a subfield. Unlike the reals, the hyperreals do not form a metric space, but by virtue of their order they carry an order topology.

The hyperreals are defined in such a way that every true first-order logic statement that uses basic arithmetic (the natural numbers, plus, times, comparison) and quantifies only over the real numbers is also true if we presume that it quantifies over hyperreal numbers. For example, we can state that for every real number there is another number greater than it:

∀ *x* ∈ **R** : ∃ *y* ∈**R** : *x* < *y*

The same will then also hold for hyperreals:

∀*x* ∈ ***R** : ∃ *y* ∈***R** : *x* < *y*

Another example is the statement that if you add 1 to a number you get a bigger number:

∀ *x* ∈ **R** : *x* < *x* + 1

which will also hold for hyperreals:

∀ *x* ∈ ***R** : *x* < *x* + 1

This however doesn't mean that **R** and ***R** behave the same. For instance, in ***R** there exists an element *w* such that 
 1<w, 1+1<w, 1+1+1<w, 1+1+1+1<w, ...
but there is no such number in **R**. This is possible because the nonexistence of this number cannot be expressed as a first order statement of the above type. A hyperreal number like *w* is called infinitely large; the reciprocals of the infinitely large numbers are the infinitesimals.

### Construction



We are going to construct the hyperreals via sequences of reals. This is nice, because we can immediately identify the real number *r* with the sequence (*r*, *r*, *r*, ...) and we can also add and multiply sequences: (*a*0, *a*1, *a*2, ...) + (*b*0, *b*1, *b*2, ...) = (*a*0 + *b*0, *a*1 + *b*1, *a*2 + *b*2, ...) and analogously for multiplication. 

We also need to be able to compare sequences, and there we run into trouble: some entries of the first sequence may be bigger than the corresponding entries of the second sequence, and some others may be smaller. We have to specify "which positions matter". Since there are infinitely many indices, we don't want finite sets of indices to matter. A consistent choice of "index sets that matter" is given by any free ultrafilter *U* on the natural numbers which does not contain any finite sets. Such an *U* exists by the axiom of choice. (In fact, there are many such *U*, but it turns out that it doesn't matter which one we take.) We think of *U* as singling out those sets of indices that "matter": We write (*a*0, *a*1, *a*2, ...) ≤ (*b*0, *b*1, *b*2, ...) if and only if the set of natural numbers { *n* : *a**n* ≤ *b**n* } is in *U*. This is a total preorder and it turns into a total order if we agree not to distinguish between two sequences *a* and *b* if *a*≤*b* and *b*≤*a*. With this identification, the ordered field ***R** of hyperreals is constructed.

### Infinitesimal and infinite numbers


A nonstandard real number *e* is called *infinitesimal* if it is smaller than every positive real number and bigger than every negative real number. Zero is an infinitesimal, but non-zero infinitesimals also exist: take for instance the class of the sequence (1, 1/2, 1/3, 1/4, 1/5, 1/6, ...) (this works because *U* contains all index sets whose complement is finite). 

A non-standard real number *x* is called *finite* if there exists a natural number *n* such that – *n* < *x* < +*n*; otherwise, *x* is called *infinite*. Infinite numbers exist; take for instance the class of the sequence (1, 2, 3, 4, 5, ...). A non-zero number *x* is infinite if and only if 1/*x* is infinitesimal.

Now it turns out that every *finite* nonstandard real number is "very close" to a unique real number, in the following sense: if *x* is a finite nonstandard real, then there exists one and only one real number st(*x*) such that *x* – st(*x*) is infinitesimal. This number st(*x*) is called the *standard part* of *x*. This operation has nice properties:
* st(*x* + *y*) = st(*x*) + st(*y*) if both *x* and *y* are finite
* st(*xy*) = st(*x*) st(*y*) if both *x* and *y* are finite
* st(1/*x*) = 1 / st(*x*) if *x* is finite and not infinitesimal.
* the map st is continuous with respect to the order topology on the finite hyperreals.
* st(*x*) = *x* if and only if *x* is real.


### Related entries


* [Archimedean](/archimedean)
* [Archimedes](/archimedes)
* [Archimedes Palimpsest](/archimedes-palimpsest)
* [Arithmetickal Engine](/arithmetickal-engine)
* [Baruch de Spinoza](/baruch-de-spinoza)
* [Calculus](/calculus)
* [Princess Caroline](/caroline-of-ansbach)
* [David Gregory](/david-gregory)
* [Escape velocity](/escape-velocity)
* [George Berkeley](/george-berkeley)
* [King George I](/george-i-of-england)
* [Gottfried Wilhelm von Leibniz](/gottfried-wilhelm-von-leibniz)
* [Infinitesimal calculus](/infinitesimal-calculus)
* [Isaac Barrow](/isaac-barrow)
* [Isaac Newton](/isaac-newton)
* [John Keill](/john-keill)
* [Kilometer](/kilometer)
* [Kinetic energy](/kinetic-energy)
* [Lens](/lens)
* [Mass](/mass)
* [Mathematics](/mathematics)
* [Meters per second squared](/meters-per-second-squared)
* [The Priority Dispute](/newton-vs-leibniz)
* [Nicolas Fatio de Duillier](/nicolas-fatio-de-duillier)
* [Non-standard analysis](/non-standard-analysis)
* [Pierre-Simon Laplace](/pierre-simon-laplace)
* [Principia Mathematica](/principia-mathematica)
* [Roger Cotes](/roger-cotes)
* [Scientific principles](/scientific-principles)


### References and external links


* Abraham Robinson: *Nonstandard Analysis*, Princeton University Press 1996. The standard reference at a graduate school level.
* [Jordi Gutierrez Hermoso](/http-mathforum-org-dr-math-faq-analysis-hyperreals-html): *Nonstandard Analysis and the Hyperreals*  A gentle introduction.
