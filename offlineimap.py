#!/usr/bin/env python
import os
import subprocess
from os.path import expanduser
homedir = expanduser("~")

def mailpasswd(acct):
  acct = os.path.basename(acct)
  path = homedir + "/.passwd/%s.gpg" % acct
  args = ["gpg", "--use-agent", "--batch", "-qd", path]
  try:
    return subprocess.check_output(args).strip()
  except subprocess.CalledProcessError:
    return ""
