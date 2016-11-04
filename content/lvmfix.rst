Fixing My Logical Volumes
#########################

:date: 2016-11-03
:category: Articles
:tags: logical volumes, acer notebook, linux

I use logical volumes on my Acer notebook. My current understanding of logical volumes is that they are most often utilized when disk space is combined across multiple physical volumes, i.e. disks. I have a single SSD in my notebook, so why use logical volumes? Because I like to tinker with linux distributions. I'm frequently installing new distros, resizing the space for each distro, adding shared space, uninstalling distros...tinkering. All of this is possible with a normal disk partitioning setup, but I found it to be cumbersome. After awhile unallocated partitions were squeezed between distros. Or I couldn't resize a partition easily since the next partition was not free. Sure, I could copy partitions to another disk, resize locally, then copy the saved partition. Or...I could use a tool that allows resizing on the fly. And is not "typical." Hence, my choice of logical volumes. 

Now, logical volumes even on a single disk are not a cakewalk. For one, I've had some difficulty installing new distros directly to a new logical volume. I'm writing this while running openSUSE Leap 42.1, which I had to install to a clean partition before copying to a logical volume. Logical volumes also aren't as visible - it is possible to delete the data on a logical volume without realizing it's there (see ED ADD REFERENCE). And, if you're like me and you don't really know what you're doing and you tinker, you can wind up with a scenario like I currently have: logical volumes spread across multiple (logical) partitions within a single extended partition.

I probably couldn't even accurately detail how I got to my current partition setup. Just so.much.tinkering. So, it's messy. Very messy. And I want to clean it up. I want a single partition that will include all my logical volumes. Then I can tinker away cleanly.

First, here's a snapshot of my current partitioning:
![Current Partitions]({filename}/images/currentpartition.png)

