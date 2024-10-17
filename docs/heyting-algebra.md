
# Heyting algebra

From the Quicksilver Metaweb.

In mathematics, **Heyting algebras** are a generalization of [Boolean algebras](/boolean-algebra). Heyting algebras model intuitionistic logic, in which the [law of excluded middle](/law-of-excluded-middle) does not in general hold.

Formally, a Heyting algebra is a bounded lattice *L* such that for all *a* and *b* in *L* there is a greatest element *x* of *L* such that *a* ∧ *x* ≤ *b*. This element is called the relative pseudo-complement of *a* with respect to *b*, and is denoted *a*⇒*b* (or *a*→*b*). We write ¬*a* for *a*⇒0. Heyting algebras are always distributive; this is sometimes stated as an axiom, but in fact it follows from the existence of relative pseudo-complements.

Boolean algebras are those Heyting algebras in which *x* = ¬¬*x* for all *x*, or, equivalently, in which *x* ∨ ¬*x* = 1 for all *x*. In this case, the element *a*⇒*b* is equal to ¬*a* ∨ *b*.

Every topology is also a Heyting algebra. In this case, the element *A*⇒*B* is the interior of *A*c∪*B*, where *A*c denotes the complement of the open set *A*.
