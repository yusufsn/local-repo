#!/usr/bin/env python

import os
from git import *

userhome = os.path.expanduser("~")
g = Git(userhome + "/local-repo/")
logs = g.log("--pretty='COM%s'", "--date=short", "--name-only").split('COM')

for log in logs:
	print (log)