# lecture 1 - the security mindset

#### goals for this course

critical thinking

-   how to think like an attacker
-   how to reason about threats and risks
-   how to balance secuity costs and benefits

#### what is computer security

-   security is a property that holds in a given system a set of constraints
    -   system: hardware, software, firmware, etc.
    -   constraints: define an adversary and thier capabillties
-   can also mean the measures and the controls that ensure these properties
-   security doesnt explicityly study other properties, ie correctness and performance

#### meet the adversary

computer security studies how systems beahve in the presense of an adversary

know your enemy

-   motives
-   capabilities
-   degrees of access

#### thinking like an attacker

-   look for the weakest links
-   identify assymptions/preconditions that security depends on
-   think outside the box

#### thinking like a defender

-   security policy: what are we trying to protect and what properties are we trying to enforce
-   threat model: who are the attackers, what kinds of attacks should we ignore?
-   risk assessment: what weaknesses exist
    -   what would security breaches cost us, direct: money & indirect: reputation
    -   how likely are these costs, P(attack), P(success)
-   countermeasures: technical vs non technical
    -   non technical: law, policy, procedures
    -   no security mechanism is free, direct cost: design, implementation etc, indirect cost: lost productivity, added complexity
    -   cost vs risk, human psychology makes reasoning about high cost/low probabilty events hard
-   rational paranoia

#### the security mindset

thinking like an attacker

-   understand techniques to circumventing security
-   look for ways to break security, not reasons it won't

thinking like a defender

-   know what you're defending and from who
-   understand cost benefit of security
-   rational paranoia