
# Heinlein:Robert:Have Space Suit Will Travel:40:Almost halfway to the Moon, I'd say (Neal Stephenson)

From the Quicksilver Metaweb.

Heinlein is having some fun here with an important idea from physics, namely: [Einstein's Principle of Equivalence](/einstein-s-principle-of-equivalence).

Kip wakes up in a sealed room, and thinks he is at rest on the surface of the earth, because the room doesn't feel like it's moving, and he seems to weigh the same as he normally does. If he were to take a penny out of his pocket and drop it, it would fall to the floor in the way that he is accustomed to.

Peewee informs him that he is actually in a cabin of a spaceship that is in transit between the earth and the moon! What Kip mistakes for normal earth gravity is actually an illusion created by the fact that the ship is undergoing a constant [acceleration](/acceleration) toward the moon at 1 [gee (G)](/gee-g), which is to say, about 9.8 [meters per second squared](/meters-per-second-squared). His "weight" is not caused by gravity but by the fact that the deck of the spaceship is pressing him "up"-wards. The "fall" of the coin is not caused by the earth's gravity pulling it down but by the fact that, once Kip lets it go, the deck of the ship accelerates "up"-wards and smacks into it.

Kip's confusion is wholly understandable, for he has been dropped into a [Gedankenexperiment](/gedankenexperiment) that is important to modern physics. The point of it is that gravity and acceleration are equivalent. For explanations, visit the link [Principle of Equivalence Gedankenexperiment](/principle-of-equivalence-gedankenexperiment).

Peewee says that travel time between Earth and Moon, on this ship, is going to be almost exactly three and a half hours. Let's see if we can check her math.

This calculation could become a little complicated if we take into account the gravity of the Earth and the Moon, and the fact that the Moon is a moving target. But let's begin with a very rough back-of-envelope calculation.

According to *Encyclopedia of Planetary Sciences*, ([ISBN 0412069512](/)) the Moon's average distance from the Earth is 284,000,000 m. This is the distance from the center of the Earth to the center of the Moon.

(the following digression may be skipped: of course, Kip and Peewee are traveling from the *surface* of the Earth to the *surface* of the Moon, so the distance is going to be a little different. But we don't know any of the details that we would need to figure out the exact straight-line distance; depending on what time of day they leave Earth, and where the Moon is in the sky, it could be greater than or less than 284,000,000 m by an amount on the order of the Earth's radius! But the Earth's radius is only about one sixtieth of the Earth-Moon distance and so we can leave this out of our crude calculation. End of digression!)

The only other fact we need to know is presented in the book: the ship accelerates toward the Moon at one gee until it is halfway there--so a distance of 142,000,000 m---then flips around and decelerates until it reaches its destination.

This sort of problem is easily handled by some basic formulas from [kinematics](/kinematics), which define the relationships among [position](/position), [velocity](/velocity), and [acceleration](/acceleration). The problem would be harder, and would require the use of [calculus](/calculus) or some sort of [numerical techniques](/numerical-techniques), if the ship's acceleration were not [constant](/constant). But it is made clear in Heinlein's book that the acceleration never changes. So we will denote it by the symbol a.

Another thing that makes this problem easy is that the ship moves in a straight line, and so it is a one-dimensional scenario. If this were not the case we would have to employ some [vector](/vector) math, but because it's one-dimensional we can consider the acceleration a to be a [scalar](/scalar). We can make the same assumption of the distance (position), which we'll denote by the symbol d.

A basic result of [kinematics](/kinematics) then tells us

![d = {1\over2}at^2](/web/20060725172429im_/http://www.metaweb.com/wiki/upload/math/dcf3835fc0c51ccef1b21ca2899e7ac0.png)

We already know the distance d (halfway to the moon, or 142,000,000 meters) and the acceleration a (1 gee, or about 9.8 meters per second per second) and would like to calculate the time t. We can do this by rearranging the formula shown above using some simple [algebra](/algebra). The expression

![t=\sqrt{2d\over a}](/web/20060725172429im_/http://www.metaweb.com/wiki/upload/math/68f238f9d9a4f029cba6a2f0701645ca.png)

is equivalent to the one shown above, as long as d/a is a positive number. If we insert our known values of d and a, we get

![t = \sqrt{2\times 142000000\over 9.8}\simeq 5383\ seconds](/web/20060725172429im_/http://www.metaweb.com/wiki/upload/math/a5c05e7df6d44124876326c8b47b17e1.png)

This time, 5383 seconds, is equal to 1 hour, 29 minutes, and 43 seconds. This is about a quarter of an hour short of Peewee's estimate in the book (she estimates three and half hours for the full trip, which means it should take 1 hour and 45 minutes to get halfway there) but given all of the approximations that are involved here, this is close enough to suggest that we are on the same page as Peewee.

When we say that something is accelerating at 9.8 meters per second per second, what it means is that with each second that goes by, its velocity increases by 9.8 m/s. Since this happens for 5383 seconds, the velocity achieved by this ship at the halfway point of the journey is

![9.8\ m/{s^2}\times 5383\ s = 52753\ m/s](/web/20060725172429im_/http://www.metaweb.com/wiki/upload/math/4483901569d803dc7b4dfffa3b89479d.png)

Just to place this in perspective, the velocity of something that is in a circular [low earth orbit (LEO)](/low-earth-orbit-leo) is more like 8000 m/s. In order to achieve [escape velocity](/escape-velocity) from the Earth, it need go only a little faster---upwards of 11,000 m/s. The alien pirate spaceship that has abducted Kip and Peewee is going almost five times as fast as that when it reaches its peak velocity.

The formula for [kinetic energy](/kinetic-energy) states that the amount of energy a moving object has goes up as its velocity [squared](/squared). So when we say that this alien spaceship is going almost 5 times as fast as [escape velocity](/escape-velocity), what we are saying is that it has got almost 25 times as much energy as it would need to escape from Earth's gravity.

Such energies are not achievable by any rocket engines known to Kip, and so implicit in all of this is that the aliens have vastly more advanced propulsion technology than anything that Kip knows about.
