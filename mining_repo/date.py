#!/usr/bin/env python

import os
from git import Repo
from time import gmtime, strftime

userhome = os.path.expanduser("~")
repo = Repo(userhome + "/local-repo/")

for commit in repo.iter_commits():
	date = gmtime(commit.committed_date)
	print (strftime("%Y/%m/%d %a %H:%M:%S +0000", date))