########################
# Author: Minghao Zhao
# Date: 4-15-2023
########################

# This is the main file of this project. Pass in the parent folder path, it will automatically parse all the files that we are intersted in. 

import os
import json
from Bio import SeqIO
from detect import *
from parseleap import *
import re  

rootdir = '/data1/jiany37/KE07-R7-2_Random_Seb'
result = {}
count = 0
for file in os.listdir(rootdir):
    d = os.path.join(rootdir, file)
    if file == 'ligands' or file == 'metalcenters':
        continue
    if os.path.isdir(d):
        trajj = []
        mdddrun = []
        mdddcon = []
        checkpint = True
        trajj.append(d + "/MD/prod.nc")
        for mdfile in os.listdir(d + "/MD"):
            if ".in" in mdfile or "0.rs" == mdfile:
                mdddrun.append({mdfile: detect(d + "/MD/" + mdfile)})
        if ".prmtop" in mdfile or ".inpcrd" in mdfile:
            mdddcon.append(d +"/" + file + "/MD/" + mdfile)
        mdddcon.append(parseleap(d +"/cache/leap.in")) 
        count += 1
        temp = {}
        tempconfig = {}
        rs = {}
        newmddddrun = []
        for i in mdddrun:
            if '0.rs' in i:
                rs = i['0.rs']
            else:
                newmddddrun.append(i)
        for i in range(0,len(newmddddrun)):
            listkey = list(newmddddrun[i].keys())[0]
            newmddddrun[i][listkey]['DISANG'] = rs
        tempconfig["runtime-config"] = mdddrun
        tempconfig["md-configuration"] = mdddcon
        temp["md-conig"] = tempconfig
        temp['traj'] = trajj
        pdbpath = ''
        mutant = ''
        for pdb in os.listdir(d):
            if "MDInput_" in pdb and "_rmH_aH_min_rmW.pdb" in pdb:
                pdbpath = pdb
                mutant= re.findall("[A-Z][A-Z][0-9]+[A-Z]", pdb)[0]
        temp['mutation'] = mutant
        temp["structure"] = [(d + '/'  + pdbpath) , (d +"/1.py")]
        temp["ligand"] = {"smiles": "c1cc2c(cc1N(=O)=O)cno2", "cif": "file-in-future", "binding": "precomplex","binding_method": ["reference_SI","https://www.nature.com/articles/nature06879"]}
        seqList = list(SeqIO.parse((d +"/" + pdbpath), "pdb-atom"))
        temp["sequence"] = str(seqList[0].seq)
        result[file] = temp 		

json_obj = json.dumps(result)
with open("result.json", "w") as outfile:
    outfile.write(json_obj)

