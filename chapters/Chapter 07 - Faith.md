# Faith

The word *faith* has many definitions, some which seem conflicting.  However, as it is commonly used, the definitions point to a single quantity.  It is easiest to see this in the exploration of faith from specific examples.

## Introduction to faith and probability

### Statements about faith

It may be helpful to start with the dictionary definition, and then follow with a number of statements about *faith* to see where the common usages fall.

- faith (noun) [@MerriamWebster2009].  1. strong belief or trust in someone or something. 2. belief in the existence of God. 3. strong religious feelings or beliefs. 4. a system of religious beliefs.

- "Now faith is confidence in what we hope for and assurance about what we do not see."[^hebrews11]

  [^hebrews11]: Hebrews 11:1, New International Version.  <https://www.biblegateway.com/passage/?search=hebrews+11&version=NIV>

- Faith is trusting in, holding to, and acting on what one has good reason to believe is true in the face of difficulties. The difficulties may be where you have to take an action where the outcome is beyond your control. (Tim McGrew) [@Brierley:2014aa]

- Belief without evidence.  Pretending to know things you do not know. (Peter Boghossian) [@Brierley:2014aa]

- Faith is the excuse people give when they believe something and don't have a good reason. When you believe something and have a good reason, then you give the reason. And in every other instance, you offer something that is faith. - Matt Dillahunty

From these few definitions, we can already see a few things.  First, people use the term in different ways, at different times, so it will be critical in any discussion that we agree on what we are talking about.  In particular, we don't want to run the risk of changing definitions mid-discussion and we don't inadvertently straw-man anyones argument.  Second, the two primary components that seem to make up all definitions of faith are *belief* and *trust*.  Faith seems to not be a synonym of either, but a particular combination of them with some restrictions - not all beliefs or acts of trust require faith.

### Belief, trust, and faith

We have already seen that *belief* is represented mathematically by *probability*, so where *faith* requires belief we will employ probabilities.  *Trust* [@MerriamWebster2009] is ''belief that someone or something is reliable, good, honest, effective, etc.'' So it would seem that trust is a subset of belief, like knowledge is a subset of belief, but pertaining specifically to the reliability or goodness of the thing believed. 

Faith, however, seems to go a bit further than trust and involve *action* or the willingness to act.  When asked by Peter Boghossian, *''why don't we say that we have faith in the existence of chickens?''*, Tim McGrew replies, 

> We are venturing nothing on the existence of chickens. When I believe that chickens exist and I act on that belief I am not taking any step that places outcomes I care about beyond my direct control. [In the case of religion], people are placing the outcome of their eternal soul out of their control. They are taking a risk where the outcomes matter. The decision itself is evidenced but the outcome is uncertain.



## Rollercoasters: faith in everyday life

Words have meaning, and if we are going to communicate with each other we need to make sure to use words as carefully as we can.  Otherwise, misunderstandings abound.  It seems very common that a word like "faith" is used by different people for different ends, and the definition shifts even within an argument.  Take for example, the video by Rich Spear [@Spear:2013aa].  In it, Spear presents a distinction drawn between "faith" and "belief," using an analogy of a roller-coaster --belief in the ride being safe vs trusting it being safe enough to ride on.  Notice that his focus is on trust, and thus on *action*.  

It is clear that one must *at least* believe the ride is safe as a prerequisite for trusting it. Since when we say we believe *strongly* in a proposition $A$ when $P(A)>0.95$ (or some other, somewhat arbitrary, high number), we can map this prerequisite to something like the following
$$
\begin{aligned}
P(\text{safe}) &= 0.99 \\
P(\text{unsafe}) &= 0.01
\end{aligned}
$$
Once you believe it is safe, do you trust it to ride?  This brings in decision theory, where we mix probabilities with utility measures. You could believe it to be safe at the $P(\text{safe}) = 0.99$ level, but still not trust it ''with your life'' because of the *cost* associated with being wrong.  A utility table might look like

|            | safe | unsafe |
| ---------- | :--: | :----: |
| ride       |  10  | -1000  |
| don't ride |  0   |   0    |

Calculating the average utility for each action we get

$$
\begin{aligned}
\langle U_{\text{ride}}\rangle &= 0.99 \times 10 + 0.01\times (-1000) = -0.1 \\
\langle U_{\text{don't ride}}\rangle &= 0.99 \times 0 + 0.01\times 0 = 0 
\end{aligned}
$$

so it is better not to ride.

As a result, *trust* requires both belief and a sufficiently positive net utility. Placed in these terms it is much more clear how the argument is set up.

- when Spear says that "faith" is like "trust," he is  already approaching the problem with strong belief, and is assessing  utility - and he rightly claims that belief is not enough.
- when the atheists say that "faith" is "belief without evidence,"  they are addressing the strength of the evidence to obtain strong  belief in the first place - and claiming that the evidence is not sufficient.
-   when  Spear and others say that "faith is rational" they are either talking about utility (and not belief) or they are claiming that the evidence is in fact good enough for strong belief, and then  consequently high utility.

In all cases, it seems as if for the religious, utility and belief are muddled when using the word "faith."  For the atheist, "faith" is always first and foremost about belief, because even the usage involving trust has belief as a prerequisite.  Perhaps if we frame the problem in terms of belief (probability) and utility we can clear up the fog surrounding discussions of the term *faith*.

## Faith and trust

We see the same structure occurring in an *Unbelievable* podcast [@Brierley:2014aa] between theist Tim McGrew and  Peter Boghossian.  Because they were not thinking in terms of the framework presented here, they talked past each other through most of the episode.  In this discussion, Boghossian insists that faith is "*belief without evidence*" or "*pretending to know things you do not know*," and Tim McGrew insists that faith is more like trust.  The discussion then devolved into a back and forth with both sides claiming that "all the people I know use my definition," and was generally unproductive.  As I've said before, at this point it becomes better to dispense with the terminology and go back to basic concepts where one could agree.  It is clear that in the expected utility equation,

$$
\begin{aligned}
\langle U_{\text{action $A$}} \rangle =& P(\text{outcome 1})&\times& U(\text{outcome 1}|\text{action $A$}) + \\
&P(\text{outcome 2})&\times& U(\text{outcome 2}|\text{action $A$}) + \\
& &\vdots&
\end{aligned}
$$

Boghossian is focusing on the probabilities ($P\text{outcome 1}$, $P\text{outcome 2}$, etc...) and McGrew is focussing on the utilities ($U(\text{outcome 1}|\text{action $A$})$, $U(\text{outcome 2}|\text{action $A$})$, etc...)  



## The discussion



McGrew says that very few Christians (less than 1\%) would use Boghossian's definition of faith, "*pretending to know things you do not know*."  I agree that no Christian would *articulate* this definition of faith, however they may be *functionally* using it, which I will address later.

McGrew opens with 

> Faith is trusting in, holding to, and acting on what one has good reason to believe is true in the face of difficulties. The difficulties may be where you have to take an action where the outcome is beyond your control.



The example he gives is jumping out of an airplane, where one has faith in ones instructor to have packed your parachute properly. Ones act of jumping draws the distinction between faith and *hope* (if you just *hoped* your instructor packed it, you wouldn't jump), and the decision is made in the face of evidence, not despite it or without it.

### Addressing the definitions

Clearly claims using expected utility require that probability assignments have already been made, so claims of utility must necessarily be probability claims as well. When translated into these more precise terms, both McGrew's and Boghossian's claims begin to make more sense. It will also show that McGrew is in fact using the Boghossian's definition, in some cases even while denying it.



> You have faith that your instructor packed your parachute, as opposed to Peter packing it.  Your act of jumping makes faith more than simply hope (if you just hoped your instructor packed it, you wouldn't jump), and the decision is made in the face of evidence, not despite it or without it.

The equations are:
$$
\begin{aligned}
\langle U_{\text{jump}}\rangle =& P(\text{instructor packed})\times U(\text{instructor packed}|\text{jump}) + \\
& P(\text{Peter packed})\times U(\text{Peter packed}|\text{jump}) \\
\langle U_{\text{don't jump}}\rangle =& P(\text{instructor packed}\times U(\text{instructor packed}|\text{don't jump}) + \\
& P(\text{Peter packed})\times U(\text{Peter packed}|\text{don't jump})
\end{aligned}
$$


with a possible utility table

|            | Instructor Packed | Peter Packed |
| ---------- | :---------------: | :----------: |
| jump       |        100        |    -10000    |
| don't jump |         0         |      0       |

For this analysis to work, we would have at least,

- $P(\text{instructor packed}) \sim 1$: one is nearly certain the instructor packed the parachute
- $P(\text{Peter packed} )\sim 0$: one is nearly certain that Peter *didn't* pack the parachute
- $U(\text{instructor packed}|\text{jump})\gg 1$: good benefit from jumping, with instructor packing the  parachute
- $U(\text{Peter packed}|\text{jump})\ll 0$: large cost  from jumping, with Peter packing the  parachute
- $U(\text{Peter packed}|\text{don't jump})=U(\text{instructor packed}|\text{don't jump})\sim 0$: neutral gain for not jumping in either case

### Analyzing the responses

Notice, for McGrew to have "faith in his instructor," two things must be true:

1. $P(\text{instructor packed}) \sim 1$: one is nearly certain the instructor packed the parachute
2. $U(\text{instructor packed}|\text{jump})\gg 1$: good benefit from jumping, with instructor packing the  parachute

McGrew wants to focus on point (2), while Boghossian wants to focus on point (1). Once seen this way, it is very easy to understand the responses to other questions.

For example, 

- Boghossian: *Why don't we say that we have faith in the existence of chickens?*
- McGrew:  *We are venturing nothing on the existence of chickens. When I believe that chickens exist and I act on that belief I am not taking any step that places outcomes I care about beyond my direct control. [In the case of religion], people are placing the outcome of their eternal soul out of their control. They are taking a risk where the outcomes matter. The decision itself is evidenced but the outcome is uncertain.*

This is because,
$$
\begin{aligned}
U(\text{chickens exist}|\text{action}) \sim U(\text{chickens don't exist}|\text{action})\sim 0
\end{aligned}
$$
for all actions - we have nothing at stake, there is no utility, even if  we are confident that chickens exist (i.e. $P(\text{chickens exist})\sim 1$).

Another example,

- Boghossian: *Do you have faith or evidence that Islam is false?*
- McGrew: *Why would I use the word 'faith' when I am venturing nothing on Islam? I am a little bit confused about the framing of the question that way. I think I have evidence that it is false, but since I am not venturing on Islam, I'm not sure why the word faith would come in.*

Does McGrew have have faith or evidence that Islam is false?  McGrew claims he has evidence that Islam is false, $P(\text{Islam}|\text{data})\ll 1$, but is not venturing anything on Islam (or more accurately, on his choice to not follow Islam), $U(\text{not-Islam}|\text{action})\sim 0$. Again, Boghossian sees the first part (the probabilities), yet ignores the second part (the utilities).

### Equivocation

Going back to the exchange, we note, however, that sometimes McGrew is also using Boghossian's definition:

- Boghossian: *what do people mean when they accuse someone of having 'faith in evolution'*
- McGrew: *You're trusting in something that you cannot completely verify because it doesn't lie open to your senses.*

Now I can think of no way to understand this statement from the perspective of McGrew's definition:

> When I act on that belief I am taking some step that places outcomes I care about beyond my direct control.

What outcomes are you placing beyond your control believing in evolution? What obvious utility are you weighing in this case? As far as we can see there is none, and so *faith* in this context is in fact being used here as *belief without sufficient evidence*. 

It is called an *equivocation fallacy* to use a word in one way but switch definitions sometime later without pointing that out or noticing it.  One of the benefits of mapping statements to mathematical language it to see this explicitly. 

### Priors and faith

The word *faith* seems to only be used in contexts with low *prior* probability. In the conversation between McGrew and Boghossian they spoke of faith in the context of the supernatural, extreme activities (i.e. jumping out of planes), events beyond our immediate senses -- all of which coincide with lower *prior* probability, and need *more* evidence than is typical to overcome them. These examples may, or may not, also have high utility. We don't have faith in the existence of chickens because the existence of chickens has high *prior* probability.

It makes sense then that there will be people who are not convinced by the evidence for things that others have *faith* in.  They are not convinced the evidence is of sufficient quantity or quality to raise a low *prior* probability up to a significant *posterior* probability.  For those who are convinced by the evidence, it also makes sense that they would then focus on the *utility* of those claims.  The problem that arises, however, that the word *faith* refers to two distinct components -- the belief and the utility -- and the apologist can easily switch between them without even noticing it themselves. Again, we put forward the suggestion to discuss things in terms of decision theory, explicitly outlining the equations in order to avoid words with multiple meanings.  

## Does science have faith?

In his talk, "Life: Creation or Evolution" [@Miller:2009aa], Ken Miller makes the point that science should inform faith and faith should inform science. He cites Paul Davies, a physicist who has an interest in theism, and whose article "*Taking Science on Faith*" [@davies2007taking] takes the position that science itself is a faith-based activity. Ken Miller points out, and one can confirm in Paul Davies' article, that there are two tenets in science that are supposedly taken on faith:

1. the universe is ultimately knowable and understandable
2. knowledge is better than ignorance

These concepts, however, are fundamentally different than faith, or even axioms.  Even here, it is plain that the claims are referring to the *belief* part of faith, and not the *trust* part of faith.  The entire phrase "*taken on faith*" is a signal to the listener that this is so.

The first idea, that the universe is knowable, needs to be a bit more specific: what does it mean to be *knowable*? Prior to 1900, it was believed that the pieces of a physical model, such as the force of gravity, or the electric and magnetic fields of Maxwell were "real": there was one-to-one correspondence between the model components and things in the real world. Thus, it was believed, that knowing the model you would know nature. After 1900, with the advent of quantum mechanics, physical models were evaluated based on their predictive value: those models that predicted well were good models. It was not believed that there was necessarily a correspondence between the model components and the real components in nature. Aspects of the model, such as the wave function in quantum mechanics, were not believed to be real but simply useful in making predictions. To know the world is to be able to predict what would happen.

Let's say we replace "*understandable*" with "*predictable*," a replacement which we think makes practical sense (how else would you determine that you understand something?), and is directly in line with modern physical thinking. Doing this, then tenet (1) ceases to be an axiom, or something we take without sufficient evidence ("*on faith*"), but is observable. If the universe is unpredictable, then all attempts at making prediction will fail. This is not what we observe at all. Surely there are still things that are unpredictable, such as the simultaneous value of the position and momentum of the electron, or the positions of every molecule of air in this room, but even there we can make specific predictions about average quantities or the values of other variables of interest. Practically, the universe has demonstrated itself to be understandable, on the whole. This is not a matter of faith.

The second tenet (2) I would wager is too vague. What does "*better*" mean? Better for whom, or for what? Psychologically, one might argue something akin to "ignorance is bliss," and there might be something to that. If we define, however, "*better*" to be higher standard of living (longer, healthier, more free life) then knowledge can be argued to have a demonstrable benefit over ignorance. The results of science has doubled the life expectancy in the past 100 years, and has allowed us to live more free and healthy lives.  As Carl Sagan says, science delivers the goods. Is there any convincing argument that ignorance is better, or that we really can't decide which is better? 

There is a danger in using the word *faith* in these contexts.  It can communicate to the unaware that there are things that one should justifiably believe on insufficient evidence -- a direct violation of the laws of probability.  It can also imply, for those who take *faith* to mean *trust*, that the scientists using the term are somehow admitting an agency in the universe that they don't intend.  It serves only to propagate sloppy thinking in both the fields of science and religion.

## Another interaction - McGrath and Dawkins



As part of the "Root of All Evil" program, Richard Dawkins conducted many interviews with theists.  One in particular, with theologian Alister McGrath, deals with the notion of faith [@Dawkins:aa].  They start with a discussion about the term *faith*, and McGrath says

> We're dealing with a different situation than, for example, evidence that the moon orbits the earth at a certain distance

and

>  There are many possible ways of explaining [the world], and we have to make the very difficult judgement of which is the best of these [explanations] [...] evidence takes us thus far, but then when it comes to deciding between a number of competing explanations, it is extremely difficult to make an evidence-driven argument.

and

> I believe faith is rational, in the sense that it tries to make the best possible sense of things [...] even though we believe this is the best possible sense of things, we cannot \emph{prove} this is the case [...] there is a point where faith goes *beyond* the evidence

By this point, the reader should be able to tell that McGrath is employing the *belief* part of the expected utility form of *faith*.  One wonders in these cases why he doesn't simply talk about evidence, and the weight of probabilities? Historians, for example, don't use the word *faith* even though they deal with probabilities, some of which are highly uncertain.  Scientists deal with probabilities all the time without invoking the word *faith* in any paper.

Further, McGrath ignores the fact that there already is a proper and rational method to address the "decision between a number of competing explanations," that *doesn't* go beyond the evidence, and doesn't claim more knowledge than is justified. What is this method? It's called the mathematics of probability! So, McGrath is claiming there is a problem that faith solves, which is not a problem at all, and he is using the word faith (at the moment) as synonymous with probability.

Why is he doing this? It seems as if it is because McGrath is holding to a double standard, and shifts the definitions of concepts around whenever pressed. He doesn't like the notion of believing strongly without sufficient evidence (which, as we've seen, is one use of the word faith), so he defines it (at the moment) to be equivalent to probabilities.

### Inference to the best explanation

Then McGrath continues to talk about probabilistic reasoning, and says that with faith one is doing *inference to the best explanation*, given a number of competing multiple explanations. As we stated earlier, if all he means is that faith is probabilistic reasoning, then we don't have an argument -- except that we think he can make things more clear. We would contend, along with Dawkins, the *vast* majority of people do not take it to mean this -- even the notion of *faith* as *trust* isn't the same as this.

However, we'd like to challenge his basic premise: that in dealing with multiple competing explanations that one should try to *infer to the best explanation*, and *believe strongly in that explanation*. A simple example introduced in Section on Belief and Evidence suffices to see this. In this example, we have two explanations of the number of stars, one which says that there is an *even* number of stars and another that says that there is an *odd* number of stars. Pretty much we know that, at any given instant, one of these *must* be true. However strong belief in either one is completely unwarranted - there is simply no way to know. From a probabilistic framework, we express this as

$$
\begin{aligned}
P(\text{odd})&=0.5 \\
P(\text{even})&=0.5 
\end{aligned}
$$
However, it is worse than that. Let's say we had a smidgen of evidence toward the even-star model, such that we had:
$$
\begin{aligned}
P(\text{odd})&=0.499995 \\
P(\text{even})&=0.500005 
\end{aligned}
$$


Even though there is a *best* explanation here (*even* is slightly more probable than *odd*), and we have the exact probabilities, it is *still irrational* to hold strong belief in either explanation. One really does have to look where the weight of the probabilities lay. Inference to the best explanation fails as a guiding principle in the face of uncertainty, and is not well defined in all contexts. 

What is happening here is that on the face of it, "inference to the best explanation" sounds like a great thing -- something we should always strive for.  However, when you look at what it *actually*  means, it falls short unless you are in a situation where the best explanation is also very probable.  Strong belief is only justified when the claim is very probable, not just that is is the most probable amongst a number of (possibly nearly equivalent) alternatives.

### Shifting sands

One of the benefits of seeing these arguments in the light of the framework of probability is that it makes one sensitive to shifting definitions.  We saw that earlier where Tim McGrew seems to change his usage of the term *faith* depending on the response.  Here, McGrath does the same thing.

First it was "*faith is reasonable*," based on evidence, going beyond the evidence to the "*inference to the best explanation*" and that as a result one can have a "*reasonable faith in God*."  Then, when asked about his belief in a creator, and the evidence for it,  despite having difficulty with the implied complexity of such a creator, he says

> I want to go back to CS Lewis who says I believe in Christianity as I believe the Sun has risen, not simply because I see *it* but *by it* I see everything else. Belief in God gives you a way of seeing the world that makes an awful lot of sense of it.

When pressed on what this implies, he says that 

> there are many reasons I believe in God and that [origins] is not even the primary one...religion really isn't much about where things came  from, about things in the distant past, but really about how things  are now. How to live your life, how to be moral, etc...

which then becomes 

>  the key reason for believing God is Jesus, that there is something [in the Jesus story] that needs explanation.

and then, this becomes that it is not really about the life of Jesus, and his historicity, but how he was perceived by his followers - the significance they saw in the life and teaching of Jesus.

Notice how this keeps shifting? At first, it is about belief, and then it is about significance (which one could argue is a kind of utility).  Every time he gets pushed on the specific consequences of his statement, he retreats, redefines, and redirects the conversation.

McGrath doesn't seem to realize that any explanation, even of things currently, entails assumptions that can be tested - perhaps with observations about the past. He can't simply say that religion is "not about where things came from," when they explicitly make statements of origins -- statements which have been universally discredited. The atonement, for example, *does* depend critically on the existence of Jesus, the existence the ''Fall'', and a creator of the universe -- for none of which did McGrath provide evidence. If Jesus didn't exist as a real person (or even if he was just an ordinary guy) then it doesn't matter that his followers simply *believed* that Jesus was God incarnate when determining ones belief in the doctrine of salvation. The demonstration of the historicity of the events claimed is *necessary* for the doctrinal belief. If you don't have strong evidence of the former, then you are not rational to believe strongly in the latter - you'd be claiming to know things you could not know.

As a scientist, one takes an idea, and pushes the idea to it furthest consequences to see where it breaks, or to see what it depends on. McGrath seems to change the topic whenever this is done - he does not seem to want to face the very real, specific consequences of his stated beliefs and refuses to see the connections between the things that may be confirmable (apparent design in the biology and the universe itself, historicity of people and events, alleged miracle claims, etc...) and the things that make him feel good, but are unmeasurable (existence of heaven, the atonement of sins, etc...).

## Pascal's wager



Blaise Pascal, a French philosopher, put forward an argument referred to now as "*Pascal's Wager*" [@Wikipedia:2015ac] for the religious life .  The argument is based on decision theory, and is one of the first uses of this theory on any topic.  In the "Wager," Pascal states that people choose to believe or not believe in God, and the possible environments they find themselves in are the God either exists or doesn't.  He then sets up the utility table,

|                      | **God Exists**| **God Does Not Exist** |
|----------------------|--------------------------|-------------------|
| Believe in God       | $+\infty$ (infinite gain)| $-1$ (finite loss)|
| Don't Believe in God | $-\infty$ (infinite loss)| $1+$ (finite gain)|

It is clear then that the best course of action, given this utility table, is to believe.  There are many problems with this argument, some which impact the mathematics and others that are theological.  An example of the former is the analysis assumes only one possible God - what if you choose the wrong God?  Extending the table to include this would make the "best choice" not as clear cut.  An example of the latter is the idea that one cannot simple *choose* to believe, and the act of pretending to believe would go against the dictates of God.  

Pascal's Wager is, however, a useful starting point for a discussion and highlights some of the issues one faces when applying decision theory too simplistically. 

## A more formal exploration

In the philosophical literature, there are more formal explorations of the concept of faith.  These explorations can also be helped by casting the ideas into the probabilistic framework.  For example, Daniel Howard-Snyder considers what he calls "Propositional Faith" [@howard2013propositional].  He immediately recognizes, as we do here, that the word *faith* has many usages which he clears away as being not on topic, and focuses on the use of faith in a sentence like "*A wife might have faith that her marriage will survive a crisis*" or  "*Frances has faith that her young sons will live long and fulfilling lives.*"  Each of these cases has the sentence structure of "$A$ has *faith that* $B$."  In his covering of other uses, Howard-Snyder removes the following usages,

- Faith as a noun (e.g. "earnestly content for *the faith*")
- Faith as a process (e.g. the process of coming to believe the Gospel as a result of the Holy Spirit)
- Taking something *on faith* (i.e. taking on authority or testimony)
- Faith as assent to a proposition with certainty
- Faith as a kind of knowledge

It is interesting to see what Howard-Snyder considers propositional faith, and some of the considerations around it.  We believe he is still using the term inconsistently, in two ways - one which matches the structure we've been exploring in this book, and the other as a direct synonym for *hope*.  Consider the following case from his paper.

> Propositional faith does not require 'certainty', without any hesitation or hanging back.  A wife might have faith that her marriage will survive a crisis, while harboring doubts about it.  Indeed, propositional faith is precisely that attitude in virtue of which she might possess the inner stability and impetus that enables her to contribute to the realization of that state of affairs, despite her lack of certainty.

This case matches decision theory quite nicely. The equations are:
$$
\begin{aligned}
\langle U_{\text{action}}\rangle &= \\
& P(\text{good marriage}|\text{action})\times U(\text{good marriage}|\text{action}) + \\
& P(\text{failed marriage}|\text{action})\times U(\text{failed marriage}|\text{action}) \\
\langle U_{\mbox{inaction}}\rangle &= \\
& P(\text{good marriage}|\text{inaction})\times U(\text{good marriage}|\text{inaction}) + \\
& P(\text{failed marriage}|\text{inaction})\times U(\text{failed marriage}|\text{inaction})
\end{aligned}
$$


where the probabilities of the outcomes, as well as the utilities, clearly change with the possible actions.  For example, we expect action to have a positive effect on the probability of a successful marriage, $P(\text{good marriage}|\text{action})>P(\text{good marriage}|\text{inaction})$.

A possible utility table, which reflects the idea that, if the marriage is successful without action then there was time and resources saved, but if the marriage failed without action there is a penalty in the form of guilt over lost opportunity.  Obviously there are many complications that this table overlooks, and should be seen as a basic approximation.

|          | good marriage | failed marriage |
| -------- | :-----------: | :-------------: |
| action   |      90       |      -100       |
| inaction |      100      |      -110       |



The high positive utility that the wife puts on her successful marriage, and high negative utility to its failure, directs her to make actions in her marriage's favor despite having lower probability of its success.  This is the notion of *faith* worked out.

Another case is

> But one can have faith that something is thus-and-so without entrusting one's welfare to it in any way, as when I have faith that Emily will survive breast cancer but I do not entrust my well-being to her or her survival

where, as far as we can see, the use of *faith* here is completely indistinguishable from *hope*.  There is no utility explicit in the statement, and the probability is presumed to be low.  



