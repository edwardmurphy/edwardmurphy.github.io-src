Title: R --> Python
Date: 2016-10-25
Modified: 2016-12-05
Tags: r, python

One of my current programming hobbies (long since "in the works" but really just "in the brain") is collecting and refactoring all of my R code and writing the same code in Python. The main purpose of refactoring my R code is to introduce myself to new libraries and functions in R, while also cleaning up code I wrote at the beginning of my R coding career. By rewriting these R scripts in Python, I can interactively and practically learn a new language. 

I'll be updating this post or creating new posts as progress is made, but for now the R code has been collected as is viewable in GitHub. The plan is to create a new repo for refactored R scripts and yet another repo for the corresponding Python scripts. I'll likely use IPython/Jupyter for the Python scripts to track my notes as I learn. I don't know if R code can be embedded in Jupyter notebooks, but if it can then perhaps I can save a step. 

Thanks for reading.
-Edward

UPDATE: Yep, R can be run in Jupyter. Fun. There are at least 2 ways to run R in Jupyter:

1. Run R "natively" using the R Kernal in Jupyter
2. Run R within the Python kernel using the rpy2 package

## R Kernel
To run R natively in Jupyter, [IRkernel](http://irkernel.github.io/installation) needs to be installed. I had a whale of a time installing the required dependency packages in R due to missing libraries (most notably libcurl and libcurl-openssl-devel). Within openSUSE Leap 42.1 I wasn't even able to locate the latter package within Yast. A Google search for the rpm file did the trick though. Oh, and gcc-c++ was needed as well for compilation. Also, install\_github didn't work at somet point. Had to use install\_git instead.
 
## R within Python Kernel
To do this, the **rpy2** package needs to be installed. I had all sorts of compilation issues using **pip** to install this, so I installed using the package manager (zypper in SUSE).

Once installed, [open up a Jupyter notebook]({filename}jupyternotes.md) and run:
```
%load_ext rpy2.ipython
```

That's it! R code can then be run using the R-magic command: prepend \%R before code. 
