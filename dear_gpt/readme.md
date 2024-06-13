# DEAR GPT: Dynamically Enhanced AI for Robust General Programming Tasks

*Problem:* It can be helpful to use ChatGPT-4 to help with complex programming problems but it has several limitations that make it less than helpful at times. These limitations are forgetting essential context quickly, not understanding the codebase, and too limited of usage of GPT-4 on ChatGPT's only $20/month plan.

*Proposed Solution:* Create an interface for the API to make a better experience. It should take a system prompt containing all of the essential codebase, context, and custom instructions necessary. Ideally, this can be used in an unlimited capacity for more complex programming problems, for a lower cost per month.

## Too long, do read

Like many developers, I have used ChatGPT to help me code. These days, I tend to reach for GPT-4 for more complex problems, and Copilot in VS Code for more general everyday stuff (things I used to Google, like how an asynchronous for loop works in javascript, Copilot usually just knows). My experience is that GPT-3.5 and Copilot are about equally smart (but Copilot wins for it's direct integration into VS Code) and GPT-4 is better for long-form, complex issue like, "Here's 300 lines of code that is supposed to do X, but in fact does not do X, find out why this code does not do X, is Python, as a programming language somehow down?" Except I actually write it like, "[PASTE CODE] this isn't doing the thing, plz fix." and it works just as well.

That said, I never really _feel great_ using GPT-4 to generate code. It's kind of like drugs and acts of violence. Cool and fun? Yes. But is it really something to build a life around, something to make your whole identity, and indeed to ultimately become so hopelessly dependent on that you can no longer function without it? Yes. The problem is just sometimes the output isn't exactly what you want, and or Open AI tells you you did too much and kicks you back down to GPT-3.5. So let's fix that.

In truth, I wanted a small project that I could build repeatedly in different languages/frameworks in a day or two as a way to get acquainted with that language. And I figured I've reached the stage of my career where I could do this publicly, sharing it so people who are not me could potentially replicate it in their own ways.

I am leaving the proposed solution quite open-ended because I don't want to make repeating the project too tedious between languages. I want the idea to have a lot of scope creep each time it's done, like bolting on more features that the core problem statement doesn't require. I think that's useful for an intro project for learning new languages. Allowing you to let your creativity open up, come up with new concepts, and figure out how to do them.

Let me flesh out the negative user experience of GPT-4 in more detail. The first thing is that it "forgets shit I just told it" all the time. I use the word just colloquially, it doesn't forget things in the prompt I gave it, or in most cases the previous prompt, but it forgets a lot of things from 5-10 prompts ago or more, moving towards no memory of it quite quickly. My experience has been that it's short-term memory and my own are not in sync, with it's being much shorter. The result of this is that I have to keep more things in my own memory, and keep inputting them into prompts to make sure they are in the memory of the AI. It occurs to me at this part of the paragraph that I should probably use a word other than memory, let's say recall instead. 

For example, the other day I was dealing with a very large json file that had some improperly formatted json in it. The file was too large for me to be able to open in any file editor, a fact I learned after trying to open it with every file editor, and a fact I had conveyed a few times to GPT-4, while I was trying to concept a strategy with GPT-4 to write some code to access the file programmatically and identify the error. Still, every 5 or so messages it would fall back to a recommendation of "Try opening the file in a file editor and scanning through it to see if you can spot the errors." 

At a certain point, I found myself typing in all caps to a piece of software because I was not feeling heard.

For additional context, a work project I had been nearly finished with needed the data contained within this file to work, and being unable to get the data threatened to delay the whole project. So it was a stressful time. 

And for me this is exactly where GPT-4 breaks down: *hard things at stressful times*. I don't think it is the case that the AI is being pushed to it's limits, but rather that I am being pushed to mine. The quality of my own prompts goes down, I just hand it things and hope AI will solve it. When it doesn't solve it we get into this garbage in, garbage out doom loop, where I "just said something" 15 messages ago, and it doesn't recall that anymore, and I am getting worried that I won't be able to solve a problem, and then I see the notification that I've hit my limit of usage of GPT-4 and can try again at 9:24PM. 

And maybe it is just looking out for me, maybe I should take a break, and come back in a few hours, and look at it with a fresher set of eyes. Or maybe, that should be my decision to make? 

Born out of that frustration I increasingly felt like the necessarily mass-market ChatGPT tool was too under-powered for serious programming, and I had no use for it in unserious programming. 

The other case where I use GPT-4 a lot is in conceptual, non-code work. "We are considering doing this big new project that will take a few weeks. It's modeled on this. It needs to do this, using this, and so on. What would be the best approach to achieving this? Within that, what about A vs B, when considered in the context of Contstraint C." And on and on. 

The responses I get to these more conceptual, high-level things are quite stunning. It brings up a lot of things that I would not have considered. It is great at dispassionately advocating both sides of a case. And it's penchant for verbosity, when directed towards a clear problem, can actually result in a nice experience of having a robust and useful consideration as a result. 

But this too, breaks. If we take the same conversation with humans, where this generally happens. A product strategy meeting could end up being a 2-3 hour talk where we are fleshing out an idea, contemplating resources, free associating to other related ideas, looking at small details and big pictures, and trying on sequences of small decisions, seeing if something whole emerges. 

That can't be done in a single call and response loop. But, ChatGPT is designed to try anyways. And while it can sometimes produce impressive results (it can get a concept from 0 to 5% fleshed out fast) it falls apart on the small footnote that is the remanining 95% of the process. Crucially, it falls apart because it is essentially trying to stuff it all into a single response. I think it does this because it can't really remember things well yet. 

If we put AI into a team conversation at a table, when it started talking and we heard it for the first time, if we had asked it a detailed and specific question, it's answer might have impressed. 30 minutes into the conversation we would have found ourselves at a point of frustration having said, "No, no, no. Like we told you before. This has to do X." Because, in a natural conversation flow, it won't remember anything from more than 5 minutes (5-10 back and forth loops). 
