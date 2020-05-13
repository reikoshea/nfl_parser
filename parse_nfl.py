#!/usr/bin/env python3

import csv
import sys
from decimal import *
from operator import itemgetter
from tabulate import tabulate

getcontext().prec = 4

if len(sys.argv) < 2:
  print("%s [INFILE]" % sys.argv[0])
  sys.exit()

with open(sys.argv[1], "r") as pbp:

    reader = csv.reader(pbp, skipinitialspace=True)
    header = next(reader)
    data_table = [dict(zip(header, map(str, row))) for row in reader]

passers = {}

for i in data_table:
#  if i["play_type"] != "pass":
#    continue
#  if i["qb_epa"] == "NA" or i["cpoe"] == "NA":
#    continue
  if i["passer"] == "NA":
    continue
  if i["passer"] not in passers:
    passers[i["passer"]] = {}
  else:
    try:
      passers[i["passer"]]["cpoe"] = passers[i["passer"]].get("cpoe", Decimal(0)) + Decimal(i["cpoe"])
      passers[i["passer"]]["cpoe_at"] = passers[i["passer"]].get("cpoe_at", 0) + 1
    except InvalidOperation:
      pass

    try:
      passers[i["passer"]]["qb_epa"] = passers[i["passer"]].get("qb_epa", Decimal(0)) + Decimal(i["qb_epa"])
      passers[i["passer"]]["qb_epa_at"] = passers[i["passer"]].get("qb_epa_at", 0) + 1
    except InvalidOperation:
      pass

output = []
for passer in passers:
  if "qb_epa" not in passers[passer] or "cpoe" not in passers[passer]:
    continue
  if passers[passer]["qb_epa_at"] < 200 or passers[passer]["cpoe_at"] < 200:
    continue
  output.append([passer, passers[passer]["cpoe"]/passers[passer]["cpoe_at"], passers[passer]["cpoe_at"], passers[passer]["qb_epa"]/passers[passer]["qb_epa_at"], passers[passer]["qb_epa_at"]])

output.sort(key=itemgetter(1), reverse=True)
print(tabulate(output, headers=["QB", "CPOE", "CPOE ATTEMPTS", "EPA", "EPA ATTEMPTS"]))
for row in output:
  print("%s,%s,%s" % (row[0], row[1], row[3]))
