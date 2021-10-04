# -------------------------------------------------------------------
# --Chipspirit Proprietary
# --Copyright (C) 2020 Chipspirit
# --All Rights Reserved
# -------------------------------------------------------------------
# --File Name		  : compare_normal.py
# --Creation Date	  : 12-05-2020
# --Last Modified         : Tuesday 12 May 2020 03:14:14 PM IST
# --Author 		  : Sumit Kavathekar
# --Author's Email	  : sumit.kavathekar@chipspirit.com
# --Project Name 	  : ABHED-1
# --Department		  : RTL Design 
# --Description 	  : 1st input file is 1st argument to be passed :golden
#                           2nd input file is 2nd argument to be passed :received
# --Run as                : python compare_block.py gldn.txt rcvd.txt

# --Detailed Description  :

# This script takes in 2 input arguments named as 1. golden txt file and 2. received txt file
# Then this script simply takes entries from rcvd.txt and compares it with entries in gldn.txt with depth selected as depth(rcvd.txt)
# If all entries match then COMPARISON SUCCESS else FAILURE !

import sys
import difflib
import fileinput

compare_files_error = 0

def file_len(file_name):
  with open(file_name) as f:
    for i, l in enumerate(f):
      pass
  return i+1
 
gldn=open(sys.argv[1],"r")
rcvd=open(sys.argv[2],"r")
 
depth_glden=file_len(sys.argv[1])
depth_rcvd=file_len(sys.argv[2])
print("depth of gldn.txt --> %s" %depth_glden)
print("depth of rcvd.txt --> %s" %depth_rcvd)

if(depth_rcvd > depth_glden):
  compare_files_error=1
  print('FAIL :: depth(received.txt) file is more than depth(golden.txt)')

for line2 in range (0,depth_rcvd,1):
  rcvd_line=rcvd.readline()
  glden_line=gldn.readline()
  if glden_line!=rcvd_line:
    compare_files_error=1
    break

if(compare_files_error == 0):
  print('COMPARISION SUCCESSFUL --> compare_files.py::compare_files_error = %s'%compare_files_error)
else:
  print('COMPARISON FAILED --> compare_files.py::compare_files_error = %s'%compare_files_error)

#sys.exit(compare_files_error)

gldn.close()
rcvd.close()

#Add the sys.exit() as per the requirement
