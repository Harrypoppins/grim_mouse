#!/usr/bin/python

import glob,filecmp,shutil,os,subprocess

modpath = '/Users/tpfaff/grimex'
origpath = '/Users/tpfaff/grimex_orig'
patchpath = 'dists/engine-data/patches/grim_pnc'

for i in glob.glob(patchpath+'/*.lua.patchr'):
	os.remove(i)

neq = 0
tot = 0
for new_file in glob.glob(modpath+'/*.lua'):
	old_file = new_file.replace(modpath,origpath)
	patch_file = patchpath + '/' + os.path.basename(new_file) + '.patchr'
	if not filecmp.cmp(old_file,new_file,False):
		neq += 1
		subprocess.call(['./diffr',old_file,new_file,patch_file],shell=False)
	tot += 1
print ('%d/%d files copied' % (neq,tot))