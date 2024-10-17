
# Real number

From the Quicksilver Metaweb.

this is a page for math and mathheads  **real number**
### Real number

 
From Wikipedia, the free encyclopedia.

In mathematics, the **real numbers** are intuitively defined as numbers that are in one-to-one correspondence with the points on an infinite line  the number line. The term "real number" is a retronym coined in response to "imaginary number ". 

Real numbers may be rational or irrational; algebraic or transcendental; and positive, negative, or zero. 

Real numbers measure continuous quantities. They may in theory be expressed by decimal fractions that have an infinite sequence of digits to the right of the decimal point; these are often (mis-)represented in the same form as 324.823211247... (where the three dots express that there would still be more digits to come, no matter how many more might be added at the end). 

Measurements in the physical sciences are almost always conceived as approximations to real numbers. Writing them as decimal fractions (which are rational numbers that could be written as ratios, with an explicit denominator) is not only more compact, but to some extent expresses the sense of an underlying real number. It is as if one says "I'm writing down only the part of the number that I know; it's infinitely long, and my stopping after a finite number of digits echoes the fact that I'm stopping short of doing more and more refined experiments forever, and getting further along in the infinite series of digits, which would be the only way to avoid an approximate final result." 

The real numbers are the central object of study in real analysis. 

A real number is said to be *computable* if there exists an algorithm that yields its digits. Because there are only countably many algorithms, but an uncountable number of reals, most real numbers are not computable. Some constructivists accept the existence of only those reals that are computable. The set of definable numbers is broader, but still only countable. 

Computers can only approximate most real numbers with rational numbers; these approximations are known as floating point numbers or fixed-point numbers; see real data type. Computer algebra systems are able to treat some real numbers exactly by storing an algebraic description (such as "sqrt(2)") rather than their decimal approximation. 

Mathematicians use the symbol **R** (or alternatively,![ \Bbb{R} ](/web/20060725171055im_/http://www.metaweb.com/wiki/upload/math/69a45f1e602cd2b2c2e67e41811fd226.png)  the letter  **R**  in [blackboard bold](/http-en-wikipedia-org-wiki-blackboard-bold))" to represent the [set](/http-en-wikipedia-org-wiki-set) of all real numbers. 

In mathematics, the term "real XXX" means that the underlying number field is the field of real numbers. For example real matrix, real polynomial and real Lie algebra. 

### History

 
Fractions had been used by the Egyptians around 1000 BC; around 500 BC, the Greek mathematicians lead by Pythagoras realized the need for irrational numbers. Negative numbers began to be generally accepted in the 1600s and were invented by Muslim mathematicians. The development of the [calculus](/calculus) in the 1700s used the entire set of real numbers without having defined them cleanly. The first rigorous definition was given by Georg Cantor in 1871. 

### Definition


#### Construction from the rational numbers

 
Real numbers could be constructed as the topological completion of rational numbers. For details and other construction of real numbers, see [Construction of real numbers](/http-en-wikipedia-org-wiki-construction-of-real-numbers)

Axiomatic approach 
Let **R** denote the [set](/http-en-wikipedia-org-wiki-set) of all real numbers. Then:
* The set **R** is a field, i.e., addition, subtraction, multiplication and division are defined and have the usual properties.
* The field **R** is ordered, i.e., there is a total order ≥ such that, for all real numbers *x*, *y* and *z*:
	+ if *x* ≥ *y* then *x* + *z* ≥ *y* + *z*;
	+ if *x* ≥ 0 and *y* ≥ 0 then *x**y* ≥ 0.
* The order is Dedekind-complete, i.e., every non-empty subset *S* of **R** with an [upper bound](/http-en-wikipedia-org-wiki-upper-bound) in **R** has a least upper bound (also called supremum) in **R**.


The latter property is what differentiates the reals from the rationals. For example, the set of rationals with square less than 2 has a rational upper bound (e.g., 1.5) but no rational least upper bound, because the square root of 2 is not rational.

The real numbers are uniquely specified by the above properties.
More precisely, given any two Dedekind complete ordered fields **R**1 and **R**2, there exists a unique field isomorphism from **R**1 to **R**2, allowing us to think of them as essentially the same mathematical object.

### Properties


#### Completeness



The main reason for introducing the reals is that the reals contain all limits.
More technically, the reals are complete (in the sense of metric spaces or uniform spaces, which is a different sense than the Dedekind completeness of the order in the previous section).

This means the following:

A sequence (*x**n*) of real numbers is called a *Cauchy sequence* if for any ε > 0 there exists an integer *N* (possibly depending on ε) such that the distance |*x**n* - *x**m*| is less than ε provided that *n* and *m* are both greater than *N*.
In other words, a sequence is a Cauchy sequence if its elements *x**n* eventually come and remain arbitrarily close to each other.

A sequence (*x**n*) *converges to the limit* *x* if for any ε > 0 there exists an integer *N* (possibly depending on ε) such that the distance |*x**n* - *x*| is less than ε provided that *n* is greater than *N*.
In other words, a sequence has limit *x* if its elements eventually come and remain arbitrarily close to *x*.

It is easy to see that every convergent sequence is a Cauchy sequence.
Now the important fact about the real numbers is that the converse is true: 
**Every Cauchy sequence of real numbers is convergent.**
That is, the reals are complete.

Note that the rationals are not complete.
For example, the sequence (1,1.4,1.41,1.414,1.4142,1.41421,...) is Cauchy but it does not converge to a rational number.
(In the real numbers, in contrast, it converges to the square root of 2.)

The existence of limits of Cauchy sequences is what makes [calculus](/calculus) work and is of great practical use.
The standard numerical test to determine if a sequence has a limit is to test if it is a Cauchy sequence, as the limit is typically not known in advance.

For example the standard series of the exponential function

 ![e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}](/web/20060725171055im_/http://www.metaweb.com/wiki/upload/math/5aabbba1c9ecaa6eada89d7665e04ef3.png)

converges to a real number because for every *x* the sums

 ![\sum_{n=N}^{M} \frac{x^n}{n!}](/web/20060725171055im_/http://www.metaweb.com/wiki/upload/math/b33758377a345927bd1dde05dcf6c63a.png)

can be made arbitrarily small by choosing *N* sufficiently large.
This proves that the sequence is Cauchy, so we know that the sequence converges even if we don't know ahead of time what the limit is.

#### "The complete ordered field"



The real numbers are often described as "the complete ordered field", a phrase that can be interpreted in several ways.

First, an order can be lattice complete.
It's easy to see that no ordered field can be lattice complete, because it can have no largest element (given any element *z*, *z* + 1 is larger).
So this is not the sense that is meant.

Additionally, an order can be Dedekind-complete, as defined in the section **Axioms**.
The uniqueness result at the end of that section justifies using the word "the" in the phrase "complete ordered field" when this is the sense of "complete" that is meant.
This sense of completeness is most closely related to the construction of the reals from Dedekind cuts, since that construction starts from an ordered field (the rationals) and then forms the Dedekind-completion of it in a standard way.

These two notions of completeness ignore the field structure.
However, an ordered [(mathematics) group](/http-en-wikipedia-org-wiki-group) (and a field is a group under the operations of addition and subtraction) defines a [uniform](/http-en-wikipedia-org-wiki-uniform-space) structure, and uniform structures have a notion of [topological completeness](/http-en-wikipedia-org-wiki-completeness-topology); the description in the section **Completeness** above is a special case.
(We refer to the notion of completeness in uniform spaces rather than the related and better known notion for metric spaces, since the definition of metric space relies on already having a characterisation of the real numbers.)
It is not true that **R** is the *only* uniformly complete ordered field, but it is the only uniformly complete *[Archimedean](/archimedean)* field, and indeed one often hears the phrase "complete Archimedean field" instead of "complete ordered field".
Since it can be proved that any uniformly complete Archimedean field must also be Dedekind complete (and vice versa, of course), this justifies using "the" in the phrase "the complete Archimedean field".
This sense of completeness is most closely related to the construction of the reals from Cauchy sequences (the construction carried out in full in this article), since it starts with an Archimedean field (the rationals) and forms the uniform completion of it in a standard way.

But the original use of the phrase "complete Archimedean field" was by [David Hilbert](/http-en-wikipedia-org-wiki-david-hilbert), who meant still something else by it.
He meant that the real numbers form the *largest* Archimedean field in the sense that every other Archimedean field is a subfield of **R**.
Thus **R** is "complete" in the sense that nothing further can be added to it without making it no longer an Archimedean field.
This sense of completeness is most closely related to the construction of the reals from surreal numbers, since that construction starts with a proper class that contains every ordered field (the surreals) and then selects from it the largest Archimedean subfield.

#### [Advanced properties](/http-en-wikipedia-org-wiki-real-number-advanced-properties)


The reals are [uncountable](/http-en-wikipedia-org-wiki-uncountable), that is, there are strictly more real numbers than [natural numbers](/http-en-wikipedia-org-wiki-natural-number) (even though both sets are [infinite](/http-en-wikipedia-org-wiki-infinity)).
This is proved with [Cantor's diagonal argument](/http-en-wikipedia-org-wiki-cantor-s-diagonal-argument).

In fact, the cardinality of the reals is 2ω (see [cardinal\_number cardinal numbers](/http-en-wikipedia-org-wiki)), i.e., the cardinality of the set of subsets of the [natural numbers](/http-en-wikipedia-org-wiki-natural-number).

Since only a countable set of real numbers can be [algebraic](/http-en-wikipedia-org-wiki-algebraic-number), [almost all](/http-en-wikipedia-org-wiki-almost-all) real numbers are [transcendental](/http-en-wikipedia-org-wiki-transcendental-number).

The nonexistence of a subset of the reals with cardinality strictly in between that of the integers and the reals is known as the [continuum hypothesis](/http-en-wikipedia-org-wiki-continuum-hypothesis).

This can neither be proved nor be disproved, but is independent from the axioms of [set theory](/http-en-wikipedia-org-wiki-set-theory).

The real numbers form a [metric space](/http-en-wikipedia-org-wiki-metric-space): the distance between *x* and *y* is defined to be the [absolute value](/http-en-wikipedia-org-wiki-absolute-value) **|***x* - *y***|**.

By virtue of being a [totally ordered](/http-en-wikipedia-org-wiki-total-order) set, they also carry an [order topology](/http-en-wikipedia-org-wiki-order-topology); the [topology](/http-en-wikipedia-org-wiki-topology) arising from the metric and the one arising from the order are identical.
The reals are a [contractible](/http-en-wikipedia-org-wiki-contractible) (hence [connected](/http-en-wikipedia-org-wiki-connected) and [simply connected](/http-en-wikipedia-org-wiki-simply-connected)), [locally compact](/http-en-wikipedia-org-wiki-local-compactness) [separable](/http-en-wikipedia-org-wiki-separable) metric space, of [dimension](/http-en-wikipedia-org-wiki-dimension) 1, and are [everywhere dense](/http-en-wikipedia-org-wiki-first-category).
The real numbers are not [compact](/http-en-wikipedia-org-wiki-compact-space).

There are various properties that uniquely specify them; for instance, all unbounded, continuous, and separable [order topologies](/http-en-wikipedia-org-wiki-total-order) are necessarily [homeomorphic](/http-en-wikipedia-org-wiki-homeomorphic) to the reals.

Every nonnegative real number has a [square root](/http-en-wikipedia-org-wiki-square-root) in **R**, and no negative number does.

This shows that the order on **R** is determined by its algebraic structure.

Also, every polynomial of odd degree admits at least one root: these two properties make **R** the premier example of a [real closed field](/http-en-wikipedia-org-wiki-real-closed-field).
Proving this is the first half of one proof of the [fundamental theorem of algebra](/http-en-wikipedia-org-wiki-fundamental-theorem-of-algebra).

The reals carry a canonical [measure](/http-en-wikipedia-org-wiki-measure), the [Lebesgue measure](/http-en-wikipedia-org-wiki-lebesgue-measure), which is the [Haar measure](/http-en-wikipedia-org-wiki-haar-measure) on their structure as a [topological group](/http-en-wikipedia-org-wiki-topological-group) normalised such that the [unit interval](/http-en-wikipedia-org-wiki-unit-interval) [0,1] has measure 1.

The supremum axiom of the reals refers to subsets of the reals and is therefore a second-order logical statement.

It is not possible to characterize the reals with [first-order logic](/http-en-wikipedia-org-wiki-first-order-logic) alone: the [Löwenheim-Skolem theorem](/http-en-wikipedia-org-wiki-l-ouml-wenheim-skolem-theorem) implies that there exists a countable dense subset of the real numbers satisfying exactly the same sentences in first order logic as the real numbers themselves.

The set of [hyperreal numbers](/hyperreal-number) is much bigger than **R** but also satisfies the same first order sentences as **R**.

Ordered fields that satisfy the same first-order sentences as **R** are called [nonstandard models](/http-en-wikipedia-org-wiki-nonstandard-model) of **R**.
This is what makes [Non-standard analysis](/non-standard-analysis) work; by proving a first-order statement in some nonstandard model (which may be easier than proving it in **R**), we know that the same statement must also be true of **R**.
