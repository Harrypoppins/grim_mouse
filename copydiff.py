#!/usr/bin/python

import glob,filecmp,shutil,os

patchpath = 'dists/engine-data/patches/grim_pnc'
for i in glob.glob(patchpath+'/*.lua'):
	os.remove(i)

neq = 0
tot = 0
for i in glob.glob('/Users/tpfaff/grimex/*.lua'):
	if not filecmp.cmp(i,i.replace('grimex','grimex2'),False):
		neq += 1
		dest = patchpath + '/' + os.path.basename(i)
		shutil.copy(i,dest)
	tot += 1
print ('%d/%d files copied' % (neq,tot))