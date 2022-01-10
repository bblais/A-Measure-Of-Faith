# The case for Jesus

## Some first thoughts

I repeat the same thoughts with which I started last chapter, at the danger of being too repetitive, to remind you of the structure of the probability of belief.  It's good to keep looking at the big-picture of the structure of probability.  Ones belief in an explanation should increase with how well that explanation fits the data and how plausible it is before the data, but it should also *decrease* with all of the other ways the data can be explained by other descriptions. 

![](../images/bayes1.png){width=400px}

Recall that arguments fail primarily for a few reasons:

1. lack of imagination in constructing alternative explanations
2. ill-formed hypotheses where initial plausibilities can't be established
3. hypotheses that are too flexible and can fit any kind of data

And recall that the false-binary construction of an argument can hide many other alternatives  in "$\textbf{not } A$" part of the equations. Watch for these failures of proper reasoning!

Following up with his argument for the existence of God, Swinburne presents a probabilistic argument for the Resurrection.

### Summary of the Argument



> Now at the end of the day this book is interested in $P(h|e\&k)$ --the probability that Jesus was God Incarnate who rose from the dead ($h$), on the evidence both of natural theology ($k$) and of the detailed history of Jesus and of other human prophets ($e$)

For clarity, I prefer to use the letter $R$ for the primary claim that Jesus was risen from the dead, rather than $h$.  Since Swinburne is assuming the "evidence of natural theology" through the entire argument, we don't need the extra symbol $k$ -- we can subsume it into the "evidence."  Finally, in Swinburne's argument, he brings in two extra symbols: $c$ for the claim that God became incarnate and $f$ that "we have *claims* that there is evidence of the strength given by $e$."  Although I agree that we should always focus on what evidence we have (i.e. we have claims of events), Swinburne makes no use of these two extra symbols because near the end of the argument he makes the following two statements (in his notation):

> 1. $P(h|e \& k)$ will not be very different from $P(c|e \& k)$
>
> 2. It cannot make any difference to the probability that $f$ (with $k$) gives to $c$, if we add to $f$ [...] the details of the evidence [...] So, $P(c|e\&k)= P(c|f\&k)$ [...]

which effectively makes his two extra symbols redundant:  $f$ is equivalent to the evidence $e$, and $c$ is equivalent to the primary statement under analysis $h$.  After recognizing this, the basic structure of the argument follows the Bayes' Rule,

$$
P(R|\text{evidence}) = \frac{P(\text{evidence}|R)P(R)}{P(\text{evidence})}
$$
where $R$ is the statement

>  $R$: Jesus was God Incarnate who rose from the dead

where the evidence is

> The various data of natural theology:
>
> 1. the existence of a complex physical universe
> 2. the (almost invariable) conformity of material bodies to natural laws 
> 3. those laws together with the initial state of the universe being such as to lead to the evolution of human organisms
> 4. these humans having a mental life (and so souls)
> 5. these humans having great opportunities for helping or hurting each other
> 6.  these humans having experiences in which it seems to them that they are aware of the presence of God.
>
> The detailed historical evidence, consisting of a conjunction of three pieces of evidence
>
> 1. the evidence of the life of Jesus 
> 2. the detailed historical evidence relating to the Resurrection
> 3. the evidence that neither the prior nor the posterior requirements for being God Incarnate were satisfied in any prophet in human history in any way comparably with the way in which they were satisfied in Jesus. 

The math follows straightforwardly by addressing each term of the equation above,

The probability that if God became incarnate/was resurrected we would have the evidence we have, Swinburne suggests the ''fairly low'' number of 
$$
P(\text{evidence}|R) = \frac{1}{10}
$$
The prior probability of the resurrection  is broken up into two parts,
$$
P(R) = P(R|G)P(G)
$$
where the probability of God, $P(G)=1/2$, is the "modest" value taken from the previous work.  The first part, $P(R|G)$, is an attempt to divine the motivations of God, 

>Then let us represent by $c$ [in our simplified notation, $R$ ] the claim that God became incarnate among humans at some time with a divided incarnation, a more precise form of the way described by the Council of Chalcedon.  I suggested that it was 'as probable as not' that he would do this and so in numerical terms the probability of his doing it is $1/2$. 

Thus, Swinburne arrives at the prior probability of the resurrection,
$$
P(R) = P(R|G)P(G) = \frac{1}{2}\cdot\frac{1}{2}=\frac{1}{4}
$$
and by the negation rule,
$$
P({\bf not}\,R) = 1-P(R) = \frac{3}{4}
$$
The evidence terms are handled as

> How probable, then, is it that if God does become incarnate (into a human race sinning and suffering), we would have evidence of the strength described, connected with one and only one prophet? Let me not exaggerate my case and suggest (despite my strong feeling that this value should be higher) that we give it a fairly low value and put it provisionally at $1/10$

and

> But it would be immensely unlikely that there would be evidence of these degrees connected with the same prophet unless God so planned it. It would have been deceptive of God to bring about this combination of evidence (or permit some other agent to do so), unless he had become incarnate in this prophet; and so God would not have brought this about. So let's say $1/1000$.

which in our notation is

- $P(\text{evidence}|R)=1/10$
- $P(\text{evidence}|{\bf not}\,R)=1/1000$

We now have all the pieces to arrive at Swinburne's final answer,
$$
\begin{aligned}
P(R|\text{evidence}) &= \frac{P(\text{evidence}|R)P(R)}{P(\text{evidence})} \\
&= \frac{P(\text{evidence}|R)P(R)}{P(\text{evidence}|R)P(R)+P(\text{evidence}|{\bf not}\,R)P({\bf not}\,R)}\\
&= \frac{\frac{1}{10}\cdot \frac{1}{4}}{\frac{1}{10}\cdot \frac{1}{4}+\frac{1}{1000}\cdot \frac{3}{4}}\\
&= \frac{100}{103} \sim 97\%
\end{aligned}
$$


### Problems with the argument

The overall structure of the argument is, of course, sound.  Bayes' Rule will work but is only as good as the probabilities we assign.  The main problems with Swinburne's argument are that he *attempts to assign probabilities to the actions of God* and he *lacks imagination for alternatives*, thus skewing any probability assignments.  

#### The mind of God

For example,

> Then let us represent by $c$ [in our simplified notation, $R$ ] the claim that God became incarnate among humans at some time with a divided incarnation, a more precise form of the way described by the Council of Chalcedon.  I suggested that it was 'as probable as not' that he would do this and so in numerical terms the probability of his doing it is $1/2$. 

Swinburne puts great store in the idea that God would do things the Christian way.  He has entire chapters littered with phrases starting with "God will want to...," "...reason God would have for...," "...reasons which God might have for...,"etc...  We are told that the mind of God is inscrutable, so I find it unconvincing that Swinburne can read it so clearly and narrowly.  How do we know that an incarnate God is the best one?  Perhaps it would have been better if he had come down looking like an alien?  Why the particular miracle of raising from the dead?  Why not glowing skin, flying, or invincibility?  Although my suggestions sound suspiciously like Superman or someone from the X-Men, other than 20-20 hindsight[^posthoc] there really is no way to tell what the reasoning should be, thus making all probabilities based on that to be arbitrary.  As a game, try to come up with a rational argument for why it would be in God's plan to send Superman.  God would want an alien to stress the Fall of mankind, but would want the alien to appear human in all obvious ways.  God would want this representative to be invincible to give good evidence for the omnipotence of God himself, but be limited in space and time to give humans the free will to work on problems on their own.  One can keep going with this line of argument because it is completely unconstrained by any possibility of confirmation or disconfirmation.  

[^posthoc]:  which in philosophical circles is called post-hoc or "after-the-fact" reasoning.

#### The nature of the evidence

Another problem with Swinburne's argument is the selection of the evidence.  He claims that, if God doesn't exist, then the evidence we see would be highly unlikely.  Focussing on the Resurrection specifically,

> So, while the fact that the universal agreement on the fact of Jesus' Resurrection, and that there were many witnesses thereof, is good evidence of its truth, the existence of somewhat different versions of to whom he appeared, and when, do little to lessen the force of that evidence unless they are too much at odds with each other. The band of followers of Jesus, routed by his
> Crucifixion, had become enthusiastic missionaries for a Gospel centred on the Resurrection of Jesus. This requires explanation. 

He admits that there may be some detailed alternative story, 

> But such a story, even if it is made so elaborate as to make the evidence probable, becomes thereby highly complicated and so highly improbable a priori. Only if any other hypothesis were even more improbable should we adopt this one. 
>
> The traditional account does not have these disadvantages of complexity. If Jesus did indeed rise, then this one action would lead us to expect to find the data which I have been discussing with no very great improbability. If the traditional account is improbable overall, that is because of its prior improbability, involving a massive violation of laws of nature, and just how improbable that makes it depends on the worth of natural theology;  

But the "worth of natural theology" in his argument comes in the form of reading God's mind, and is thus arbitrary.  Further, he never considers evidence which we *don't* have but should be observable and recorded if the actual events transpired as claimed.  For example, the Romans should have had trials for grave robbing -- whether Jesus was resurrected or no -- but these are not mentioned by other historians of the time at all, even while other Roman trials of the early Christians are discussed in great detail.   Any mention of the temple veil ripping, the dead saints walking around Jerusalem, and the purported earthquake are also never mentioned.  Any probabilistic treatment needs to handle these cases. The part of Bayes' Rule which describes how well the claim explains the evidence can be broken up into separate parts of the evidence,
$$
P(\text{evidence}|\text{claim})=P(e_1\,{\bf and}\,e_2|\text{claim})=P(e_1|e_2,\text{claim})P(e_2|\text{claim})
$$
The evidence, for example, could be $e_1$: reported sightings of Jesus, $e_2$: reported Roman trials.  If we consider, for simplicity, two claims $C_1$: Jesus actually rose from the dead and $C_2$: Jesus was seen by his disciples as visions, then it is clear that we'd have the following,

- $C_1$: $e_1$ is likely and $e_2$ is also likely
- $C_2$: $e_1$ is likely but $e_2$is *unlikely*

If we observe $e_1$ but not $e_2$ then that makes $P({\bf not}\,e_2|C_1)$ quite small, and thus the final answer is diminished and our confidence in the resurrection is reduced.

It is therefore important to not only come up with many alternatives, but to recognize that both positive and *negative* evidence must be used.   

## McGrew on the Resurrection

In "The Argument from Miracles" [@mcgrew2009argument], Tim and Lydia McGrew offer a probabilistic argument for the *cumulative* case for the resurrection. 

### Summary of the argument

The primary assumptions of the approach are stated up-front,

> Our argument will proceed on the assumption that we have a substantially accurate text of the four gospels, Acts, and several of the undisputed Pauline epistles (most significantly Galatians and I Corinthians); that the gospels were written, if not by the authors whose names they now bear, at least by disciples of Jesus or people who knew those disciples -- people who knew at first hand the details of his life and teaching or people who spoke with those eyewitnesses -- and that the narratives, at least where not explicitly asserting the occurrence of a miracle, deserve as much credence as similarly attested documents would be accorded if they reported strictly secular matters.  Where the texts do assert something miraculous -- for example, Jesus' post-resurrection appearances -- we take it, given the basic assumption of authenticity, that the narrative represents what someone relatively close to the situation claimed. For the purposes of our argument, we make no assumption of inspiration, much less inerrancy, for these documents, and we accept that there are small textual variations and minor signs of editing, though we do not in any place rely on any passage where the textual evidence leaves serious doubt about the original meaning. 

The core of the argument comes down to,

> As a first step, let us consider a single disciple. The best of the available naturalistic explanations, the hallucination theory, requires (if it is to match $R$ in likelihood) an extraordinary level of detailed delusion, seamlessly integrated (so far as he can tell) with his experience of those around him. Such delusions do occur in waking life in those who suffer from severe mental illness, but such illness is mercifully rare and is accompanied by other noticeable conditions that were absent in the case of the disciples. The other naturalistic hypotheses have higher prior probabilities, perhaps as high as $0.001$, but they do not come close to matching the explanatory power of $R$; their contribution to the likelihood $P(D_i|\sim\!\!R)$ is negligible even by comparison to the hallucination theory.
>
> [...]
>
> But having assigned a single factor, we must ask what happens when we take into account the fact that there were thirteen such disciples. We can get a first approximation to the result by assuming independence. [...] So under the assumption of independence, the Bayes factors for each of the thirteen $D_i$ must be multiplied, which yields a staggering combined factor
>
> 
> $$
> \begin{aligned}
> P(D|R)/P(D|\sim\!\!R) =& P(D_1|R)/P(D_1|\sim\!\!R)\times \\
> &P(D_2|R)/P(D_2|\sim\!\!R)\times \cdots \times \\
> &P(D_{13}|R)/P(D_{13}|\sim\!\!R) \\
> =&\underbrace{\frac{1}{0.001} \times \frac{1}{0.001} \times \cdots \times \frac{1}{0.001}}_{13\text{ times}} \\
> =&10^{39}
> \end{aligned}
> $$

by including two other pieces of evidence (e.g. the testimony of the women which they call $W$ and the conversion of Paul which they call $P$), they arrive at

>But our estimated Bayes factors for these pieces of evidence were, respectively, $10^2$, $10^{39}$, and $10^3$. Sheer multiplication through gives a Bayes factor of $10^{44}$, a weight of evidence that would be sufficient to overcome a prior probability (or rather improbability) of $10^{-40}$ for $R$ and leave us with a posterior probability in excess of $0.9999$.

McGrew anticipates the challenge of the independence assumption and provides a discussion and justification.

> the invocation of independence assumptions at several points is contestable; in fact, we believe that in the case of the calculation for D the independence assumption almost certainly breaks down. Surprisingly, however, this fact does not necessarily lessen the strength of the argument. Everything depends on the balance of considerations regarding the direction and extent of the breakdown of independence under $R$ and under $\sim\!\!R$. 

They describe the problem with the independence assumption

> If three men accused of committing a crime all give, in essentially the same words, the same innocent explanation of their actions, the plausibility of the claim that they are conspiring to give themselves an alibi undermines the force of their combined testimony. Even when there is no definite intent to deceive, witnesses may influence one another's testimony causally in a way that would obtain even if the event had not happened, or had not happened in the way that they are saying it did. 

First, with the three pieces of evidence under consideration

> First, let us consider the independence of the strands of argument which we have labeled
> $W$, $D$, and $P$.  [...] The testimony of the women to the empty tomb and to the appearances of Christ are independent, obviously, of Paul's conversion [...]  The women's testimony is essentially independent of that of the thirteen male witnesses. [etc...]
>
> But the assumption of independence *among* the thirteen male witnesses raises greater difficulties. [emphasis original]  

Then the argument moves to the idea of collusion in  early  Christianity,

>  When people are claiming to be eyewitnesses to some event (in this case, the appearance of the risen Jesus), and when they are in danger of an unpleasant fate for making the claim in question, their believing and having better evidence for this claim is a better explanation of positive dependence among their accounts -- their being able to encourage one another to continue making their testimony -- than their not believing the claim or having worse evidence for it. [...] If any one of the witnesses in question had not actually had clear and realistic sensory experiences just as if Jesus were physically present, talking with them, eating before them, offering to let them inspect his hands and side and the like, it is not credible that he would listen to the urging of his fellows to remain steadfast in testifying to such experiences. 

So, in sum, the McGrews argue that either the testimony of the disciples is  independent or when it is not independent, the independence is broken in such a way that *favors* the resurrection claim.  This is due to the idea that the existence of thirteen claims to the resurrection -- under penalty of death -- is much less likely than would be expected if the event didn't happen than if it did.  

### Problems with the argument

The problems with this argument stem from a *lack of imagination* of alternatives (as we've seen before) and a *lack of skepticism* about the independence of the sources (which somewhat follows from the lack of imagination).

#### Lack of imagination

My first objection comes from the assumptions about the text -- this already gives too much ground.   I don't have a problem with "substantially accurate text" because I don't think the primary issues come from translation or copying problems.  Quotes like "people who knew at first hand the details of his life and teaching or people who spoke with those eyewitnesses" and "basic assumption of authenticity, that the narrative represents what someone relatively close to the situation claimed" are not well-supported historically.  I think this can be handled in the present analysis by rolling these assumptions into the primary claim, $R$, and adding the contrary claims into the alternative, $\sim\!\!R$.  By restricting the analysis to only those that, effectively, assume eye-witness testimony already favors the primary claim unduly.  

For an example, it helps to recall that what we actually have for evidence are *claims* written decades later which all show theological embellishment and literary structures.   If you see the Gospel of Mark as a story about how the "last shall be first," a response to the Roman destruction of the Jewish temple, then many of the claims collapse as possible literary constructions.  The testimony of the women is easily understood in this context and can be further understood as a way of Mark dealing with the possible fact that the entire story is a late creation -- those "unreliable women" didn't get the message out until now.  In fact Mark, our earliest Gospel, doesn't even mention any of the testimony from the disciples about the resurrection and the letters of Paul never even mention disciples...at all.[^disciple]

[^disciple]:Paul mentions apostles but never mentions anyone actually knowing Jesus personally, listening to his ministry, or being with him during the crucifixion.

A similar line of argument can be held for the writings of Paul.  I'll admit that the conversion of Paul itself would be a rare event, but not unheard of.  I'll accept the McGrew estimate of 1 out of a 1000 for it, but how many early religious sects were there in the Roman empire at that time?  If you play the lottery enough, as we've seen, you will invariably have rare events happening frequently.  Also, whichever sects were successful would have to have had a successful group of founders with a compelling (and flexible) story.  Even Paul's conversion fits the "last shall be first" theme which would be a compelling narrative for the early Christians regardless of the truth value of any of the claims.  The point here is not to suggest any particular way that Christianity began, but to point out that there are numerous, unremarkable pathways which are still consistent with a rare conversion.

#### Lack of scepticism

The McGrews provide a quote which they should follow themselves, 

> "William Kruskal sums up his detailed discussion of independence in the combination of testimony with a succinct cautionary moral: 'Do not multiply lightly' (Kruskal, 1988, p. 929). "  

When your calculation *critically* depends on the independence assumption and there is a chance -- even a small one -- that the sources were not independent, especially in the direction against your claim, then you need to establish that this chance is less likely than the claim you're using independence to support.  Otherwise you are biasing the calculation towards your claim.

Other than collusion, what other mechanisms are there?  Recall that all the evidence we have is from *literary* constructions decades after the events.  You could have *literary* "collusion."  Say, only 5 disciples independently made the original claims, but for *literary* reasons you like the number 12 or 13, you might have expanded those claims to include all the disciples.  Because of the gap between the original events and the writings it would be challenging to rule out such processes, yet the calculations presented depend *critically* on those processes not happening.  

### How should the argument be done?

If you're really trying to structure the 

## Minimal facts argument

One of the more recent arguments for resurrection  comes in the form of the so-called "Minimal Facts Approach" [@habermas2004case], introduced by Gary Habermas and Michael Licona and popularized by William Lane Craig. In this approach a core handful of claims are supposedly supported even by secular scholars, and that this core inevitably leads directly to supporting the resurrection. Different people have somewhat different lists of these minimal facts[^minimal], but Craig summarizes them[^craigminimal] neatly as

[^craigminimal]: https://www.reasonablefaith.org/media/debates/is-there-historical-evidence-for-the-resurrection-of-jesus-the-craig-ehrman

> - Jesus's honorable burial
> - his empty tomb
> - his post-mortem appearances
> - the origin of the disciples' belief in his resurrection.
>
> [https://crossexamined.org/the-minimal-facts-of-the-resurrection/](https://crossexamined.org/the-minimal-facts-of-the-resurrection/)

[^minimal]: The fact that there is disagreement even among apologists about what counts as a "minimal fact" should give one pause and be perceived as a problem for the argument as a whole.

Matthew Ferguson in his essay "[Knocking Out the Pillars of the "Minimal Facts" Apologetic](https://adversusapologetica.wordpress.com/2013/06/29/knocking-out-the-pillars-of-the-minimal-facts-apologetic/)" [@Ferguson2013] has a very detailed historical dismantling of these primary claims and is very good reading. 

An immediate rejoinder to the minimal facts approach is the fact that Paul, the earliest Christian writer, doesn't mention most of them - the honorable burial or the empty tomb. Paul also uses the same word for Jesus "appearing" to Peter and James as to "appearing" to himself, which calls into question whether these were actual visitations or just visions, clearly not requiring an empty tomb or any other details of the crucifixion. Further, Paul never talks about any post-resurrection *stories*, only *visions*. This, too, doesn't lend any support to the minimal facts argument because a big part of the post-resurrection appearances the stories. If the stories aren't true then the appearances are called into question too.

Another thing to consider is that if this line of logic were applied to, say, the Roswell Incident it would be quite easy to argue for alien visitation. Given the rarity of alien visitations, as well as supernatural resurrection, I will need more than a few claims about tombs and visions to convince me that something extraordinary occurred.



