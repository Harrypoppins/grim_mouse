#!/usr/bin/python
import glob,struct,sys

class Dataset:
	pass

def writestring(fp,str):
	fp.write(struct.pack('i',len(str)))
	for c in str:
		fp.write(struct.pack('c',c))

dset = []
sname = []
for file in glob.glob('*.set.hot'):
	set = file.replace('.set.hot','')
	with open(file,'r') as fin:
		print (file)
		data = []
		for line in fin:
			line = line.strip()
			if not line:
				continue
			d = Dataset()
			[startp,_,interm] = line.partition('"')
			[d.name,_,endp] = interm.partition('"')
			[setup,_,d.id] = startp.strip().partition(' ')
			d.setup = int(setup)
			tok = endp.strip().split(' ')
			d.type = int(tok[0])
			d.pos = [float(tok[1]),float(tok[2]),float(tok[3])]
			d.num = int(tok[4])
			d.poly=[]
			for i in range(d.num*2):
				d.poly.append(int(tok[5+i]))
			data.append(d)
		dset.append(data)
		sname.append(set)

with open('../dists/engine-data/patches/grim_pnc/set.bin','wb') as fout:
	fout.write(struct.pack('i',len(dset)))
	for i in range(len(dset)):
		writestring(fout,sname[i])
		fout.write(struct.pack('i',len(dset[i])))
		for d in dset[i]:
			writestring(fout,d.id)
			writestring(fout,d.name)
			fout.write(struct.pack('iifffi',d.setup,d.type,d.pos[0],d.pos[1],d.pos[2],d.num))
			for i in d.poly:
				fout.write(struct.pack('i',i))
