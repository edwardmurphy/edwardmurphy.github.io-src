Title: Microsoft SQL Server with R Server
Date: 2017-01-01
Tags: sql; R

## Introduction and Motivation

I suppose it's a New Year's resolution of sorts (gasp!), but bear with me. There are so many applications and 
languages and tools and such that I want to learn that I can easily let myself bounce from project to project. This is 
an intellectual curiosity that I've had my entire life, and I'm proud to have it. However, it has sometimes left me 
feeling incomplete with my knowledge - the feeling that I didn't spend enough time on a single task. Perhaps because 
my curiosity doesn't come with goals. It's satisfied just being curious, while the analytical part of my mind jumps up 
and down with frustration at a trail of incompleteness. So I thought it would be worthwhile to give the analytical 
part some credit and set more intentional goals for the curiosity. Thus, I've set out to perform self-learning 
projects on a monthly basis. This just so happens to coincide with the new year, hence it being a resolution of sorts. 

The choice for this month was a touch arbitrary. When this revelation of intention came to me, I decided to go with 
the project on my plate at that very moment. It happened to be SQL Server. Now, I've been working on this for a few 
days already, and I'm happy to see there are immediate data science benefits. Microsoft SQL Server 2016 includes 
capability for running R (I'll clean up this language in the more technical part of this blog, i.e. defining this 
capability), and Microsoft has posted some machine learning examples on GitHub for use with their R Server, so scoRe! 
We'll be using Visual Studio as the R IDE, so this month's project is mostly Windows based. SQL 
Server is now available in some Linux distributions, and I've already leaped ahead a bit and installed it in a virtual 
machine running CentOS. We'll get to this later though.

I'll be walking through *Beginning SQL Server R Services* by Bradley Beard as my main text. This has served me well to 
date with installation of SQL Server 2016 and the component R tools. The purpose of this post will be to document my 
progress (so I can keep the analytical part of my brain appeased) and maintain notes of sort that I may refer to in 
later months when I've moved on to other projects.  

## Terms

In this section I'll keep a running list of terms to define, mostly the different components of my SQL Server 
installation. 

1. SQL Server: For our purposes, this refers to the relational database server from Microsoft. The installation documented in this post is the 2016 Developer Version of Microsoft SQL Server. The Developer Version is a free version of the enterprise-level server without the license for production use. Since I've no production or profit motivations at this point, I'm quite secure in meeting that requirement. Just to be complete, let's also define:

a. SQL (Structured Query Language): Check out the [wiki](https://en.wikipedia.org/wiki/SQL). Quick, quick version it's a language used in conjunction with relational databases, i.e. those structured according to the [relational model](https://en.wikipedia.org/wiki/Relational_model).

b. Server: Check out the wiki page for [database server](https://en.wikipedia.org/wiki/Database_server).

2. R Server: Microsoft's enterprise level R platform. This is based on the CRAN R distribution, but adds high level capabilities for processing of big data in multiple environments. It's provided as **R Services** in SQL Server 2016 Developer edition. 

3. R Open: Looks and feels like normal R (including the RGui), but Microsoft has added additional packages for this distribution.

4. R Tools for Visual Studio (RTVS): Turns Visual Studio into an IDE for R. Uses R Open to interpret code developed in Visual Studio.

5. SQL Server Management Studio (SSMS): The GUI for managing servers.
