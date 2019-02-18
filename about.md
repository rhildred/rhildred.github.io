---
layout: about
title: About
permalink: /about/
img750x500: "https://res.cloudinary.com/salesucation-com-inc/image/upload/v1523471546/rich750x500_xgz0dq.png"
---

These pages highlight some of my student's work. I am a software developer passing on my trade. It was also my father's trade. And my brother's. As well as developer I have also held the role of product manager and sales engineer. I believe that interface is king. I also believe strongly in pattern language, systematic problem solving and test driven development. Actually anything by [Kent Beck](https://en.wikipedia.org/wiki/Kent_Beck) is pretty good in my opinion. Facebook is really strong from a [development operations](https://code.facebook.com/posts/270314900139291/rapid-release-at-massive-scale/) perspective if not an ethical perspective.

## <a href="https://rhlab.io" target="_blank">rhlab.io</a>

I have to apply for my job at Wilfrid Laurier every term. I need a portfolio of student's work to apply. I also need students to be satisfied with my current courses. It looks really bad, unprofessional and dis-satisfying to students when their software labs don't work. Often they don't. In the past I have solved this problem by using portable apps and putting the required software on a usb key. Then I would use heroku and openshift 2 to let the students showcase their code. This approach failed for me last term with my python class. There were a couple students in my class of 30 that it just didn't work for. I didn't figure out why as I had already started a product idea with my remaining consulting customer. No time.

  

This term I had a wordpress class in a mac lab. The first class I discovered that the lab wasn't set up. I had a short lecture and went over the instructional plan. That week I hacked like mad to get something going for a new lab and made Francescou's [docker-compose-ui](https://github.com/rhildred/docker-compose-ui) be multi-user based on a github oauth2. I came back to school and had a giant fail because I didn't put the github name in the container name. Student a and b both called their instances "wordpress-starter." When b brought their's up a would get a gateway error, bring their's back up. B would get a gateway error ..... Week 3 I fixed this and made it impossible to type invalid characters in a host name and the setup was very reliable. Last week I had 30 students in my 4gb amazon linux ec2 instance virtual lab all doing their midterm in peace.

  

Now I have the beginnings of a permanent solution. It is reading week. When I come back from reading week the students are going to need to do wordpress plugins. I already integrated [Eclipse Theia](https://github.com/theia-ide/theia) so that the students could edit the css in child themes. Now I want to make the workflow be Theia and git based with no docker-compose-ui. Currently I want the security to stay as github oauth2 but I want the students to get 1 docker container with Theia and the development tools in it. Students will also get a 2nd port that they can publish their project on. For the docker-compose-ui project I hacked an nginx proxy up that maps a subdomain to a port. Students will access their ide through `github login name`.rhlab.io and their web-app through apps-`github login name`.rhlab.io. I also have a cloudflare proxy thrown in for good measure and so that I can create cnames programatically. The cloudflare proxy is set to not cache if there is a `-` in the subdomain.

  

I have a portfolio of my own to maintain so it is still an absolute requirement for students to be able to showcase their work on my system. I was thinking about this myself this morning (first day of reading week). I want students to create showcase items that look good in my portfolio as well as theirs. My portfolio template requires some front matter:

  

```

  

title: "Northern Threads"

tags: html5 CP202 github ghpages

img750x500: "https://res.cloudinary.com/salesucation-com-inc/image/upload/v1522973943/NorthernThreads750x500_zt8i5q.png"

img700x300: "https://res.cloudinary.com/salesucation-com-inc/image/upload/v1522973943/NorthernThreads700x300_qkouj2.png"

img500x300: "https://res.cloudinary.com/salesucation-com-inc/image/upload/v1522973943/NorthernThreads500x300_yvqat3.png"

excerpt: "Businesswear for the Canadian Entrepreneur."

audience: CP202 Wilfrid Laurier elective.

language: html5, github pages

link_to_site: "https://hexx0960.github.io/NorthernThreads/"

repository: "https://github.com/rhildred/CP202Assignment5"

  

```

  

for instance. I will make an application process a bit like google play store that includes the front matter that I need in my portfolio. They will need to:

  

1. commit a special portfolio md page to their repo as well as a docker-compose.yml

1. run a script that creates a new repo on my server and sends me a text to approve

1. push the code to the repo `git push rhlab master`

1. work with me to approve the repo and add the docker-compose magic in to the .git of the repository and to my portfolio if it fills a gap.

  

I am pretty sure that I will win this week. Winning this week will look like a theia php lab that has one docker container per student and is protected by github oauth2. It will also include me marking that midterm and all of the other marking that I put off while struggling to get the Wordpress class going without php being installed. Next week I will have the wordpress students again and a chance to further test the lab. It is reading week at 2 of my institutions this week. Next week is reading week at my 3rd institution. Hopefully I will have a bit more hacking time.

  

Winning next week will look like:

  

1. kinks ironed out of the wordpress lab

1. having a showcase form and backend

1. having a way of updating the showcase automatically from a push by the student.

  

Let's say that I solve my personal lab frustrations over the next 2 weeks. Winning at development should improve my brand by letting me spend more time on other student satisfiers like prompter marking. I should get another course from it ... increasing my billable hours. Is there a way that I can solve pains for other people with this? I could sell this to other contract academics but that would take away from my differentiation. Besides it's all on github at this point so other contract academics can just contribute by using it. I could add lms integration as a premium offering and sell it to the schools I work at. I could maybe sell it by the student seat. I could develop online courses and sell them to the schools that I work at. The colleges have Ontario Learn and I have in the past unsuccessfully approached them about developing online courses where I saw a student need.

  

There are also some student needs that I could meet directly. Perhaps I can re-segment the online instructor-led course market. I read Patt Flynn's ["Will it Fly"](https://www.smartpassiveincome.com/will-it-fly/) and asked some former students that were looking for help to pay me for it. They both disappeared when I asked them for money. I need the lab for my own frustrations so I will finish it at least to the point that will work for the next 2 weeks but right now the rest is a big question mark.
