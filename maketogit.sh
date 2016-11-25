#! /bin/bash

make html
cd output
git add . && git commit -m "Updated" && git push -u origin master
cd ..
git add . && git commit -m "Updated" && git push -u origin master
