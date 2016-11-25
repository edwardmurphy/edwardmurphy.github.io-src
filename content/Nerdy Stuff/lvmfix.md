Title: Fixing My Logical Volumes
Date: 2016-11-04
Tags: logical volumes, linux

I use [logical volumes](https://wiki.archlinux.org/index.php/LVM) on my Acer notebook. My current understanding of logical volumes is that they are most often utilized when disk space is combined across multiple physical volumes, i.e. disks. I have a single SSD in my notebook, so why use logical volumes? Because I like to tinker with Linux distributions. I'm frequently installing new distros, resizing the space for each distro, adding shared space, uninstalling distros...tinkering. All of this is possible with a normal disk partitioning setup, but I found it to be cumbersome. After awhile unallocated partitions were squeezed between distros. Or I couldn't resize a partition easily since the next partition was not free. Sure, I could copy partitions to another disk, resize locally, then copy the saved partition. Or...I could use a tool that allows resizing on the fly. And is not "typical." Hence, my choice of logical volumes. 

Now, logical volumes even on a single disk are not a cakewalk. For one, I've had some difficulty installing new distros directly to a new logical volume. I'm writing this while running openSUSE Leap 42.1, which I had to install to a clean partition before copying to a logical volume. Logical volumes also aren't as visible - it is possible to delete the data on a logical volume without realizing it's there (*REFERENCE TO BE ADDED*). And, if you're like me and you don't really know what you're doing and you tinker, you can wind up with a scenario like I currently have: logical volumes spread across multiple (logical) partitions within a single extended partition.

I probably couldn't even accurately detail how I got to my current partition setup. Just so...much...tinkering. So, it's messy. Very messy. And I want to clean it up. I want a single partition that will include all my logical volumes. Then I can tinker away cleanly.

First, here's a snapshot of my current partitioning:

![Current Partition]({attach}images/currentpartition.png)

Some things of note:

1. The first partition is unused and may be completely unnecessary. I use grub as my bootloader, and the files for this are located in the extended partition. I really have no idea right now if this first partition is necessary. Perhaps Windows uses it, but I don't have Windows installed. I'm thinking this can be removed with no problem.
2. The swap partition is taking up a primary partition, and this is not necessary. I can move this to a logical partition and save a primary partition if I need it. Or I can simply use a swap file. 
3. The "linux" volume group is spread across multiple partitions. This is not causing any problems (in fact is one of the nice features of logical volumes) but it just looks...not right. 
4. The final partition (/dev/sda9) used to be unallocated space - it is recommended in the for solid state drives that a portion of the drive be left free in order to optimize read/write and prevent partial blocks. However, I needed this space to install openSUSE Leap, and did copy to the linux volume group...but look at that I'm actually still booting into this partition! Did not know that. So I have 2 copies of Leap. Sort of unnecessary, yeah? Would like to leave this space unallocated again. I've read that 25% of the drive should be left free, but I've also read 10% is sufficient. The drive isn't large, so 10% is what I chose.
5. My "linux" volume group currently includes 2 distros: openSUSE Leap 42.1 and Linux Mint 18 (Sarah). 

With all this in mind, in order to fix this mess, here's an outline of what I'll need to do. Note that I'm using a 120 GB Kingston SSD (112 GB available) for all of this.

1. Make images of my current distros (for openSUSE Leap, this would be the one on /dev/sda9)
2. Wipe my entire SSD 
3. Create a primary partition (20 GB) at the front of the drive that would allow for new distros to be installed when necessary. By leaving a partition at the front, I could also install Windows if I had to without having to move partitions again, since Windows needs to be the first OS on the disk
4. Create another primary partition (80 GB) of type lvm that will include all of my Linux distros on separate logical volumes
5. Leave the final 10% of the drive (12 GB) unallocated
6. Copy images of distros to the new logical volumes

This should be fun. I'll document the execution step-by-step as we go along.
  
## Imaging Current Distros
There are a multitude of tools for creating images of disk partitions, but whenever possible I like to use the *dd* command. It's powerful, and dangerous, but it's right there - no need to install other software, figure out a new GUI, boot from a rescue USB with Clonezilla. Since I have two distros (plus another logical volume for shared files), I can image each distro while booted into the other. So, while booted into openSUSE Leap 42.1, I can image the Linux Mint distro very easily:
```
# dd if=/dev/mapper/linux-mint of=/path/to/image.img bs=4M
```

I used an external drive to save the image. The block size is...well I don't really know why I use 4M. A remnant of a quick Google search. Perhaps (likely) can be optimized. But there it is. Wait, and when complete you have an image of the distro. Simple. Just to check, we can mount the image using a loop device:
```
# losetup /dev/loop0 /path/to/image.img
# mount /dev/loop0 -o loop /mnt
$ cd /mnt && ls -Al
```

Quick look to see that the expected directories are there to give a little boost of confidence that all went well. Remember, the SSD will be wiped clean, so be confident as can be! Then repeat for all other logical volumes as needed. Remember to unmount and delete the loop devices:
```
# umount /dev/loop0
# losetup -d /dev/loop0
```

## Wiping SSD
I followed [this page](https://wiki.archlinux.org/index.php/Solid_State_Drives/Memory_cell_clearing) on Arch-Wiki to wipe my SSD. As disussed on the wiki page, my SSD was frozen, but after suspending the system it became unfrozen and I was able to proceed.

## Repartioning SSD with Parted Magic
I have a multiboot USB (courtesy of [yumi](https://www.pendrivelinux.com/yumi-multiboot-usb-creator/)) that includes a live version of Parted Magic. Booting into this I was able to use GParted to create the following partitioning scheme:

1. 20GB unformatted partition
2. 80GB partition formatted for lvm (linux logical volume manager utility)
3. 12GB unallocated space at end of drive

## Reinstallation of Distros
So...this is where things got difficult. The Linux Mint image I created was corrupted somehow, so using **dd** to copy the image to the newly created lvm partition was not possible. I was not yet aware of the **ddrescue** utility, so I put all my effort into copying the openSUSE image first.

### openSUSE on Primary Partition
Copying the openSUSE image directly to the lvm partition did not work because the initramfs image used at boot did not include capability for logical volumes (through dracut). Thus, at boot the logical volume devices in /dev/mapper/ were not available for mounting. Because of this, I first had to copy the image to a primary partition (/dev/sda1). The file system on the first partition needed to be created first. This can be accomplished in Parted Magic.
```
# mkfs.ext4 /dev/sda1
# dd if=/path/to/image.img of=/dev/sda1 bs=4M
```

Now, another issue comes into play. **dd** is a direct copy of the old distro, so the UUIDs are copied into the new partition (which was given a different UUID at creation). I don't even begin to understand it at a deeper level than what I just stated. Needless to say, it causes major issues at boot since the root partition cannot be found due to mismatch of UUID. This assumes mount points are referenced by UUID. I suppose using labels would have prevented this, but frankly I don't know. In any event, what I needed to do was give the partition a new UUID after copying the image then update /etc/fstab with the new UUID for the root partition. 
```
# tune2fs -U random /dev/sda1
# blkid | grep -e '/dev/sda1' >> /etc/fstab
```

Then I opened /etc/fstab and cleaned it up to look like:
```
UUID=uuid	/	ext4	defaults	0	1
```

Next, the initial ram disk (initrd in SUSE) needs to be updated. This requires chrooting into the SUSE file system; however I was not able to do this in Parted Magic. So I booted into a live version of Arch Linux. Arch is suuuuuuper handy for chrooting because it becomes with a utility **arch-chroot** which automatically mounts /proc, /dev, and /sys. After booting into Arch and mounting /dev/sda1 at /mnt, I ran the following commands:
```
# arch-chroot /mnt
# mkinitrd
```

Quick note on **mkinitrd**. This command uses the utility **dracut** to create the initial ram disk. So why not run dracut? Because it didn't always work for me, especially later when copying the distro to a logical volume. It's likely I'm missing a few simply options, so not a big headscratcher. But **mkinitrd** worked, so I stuck with it. 

Finally, grub bootloader needs to be installed on the disk and the configuration updated. I had to add /usr/bin and /usr/sbin to the PATH environment variable before installing grub.
```
# grub2-install /dev/sda
# grub2-mkconfig -o /boot/grub/grub.cfg
```

Reboot and openSUSE boots! Easy as...pause not.

### Linux Mint in Logical Volume
From our fresh install of openSUSE, create a volume group in our lvm physical volume (/dev/sda2) and create some space for Linux Mint:
```
# vgcreate linux /dev/sda2
# lvcreate -L 30G -n mint linux
# mkfs.ext4 /dev/mapper/linux-mint
```

Since the mint image was corrupted, I used **ddrescue** to copy the image to the new logical volume. It turned out that single file was corrupted (total size was 4096K), but **ddrescue** had no problem doing its thing:
```
# ddrescue --force /path/to/image.img /dev/mapper/linux-mint
```

Next, created a new UUID for the mint logical volume as was done above for openSUSE, then mount the logical volume for chrooting. This time, I had to mount /proc, /dev/, and /sys myself. Assuming the mint logical volume is mounted at /mnt, run the following in order to update the initial ram disk (initramfs in Mint):
```
$ cd /mnt
# mount -t proc /proc proc/
# mount --rbind /dev dev/
# mount --rbind /sys sys/
# chroot /mnt
# update-initramfs -u
```

Update /etc/fstab as above, exit chroot, and update the bootloader:
```
# grub2-mkconfig -o /boot/grub/grub.cfg
```

Reboot and Mint is available from the grub menu.

### openSUSE in Logical Volume
In order to free up the first partition and have all distros in logical volumes, the openSUSE installation on /dev/sda2 needs to be copied to a new logical volume. Boot in Mint, and perform the following:
1. Create a new logical volume *suse* with ext4 filesystem
2. Use **dd** to copy from /dev/sda1 to the new logical volume
3. Create new UUID 
4. Chroot into new *suse* logical volume
5. Update initrd
6. Update /etc/fstab
7. Exit chroot
8. Delete openSUSE installation on /dev/sda1
9. Install grub2 and configure from Mint

Fiiiiiiiiiinally. Done. Here's how my disk is partitioned now, with both openSUSE Leap 42.1 and Linux Mint 18 copied 
to the new partition:

![New Partition]({attach}images/newpartition.png)

## What I Learned
1. Perhaps a program like Clonezilla is better in this situation. I have used it previously, and frankly I don't recall having to update UUIDs. My memory could be wrong though. I do remember that it's a pain to copy a Clonezilla image to a different partition. Well, pain is stretching it. One of the files in the Clonezilla folder for the image needs to be updated with the new partition. 
2. This whole updating initial ram disks was fun. I have to keep this in mind as a first level troubleshooting technique, right behind...
3. Can't tell you how many times I've had issues booting into a distro, and the solution being **UPDATE /etc/fstab**! This has almost become second nature to me now, to check this when I can't boot into a distro. 
4. One of the "joys" of working with different distros is figuring out how to do the same exact thing with different (unique) commands, e.g. **mkinitrd** vs. **update-initramfs**. I say joy now, but sometimes I wonder why the hell I'm diluting my knowledge. It rather confuses me sometimes. Perhaps I'd be better off REALLY knowing how to update initial ram disks in Debian, for example, and to hell with the rest. Hmmmm...nah. I like tinkering too much. But it does mean I have to relearn quite a bit. 
5. The most important thing I did?? I WROTE THIS ALL DOWN! Seriously, I've performed these steps more than once, and as I just mentioned, I had to start from scratch each time I did this. I'm really happy I have a blog that no one will likely read. At least as far as this. If you have...wow, I'm grateful you have. Truly.








 




