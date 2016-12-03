Title: Tests/Conditions for Linux Distro Likeability
Date: 2016-12-02
Tags: linux

At some point I may get around to an article describing how/why I run multiple Linux distros across my various 
gadgets/hardware, but if I waited to write this article then frankly I'd stall. So, it'll have to suffice that 
multiple posts of mine will simply refer to this as yet unwritten article. 

For now, I'd like to jot some notes concerning how I've evaluated distros in the past, as much as I can recall them 
from memory, and also to delineate planned benchmarks. All of the items I'm now posting have been scattered in my 
brain over a fairly long stretch of time, so it is mighty fulfilling to capture them more concisely and spatially. 
Perhaps the following conditions/features can be scripted one day for quick reporting in tabular form...maybe even 
wrrapped into some more tinkering with databases for data capture - a skill that I'd enjoy learning. Ahhh, reference 
to another article. 

Here are some stock feature of Linux distros that I've previously jotted down as worthy of consideration for 
evaluation. Most of these features are customizable, so most are not show-stoppers. However, since I've found that the 
main difference among distros is the suite of stock packages included with the Linux kernel, these features rather 
define a distro from the beginning, so in the end they can make or break a distro for me. After all, if I simply 
wanted to pick ALL my own packages, I'd just start with Arch. Who has time...

- Terminal
- File Explorer (especially network discovery, including Samba shares)
- Document Viewer
- Test Editor
- Image Editor
- BitTorrent Client
- E-mail
- Video Player
- Package Manager

The choice of display manager is inexorably tied to the features above for most distros, and I've found that I usually 
prefer bits and pieces from different display managers (e.g. Gnome, Cinnamon, etc.). For instance, my favorite 
terminal is yakuake. However, installation of yakuake comes at a price - installation of dozens and dozens of KDE 
packages I simply do not use. Thie could belie inexperience on my part (i.e. knowing how to not install recommended 
but unrequired packages), but what I wind up with is bloatware to the max. As I test and/or evaluate these features 
more formally across distros, I'll take some more time to see if installation of new packages is loaded with 
unncessary software. 

Here are some additional considerations which I'll most leave here for future description and amendment.

- Expertise level assumed (i.e. does the distro assume I need to be protected from myself?)
- R: ease of installation of packages (i.e. are paths available to R or, as in above, as I assumed to need protection 
from myself?)
- Chroot-ability: any issue chrooting into other filesystems?
- GUI system configuration (related to package management). I don't want to be protected from myself, but I also don't 
really know how to configure the system in /etc for most settings, so leave me alone but come here...that's a totally 
reasonable attitude, right?
- Overall speed. Plasma 5 just simply DOES NOT WORK (except in CentOS, I've found). openSUSE seems to be faster than 
Linux Mint. Stuff like this.
- Does Samba configuration work out of the gate? Usually not. I spent WAYYYYYY more time on Samba than I really needed 
to, getting sucked down that rabbit hole on far too many occasions. Yet I can't let it go. 

I'll follow-up with an article about development setups I'd like to evaluate/try/learn (e.g. Anaconda, Docker), and 
with those considerations plus these I can map out a factorial evaluation for multiple distros. 

 

 
