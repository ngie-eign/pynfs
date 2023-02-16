#!/usr/bin/env python3

from __future__ import print_function

import os
import subprocess
import sys

try:
    import ply
except ImportError:
    # Avoid confusing cascading failures due to how xdrgen is imported via
    # setup.py files in subdirs.
    sys.exit("You must install ply first.")

DESCRIPTION = """
pynfs
============

Add stuff here.
"""

DIRS = ["xdr", "rpc", "nfs4.1", "nfs4.0"] # Order is important

def setup(*args, **kwargs):
    cwd = os.getcwd()
    for dir in DIRS:
        print("\n\nMoving to %s" % dir )
        os.chdir(os.path.join(cwd, dir))
        rc = subprocess.call([sys.executable] + sys.argv)
        if "clean" not in sys.argv and rc:
            sys.exit(rc)
    os.chdir(cwd)

setup(name = "pynfs",
      version = "0.0.0", # import this?
      packages = ["nfs4", "rpc", "xdr"],
      description = "NFS tools, tests, and support libraries",
      long_description = DESCRIPTION,
      #install_requires = ["gssapi", "ply"],

      # These will be the same
      author = "Fred Isaman",
      author_email = "iisaman@citi.umich.edu",
      maintainer = "Fred Isaman",
      maintainer_email = "iisaman@citi.umich.edu",
      url = "http://www.citi.umich.edu/projects/nfsv4/pynfs/",
      license = "GPL"
      
      )

