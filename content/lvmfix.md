Title: Fixing My Logical Volumes
Date: 2016-11-04
Category: Articles
Tags: logical volumes, linux

I use logical volumes on my Acer notebook. My current understanding of logical volumes is that they are most often utilized when disk space is combined across multiple physical volumes, i.e. disks. I have a single SSD in my notebook, so why use logical volumes? Because I like to tinker with linux distributions. I'm frequently installing new distros, resizing the space for each distro, adding shared space, uninstalling distros...tinkering. All of this is possible with a normal disk partitioning setup, but I found it to be cumbersome. After awhile unallocated partitions were squeezed between distros. Or I couldn't resize a partition easily since the next partition was not free. Sure, I could copy partitions to another disk, resize locally, then copy the saved partition. Or...I could use a tool that allows resizing on the fly. And is not "typical." Hence, my choice of logical volumes. 

Now, logical volumes even on a single disk are not a cakewalk. For one, I've had some difficulty installing new distros directly to a new logical volume. I'm writing this while running openSUSE Leap 42.1, which I had to install to a clean partition before copying to a logical volume. Logical volumes also aren't as visible - it is possible to delete the data on a logical volume without realizing it's there (see ED ADD REFERENCE). And, if you're like me and you don't really know what you're doing and you tinker, you can wind up with a scenario like I currently have: logical volumes spread across multiple (logical) partitions within a single extended partition.

I probably couldn't even accurately detail how I got to my current partition setup. Just so.much.tinkering. So, it's messy. Very messy. And I want to clean it up. I want a single partition that will include all my logical volumes. Then I can tinker away cleanly.

First, here's a snapshot of my current partitioning:


![Current Partition]({attach}images/currentpartition.png)

Some things of note:
1. The first partition is unused and may be completely unnecessary. I use grub as my bootloader, and the files for this are located in the extended partition. I really have no idea right now if this first partition is necessary., Pretty sure Windows uses it, but I don't have Windows installed. I'm thinking this can be removed with no problem.
2. The swap partition is taking up a primary partition, and this is not necessary. I can move this to a logical partition and save a primary partition if I need it.
3. The linux volume group is spread across multiple partitions. This is not causing any problems (in fact is one of the nice features of logical volumes) but it just looks...not right. 
4. The final partition (/dev/sda9) used to be unallocated space - this was recommended in the following article (ED ADD REFERENCE) for solid state drives. However, I needed this space to install openSUSE Leap, and did copy to the linux volume group...but look at that I'm actually still booting into this partition! Did not know that. So I have 2 copies of Leap. Sort of unnecessary, yeah? Would like to leave this space unallocated again.
5. My linux volume group currently includes 2 distros: openSUSE Leap 42.1 (already mentioned) and Linux Mint Sarah. 

With all this in mind, in order to fix this mess, here's an outline of what I'll need to do. Note that I'm using a 120 GB Kingston SSD for all of this.
1. Make images of my current distros (for openSUSE Leap, this would be the one on /dev/sda9)
2. Wipe my entire SSD 
3. Maybe recreate the first partition again? I don't know enough about it yet to know which way to go, and it's not really taking up much space. Let's say yes to this. So, 250 MB.
4. Create a primary partition (10 GB) at the front of the drive that would allow for new distros to be installed when necessary. By leaving a partition at the front, I could also install Windows if I had to without having to move partitions again, since Windows needs to be the first OS on the disk.
5. Create a big extended partition (~98 GB) that will include:
   * swap space, and
   * a single partition (at least initially) as a volume group for all the logical volumes I want
6. Leave the final 10% of the drive (12 GB) unallocated
7. Copy images of distros to the new logical volumes (maybe...for another article).

This should be fun. I'll document the execution step-by-step as we go along.
  
## Imaging Current Distros
There are a multitude of tools for creating images of disk partitions, but whenever possible I like to use the **dd** command. It's powerful, and dangerous, but it's right there - no need to install other software, figure out a new GUI, boot from a rescue USB with Clonezilla. Since I have two distros (plus another logical volume for shared files), I can image each distro while booted into the other. So, while booted into openSUSE Leap 42.1, I can image the Linux Mint distro very easily:
```
\# dd if=/dev/mapper/linux-mint of=/path/to/image.img bs=4M
```

I used an external drive to save the image. The block size is...well I don't really know why I use 4M. A remnant of a quick Google search. Perhaps (likely) can be optimized. But there it is. Wait, and when complete you have an image of the distro. Simple. Just to check, we can mount the image using a loop device:
```
\# losetup /dev/loop0 /path/to/image.img
\# mount /dev/loop0 -o loop *mountpoint*
\$ cd *mountpoint* && ls -Al
```

Quick look to see that the expected directories are there to give a little boost of confidence that all went well. Remember, the SSD will be wiped clean, so be confident as can be! Then repeat for all other logical volumes as needed. Remember to unmount and delete the loop devices:
```
\# umount /dev/loop0
\# losetup -d /dev/loop0
```







 




