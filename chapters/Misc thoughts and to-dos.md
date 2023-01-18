* figure out citations and footnotes
* check the steelman link to see if pandas handles it like typora


#todo 
- [ ] grammarly
- [x] equation numbers?
- [ ] update url links to bibliographic links
- [ ] go through the miracles and resurrection episode and put in anything useful
- [ ] summarize James and Kamil's arguments in [[Chapter 05 - The Case for Jesus#McGrew on the Resurrection]] -- in how should the argument be done
- [ ] put in the problems in some specific miracle claims
- [x] replace '' with "
- [ ] cumulative cases and the magnitude 
- [ ] fix bibliography for epub

## Lessons


- apply your reasoning about rare or miraculous things to other rare and improbable things - Mormonism, UFO abduction, etc...  does it work there?  if someone used the argument you've used, but for one of these things, would you be convinced?  why or why not?
- consider alternative explanations for everything
- reconsider your prized beliefs from time to time.  were your original reasons valid?  are they still valid?
- don't take claims at their face value -- follow up to the originals
- don't insist that someone accept your definition for a term or label, especially if it is a label the other person is using for themselves.  a theist telling an atheist what atheism means is as bad as an atheist telling a theist what God means.  
- don't get hung up on labels -- ditch them when they are not useful and get in the way of conversation.
- be aware of cognitive fallacies and the steps to avoid them
- the person that you can fool the easiest is yourself

## From Stephen Thrasher

**Probability is not just about the math - On simplicity**


#todo
- [x] scale up the model complexity penalty example -- perhaps continuous case?
>I did not realize that it was possible to calculate a penalty for model complexity, and I found this section very helpful to put that in concrete terms. It's hard for me to relate the small penalty in the card example to models with more degrees of freedom. Is there a way to scale this, like you’ve done for the Monty Hall problem?


#todo   
- [x] look at changing the expected value in this example
>I’m having a little bit of a hard time with one part of the card deck example. It seems to me that for purposes of comparison the decks should be equivalent except for level of complexity, but the expected value of the zero to three 3-spades in E5 is (0+1+2+3)/4 = 1.5 spades, which is fewer than the 2 spades in E4. It’s unclear whether E5 is less likely than E4 after the first draw because of its complexity or because it has fewer 3-spades on average.

  
#todo   
- [x] check out Jaynes ch 20 to see if it can help with this section
>I've now looked at Jaynes ch 20 on model comparison and re-read your section, and it looks like the answers are there. Jaynes compares the peak likelihood against the likelihood integrated over parameters and calls that the Ockham factor. Your model E5 has a higher peak likelihood than E4 because it can have up to three 3-spades in the deck, and re-reading your section, I see that you’re saying that you shouldn’t look only at the peak likelihood, as tempting as that might be, rather you have to look at the composite problem.

  
>I do wonder, though, if there is more to the calculation. Jaynes eq 20.10 suggests that when the data concentrates the parameter space, you have to scale by the fraction of prior probability in the newly limited parameter space. Does this mean that when you have a first draw of 3-spades, the zero-spades instance of E5 is ruled out, and the probability should be scaled by 3/4? I’m guessing yes because the model still includes the invalid region of parameter space.


#todo 
- [x] go through this calculation
>To sketch this out: if E5 were instead {0,2,2,4} of 3-spades, then its expected value would match that of E4, and the only difference left would be complexity, I think. After drawing the first 3-spades, the probability numerator for E5 needs the scaling factor to reduce the prior to the still-plausible region of parameter space.


> P(3-spade | E5)*P(E5) = [(2/4)*(1/4)+(2/4)*(1/4)+(4/4)*(1/4)] * (1/2) * **(3/4)** = 3/16

> If the model is {1,2,2,3} of 3-spades, then it doesn't have that penalty and after the first draw of 3-spades has the same probability as the simple E4 model. I'm not sure how to make sense of this.

  

**Probability is not just about the math - Lessons from probability**

#todo 
- [x] make sure all of Jaynes' desiderata are mentioned in the book
>The list at the beginning of this section gave me a big confidence boost. One possible addition: in your Graceful Atheist interview, you mentioned Jaynes saying that you can't make conclusions on only a subset of the data (i.e., it has to be non-ideological). I'm not sure that's in your book yet, and I think it would fit well in this list.

  

**Miracles - Arguments against miracles**

#todo 
- [x] read essay
- [x] check blog again for other Hume posts
>After reading [John Earman's article critiquing Hume](https://nam12.safelinks.protection.outlook.com/?url=https%3A%2F%2Fsites.pitt.edu%2F~jearman%2FEarman2002a.pdf&data=04%7C01%7C%7Cace836fc94ee4ed1a3d108d9d06084a7%7C6c853569e95e43788926ab9501a771a3%7C0%7C0%7C637769937486238332%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&sdata=5ovLNYB%2F2WCbdVtk88RHhWbTY1RkJBwI4WYYzDINZ3g%3D&reserved=0 "https://nam12.safelinks.protection.outlook.com/?url=https%3A%2F%2Fsites.pitt.edu%2F~jearman%2FEarman2002a.pdf&data=04%7C01%7C%7Cace836fc94ee4ed1a3d108d9d06084a7%7C6c853569e95e43788926ab9501a771a3%7C0%7C0%7C637769937486238332%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&sdata=5ovLNYB%2F2WCbdVtk88RHhWbTY1RkJBwI4WYYzDINZ3g%3D&reserved=0"), yours was the first positive interpretation of Hume I came across. It was helpful to see a simple validation of an old idea that has been ridiculed so much. I later found an [essay by Peter Millican](https://nam12.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdavidhume.org%2Fscholarship%2Fpapers%2Fmillican%2F2013_Earman_Miracles.pdf&data=04%7C01%7C%7Cace836fc94ee4ed1a3d108d9d06084a7%7C6c853569e95e43788926ab9501a771a3%7C0%7C0%7C637769937486238332%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&sdata=dGqxN8Qmnrxcf0oBX4JoDX%2Fpy7%2BZ5RMTFLsqq2SY4bk%3D&reserved=0 "https://nam12.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdavidhume.org%2Fscholarship%2Fpapers%2Fmillican%2F2013_Earman_Miracles.pdf&data=04%7C01%7C%7Cace836fc94ee4ed1a3d108d9d06084a7%7C6c853569e95e43788926ab9501a771a3%7C0%7C0%7C637769937486238332%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&sdata=dGqxN8Qmnrxcf0oBX4JoDX%2Fpy7%2BZ5RMTFLsqq2SY4bk%3D&reserved=0") that you might enjoy if you haven't seen it already.

  

**Lack of imagination**  

#todo 
- [x] update alternatives to include Kamil's alternatives and Fodor's alternatives
>I was pretty floored when I finally understood that one major consequence of Bayes theorem was that you have to find the highest-quality alternative explanations possible. As a deconverting Christian, I personally care less about whether theism in general is true and more about whether Christianity in particular is true. In the The Case for Jesus > McGrew on the Resurrection > Lack of Imagination section, I think it would be helpful to contrast McGrew’s weak alternative hypothesis (a not-very-good hallucination theory) with a much more substantial alternative. I like this [succinct summary from Kamil Gregor](https://nam12.safelinks.protection.outlook.com/?url=https%3A%2F%2Fyoutu.be%2FDRNIXn1xD_0%3Ft%3D340&data=04%7C01%7C%7Cace836fc94ee4ed1a3d108d9d06084a7%7C6c853569e95e43788926ab9501a771a3%7C0%7C0%7C637769937486238332%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&sdata=BV6zIVTtp2h2MRQumud01sL51cMGkitG50WTkGZV%2Fd0%3D&reserved=0 "https://nam12.safelinks.protection.outlook.com/?url=https%3A%2F%2Fyoutu.be%2FDRNIXn1xD_0%3Ft%3D340&data=04%7C01%7C%7Cace836fc94ee4ed1a3d108d9d06084a7%7C6c853569e95e43788926ab9501a771a3%7C0%7C0%7C637769937486238332%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&sdata=BV6zIVTtp2h2MRQumud01sL51cMGkitG50WTkGZV%2Fd0%3D&reserved=0") (YouTube, the summary is ~2 minutes long) which as far as I can tell reflects the dominant scholarly hypothesis. I found a similar summary in a well-known book by Christian theologian N. T. Wright if you're interested.

  
#todo 
- [x] add a response to this -- essentially, the only reason they see not-serious is because there are not many adherents currently.  but this is *exactly* how atheists view the Christian God Yahweh, just like Zeus and Apophis.
>Regarding the alternative examples in The Case for God > Swinburne > Imagination, I totally understand how an evil-god and the Greek pantheon might seem like rivals to theism to many people, but to me, maybe because it’s all still so fresh, they don't seem like very serious alternatives. I do wonder if other people would, like me, see these as weak examples and feel like they penalize the overall argument, consciously or not.

  

**The case for Jesus - Minimal facts argument**

#todo 
- [x] need to update the link/info for Ferguson's essay
- [x] include the material and cite it.
>Unfortunately, it looks like Matthew Ferguson’s essay “Knocking Out the Pillars of the “Minimal Facts” Apologetic” is no longer available. He took down his blog, and although I did find mention that he has plans to put some content up again, he has yet to do so. If you want to try to contact him, you can look up celsushistoricus on Facebook and Reddit.


>I myself can’t believe that the minimal facts argument has survived this long. Even apart from the historical issues, it’s just not a valid argument. You do unshared statistical analysis on unshared survey data to establish whether a cherry-picked set of claims can be called “historical fact” without defining the term, then you round up to P=1 and switch to a deductive argument, where you then ignore the issue of priors and all other evidence and explanations.

  

**Stand-alone argument**

#todo 
- [ ] summary of the argument and the problems still

>When I reached the end of the book, it felt like I had a lot of really powerful ideas, but they were mostly embedded within commentary on apologetic arguments. I suppose I was expecting an overall stand-alone argument against theism or the Christian faith. As I went along, I had constructed an argument along these lines:  
  
>* There is no way around a very low prior for Christianity, even if you assume theism in general.  
>* The prior for a religion arising from natural human causes is quite reasonable.  
>* Take one strong alternative explanation, some form of the dominant scholarly hypothesis.  
>* Express burden of proof as an inequality from the odds-ratio form of Bayes.  
>* For Christianity to be plausible, the overall evidence update has to favor Christianity over the alternative explanation more than the ratio of priors favors the alternative explanation.  
>* The overall evidence update doesn't do anything close to that, so Christianity is unlikely to be true.  
  
>The main reason I'm interested in seeing a stand-alone argument like this is that I'm a little disturbed by how solid it looks to me, and to not see such an argument makes me question my understanding. McGrew and Swinburne’s treatments of Bayes are problematic; am I overstating my case as well? Stating the argument as a postive, consolidated, independent argument will give it more overall weight and clarity, even if it's largely repetition.

  
>
**My background on this topic  
**

>I’m in my early 40s, married with three kids, an aerospace engineer, resigning my church membership in the next couple of months after being in it all my life. My Christian community in Cambridge, MA, is fairly intellectual, including a professor of epistemology and a pastor with an MIT economics PhD who are both very conversant with Bayes Theorem. I took a probability class in my masters program at MIT and use it occasionally for work. Before reading A Measure of Faith, I had already discovered some of the qualitative implications of Bayes and learned that my level of belief, which had seemed marginal, was actually much lower than I thought it was. My brother was interviewed on the Graceful Atheist, and he pointed me to your book. I’m mostly interested in checking the validity of the overall argument and understanding how strong a case it makes.



#todo 
- [ ] make tables less fragile
- [ ] put websites in  the bibtex so they show up in references


