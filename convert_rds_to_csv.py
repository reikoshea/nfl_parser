#!/usr/bin/env python3

import sys

if len(sys.argv) < 3:
  print("%s [INFILE] [OUTFILE]" % sys.argv[0])
  sys.exit()

from rpy2.robjects import r, pandas2ri
pandas2ri.activate()

readRDS = r['readRDS']
df = readRDS(sys.argv[1])

r['write.table'](x=df, file=sys.argv[2], sep=",", row_names=False)
