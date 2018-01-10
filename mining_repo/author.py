#!/usr/bin/env python

import os
from git import Repo

userhome = os.path.expanduser("~")
repo = Repo(userhome + "/local-repo/")

master = repo.commit('master')
master_author = master.author

for commit in repo.iter_commits():
	if commit.committer == master_author:
		print (commit)