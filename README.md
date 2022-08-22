# Hackathon: Algorand GreenHouse Hack#1
Algorand GreenHouse Hackathon Submission | Soul Bound NFTs ARC

# Video 📽

[Watch our submission video](https://www.youtube.com/watch?v=5ujm5RIS9K0)

[0:20](https://youtu.be/5ujm5RIS9K0?t=20) - Introduction
[0:35](https://youtu.be/5ujm5RIS9K0?t=35) - Why we are doing this
[1:35](https://youtu.be/5ujm5RIS9K0?t=95) - Challenges in the cannabis industry
[2:35](https://youtu.be/5ujm5RIS9K0?t=155) - Cannabis compliance and why it's different
[3:47](https://youtu.be/5ujm5RIS9K0?t=227) - How NFTs work
[5:03](https://youtu.be/5ujm5RIS9K0?t=303) - Soulbound Tokens and how they work
[6:49](https://youtu.be/5ujm5RIS9K0?t=409) - Technical overview
[8:32](https://youtu.be/5ujm5RIS9K0?t=512) - Our solution
[9:59](https://youtu.be/5ujm5RIS9K0?t=599) - Demo
[13:07](https://youtu.be/5ujm5RIS9K0?t=787) - Final message

# Article 📜

## Introduction

Parsl is a technology company which serves the global cannabis industry by developing the software used for inventory management, traceability, compliance, etc. helping the businesses to save time and money.

We’ve recognised a gap in the market when it comes to how cannabis businesses interact with financial institutions. The uncertain legal status that surrounds the cannabis industry has led to higher costs for patients, which exist because of the burdensome compliance requirements a cannabis business needs to deal with, but which also affects those who serve them, including banks, payment processors and other financial institutions. 

## Industry Problems

The cannabis industry is marred by issues including tedious and expensive compliance requirements and cash operated businesses unable to access robust banking and payment solutions.

Moreover, the compliance requirements in America vary from federal level to state level to county level. Not to mention, these compliance requirements are constantly changing creating additional challenges for the businesses to stay compliant and be ready to provide the necessary documentation on request.

Parsl provides unique, unparalleled decentralized cannabis compliance solutions for banks, credit unions, and investment management firms. Decentralizing compliance lowers the risk profile for any business and eventually the cannabis industry as a whole. 

This is achieved simply by collecting the data through Parsl’s range of services including inventory management, traceability, compliance management, etc. involving impartial actors generating verifiable results thereby eliminating the risk of human error or bad actors.

## Current Limitations

While the world has developed a system of finance involving smart contracts and NFTs, these approaches are centered around transferable and financialized assets utilizing centralised web structures. However, many core financial activities rely on non-transferable relationships and owing to the lack of social identity have become fundamentally dependent on the centralised web structures and inheting their limitations, mentioned below.

NFT (non-fungible token),is a special type of token that is built using blockchain technology, where each token is individually identifiable, meaning unique amongst other tokens of the same type.

NFTs these days are usually used to tokenise assets, which can be anything physical or digital. Things like a piece of art or music or even a video sequence! These NFTs therefore can be used to represent ownership, and thus often hold an economic value themselves which is primarily determined by the markets. NFTs such as these can be bought or sold just like physical items or stock in a company. In other words, these assets are wholly transferable.

Additionally, NFTs may contain a degree of digitally verifiable scarcity, which can often be a key factor driving the demand and value of these tokens.

Moreover, most NFTs rely on centralised platforms like OpenSea to carry out the initial minting of the token as well as the monitoring of transactions.

These features are great for some things, but they don’t work in the context of what we want them to do, and therefore we need to create something new, which we have created in the form of a Soul Bound Token, or SBT.

The SBT standard we propose differs from traditional NFTs and we will now explain how.

The SBTs that we are defining are forever linked to a particular ‘soul’ which is represented by an Algo account. The SBTs need to be claimed by the ‘soul’ to ensure accuracy in the way they are distributed.

Additionally, the SBTs themselves do not hold any economic value. Instead, the value is derived from these tokens through the value they provide in conducting a social, compliance, credit or other type of audit on that ‘soul’.

The quantity of our SBTs is not predetermined but rather the tokens are minted only after a set of requirements have been met.

Additionally, the SBTs are publicly verifiable and non-transferrable which is why the tokens are permanently bound to a specific soul. This in turn eliminates any need for centralized platforms to perform and monitor the transactions. They are more trustable, because they are given out from any issuing ‘soul’ to another ‘soul’ and thus we are decentralising the process of spreading trust through a network.

And finally, the SBTs also provide us with an ability to revoke the tokens, if necessary, which is not possible in case of NFTs.

Combining these factors thus allows us to lower the cost of trust in real-world applications utilizing web3 technology and making the system profitable for all stakeholders.

## Parsl's Solution

A large part of the reason that cannabis compliance is so expensive, is that it needs to be done by highly paid, and scarce Bank Secrecy officers. Our solution allows, for the very first time, participation by the general public in cannabis compliance. 

This allows compliance checks to be automated and significantly more precise and facilitates decentralization by enabling anyone holding our token to participate in auditing a transaction (order) made by a cannabis business. It also allows this data to be quickly collated and shared with a financial institution that has a need to check the compliance of the cannabis business during onboarding, and also in an ongoing manner.

We achieve this by building a smart contract that analyzes all the data found within the inventory management and Point of Sale systems that are used by the cannabis businesses and issues a SBT that gives a compliance score to each order they process. 

It’s an entirely new concept that cannabis businesses are able to own their compliance data but we think it’s important, as an entity should be the one who owns their own compliance, and, most importantly, the one who has the opportunity to build a trust or credit score with traditional financial institutions. 


![Solution Diagram](https://github.com/MatiFalcone/algorand-soulbound/blob/main/Diagram.png)

## Technical Overview

The section briefly describes the various technical components used in development of this system.

### Algorand

Algorand has been a great technology to bring into our stack at Parsl. Algorand has superior performance and high transparency as well as having a minimal environmental impact.

The pure Proof-of-Stake consensus Algorand is founded on has many benefits as a choice for the Parsl platform over the more common Proof-of-Work model. 

The Proof-of-Stake consensus uses randomised voting based on the stake held by accounts on the Algorand network. For the Parsl platform, this means we have higher efficiency, security and scalability. 
It ensures us that the complexity of processing will never grow, and new blocks aren’t slowed down by inefficient challenges that need to be solved. 

We can rely on Algorand to give us a dependable 1000 transactions per second, without performance degradation which is something really important to us as a B2B organisation. 


Proof-of-Work Protocols on the flip side provide cryptographic challenges that forever grow in complexity and inevitably have to ever expand into higher processing requirements which aren’t ideal for resource usage, cost and impacts on the environment.

For us, some of the additional benefits that make Algorand suitable for the Parsl blockchain of choice are the very low transaction fees, and the transparency that we are working with an open source technology.

### Next.js

To ensure we could produce a timely submission we started out with a NEXT JS Template provided by Vercel. 

NextJS is a powerful framework for quickly prototyping and producing a functioning demonstration. Technologies like React-backed NextJS are becoming increasingly important to adopt for implementation speed, server-side rendering options, consistency within a team and performance considerations that you wouldn’t normally be able to achieve in a bones-up project. 

### AWS

As with all of our Parsl Solutions we partner with AWS to ensure stability, security and a broad range of useful services. There are many options on AWS for deploying NEXTJS applications, depending on what kind of hosting you are looking for you require you can directly deploy an SSR application on AWS Amplify, host it in an S3 Bucket or even deploy it as an SSR Node App in an EC2 instance. 

At Parsl we also make use of technologies like the AWS SQS for our managed queues and hosting containerised background services in ECS that make requests out to the Algorand network. 

## Implementation

Issuing a SBT is as simple as issuing any Algorand Standard Asset. The only difference is that we need to provide a few extra parameters. These parameters are: 

1) The Algo account of the issuing soul
2) The Algo account of the Soul that will receive the token. 
3) The `Manager Address` defines the soul that can update the token
4) The `Freeze Address` defines the account that is able to freeze this asset
5) The `Clawback Address` defines the account that is able to revoke this token

But the question remains… how can we attach a token to a specific account? We have achieved this with the use of Atomic Transfers, which are native to the Algorand blockchain. 

They are irreducible batch operations, where a group of transactions are submitted as a unit and all transactions in the batch either pass or fail together.

For example, using Atomic Transfers we can ensure that, every time someone claims a SBT, the token is instantaneously frozen in their account, so the claimer has no time to send it elsewhere (as SBTs are non-transferable by definition, the only possible allowed transfer should be between the issuer and the claimer).

# Our Team 🦸‍♂️

**Atharva Desai**
*Pune, India*

Atharva gets stuff done. He’s the team communications hub, organizer, and enabler, translating the technical requirements into actionable items stakeholders can understand and back again. 

He has the ability to analyze vast amounts of information, identifying and connecting the dots to build a full picture, without losing sight of the individual tasks necessary to make that big vision happen.

In his time at Parsl, he’s developed a rare skill set — the ability to overcome the many obstacles faced when creating new technology, with a smile. When you see Atharva light up, it means something magical is about to happen on your screen.

**Matias Falcone**
*Buenos Aires, Argentina*

Matias is Parsl’s resident blockchain expert and is responsible for designing and developing the applications which use blockchain technology, including for this hackathon. He handles testing and troubleshooting, implementing the team’s great ideas, and politely explaining why the not-so-great ones aren’t going to happen.

This project, however, is a great one and Matias is somehow just a bit more excited than the rest of the team about it — probably because it understands the long-term implications and potential better than most. He’s utilizing his deep understanding of blockchains — derived from extensive research and years of experience — to ensure this project is a success. Really, he deserves a lot of the credit here as he’s the boots on the ground doing a lot of the technical gruntwork.

**Dr. Isaac Balbin**
*Melbourne, Australia*

As the visionary of this project, Isaac isn’t just all big dreams and no hard skills. He’s a PhD-educated electrical engineer and successful entrepreneur. He’s also a blockchain/cryptocurrency subject matter expert, who has given interviews on these subjects to help the average person understand their uses and potential. 

If it’s complicated but needs to be made comprehensible to an average Joe, Isaac is your translator. You may end up on a tangent or two but you’ll know more about the initial question’s subject than you thought possible (and probably 2 or 3 other things you didn’t even know you wanted to learn about).

**Kane Wray**
*Melbourne, Australia*

Don’t ask Kane Wray what he thinks Web3 and decentralization will do for the world unless you’ve got at least 6 hours and want to know the answer in great detail. Of course, if you do, at the end of those 6 hours, you’ll understand why Parsl is such a technological powerhouse as Kane is the one running the technical team.

He’s passionate about blockchain and crypto, leaning on his 10+ years of industry experience to nimbly guide the developers, while also mentoring them to reach their full potential. He’s the perfect person to chat with about the creative solutions and art that has been born from the rise of crypto and NFTs.  Just don’t take him up on his offer of a game of Magic the Gathering or Unstable Unicorns as you’ll probably lose.

**Ralf Kaiser**
*Edmonton, Canada*

If you want to talk about banking or finances, you want to talk to Ralf Kaiser.  With over 30 years of experience in the financial industry — ranging from investment to growth strategies to mergers and acquisitions — Ralf is always interested in and working with technology that’s about to change the banking industry.  Right now, it’s crypto and specifically the potential of Algorand. 

Ralf looks at what Parsl is doing and immediately calculates the impact of every new technology and initiative on the banking industry. As the expert in capital raising, investment management, and capital markets, he can do these calculations in his sleep…or over a beer at the pub (trust us, we’ve seen it.) If it involves any sort of currency, Ralf is your guy.

**Amna Shamim**
*New York, United States*

Amna is a storyteller who loves connecting with her audience. She’ll get inside their heads and deliver the information they want in a way they find enjoyable to consume, whether that’s through detailed technical documents or witty little bios. 

Her background is in writing and editing, and she has translated that ability to connect with the reader into a superpower that works across all communication formats, although she is still a little awkward on stage.

Consuming vast amounts of information and distilling it into easily-digestible formats is her passion (which she insists is completely normal).

# Resources 📚

- ARC Standard: https://github.com/MatiFalcone/algorand-soulbound/blob/main/ARCs/arc-5114.md
- Python Implementation: https://github.com/MatiFalcone/algorand-soulbound/tree/main/python
- Demo: https://algosouls.io
- Demo Source Code: https://github.com/MatiFalcone/algorand-soulbound-frontend
- Parsl Website: https://parsl.co