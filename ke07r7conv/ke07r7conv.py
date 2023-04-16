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

rootdir = '/data1/jiany37/KE07-R7-2_Conv_Seb'
result = {}
count = 0
for file in os.listdir(rootdir):
    d = os.path.join(rootdir, file)
    if os.path.isdir(d):
        trajj = []
        mdddrun = []
        mdddcon = []
        checkpint = True
        for child in os.listdir(d):
            if file in child and( file != "snapshots" and file != "QMMM") :
                checkpint = False
                trajj.append(d +"/" + child + "/MD/prod.nc")
        if checkpint == False:
            for mdfile in os.listdir(d +"/" + file + "1/MD"):
               	    if ".in" in mdfile or "0.rs" == mdfile:
                        mdddrun.append({mdfile: detect(d +"/" + file + "1/MD/" + mdfile)})
            for mdfile in os.listdir(d +"/" + file + "1"):
                    if ".prmtop" in mdfile or ".inpcrd" in mdfile:
                        mdddcon.append(d +"/" + file + "1/MD/" + mdfile)
            mdddcon.append(parseleap(d +"/" + file + "1/cache/leap.in")) 
        if checkpint == False:
                count += 1
                temp = {}
                tempconfig = {}
                rs = {}
                newmdddrun = []
                for i in mdddrun: 
                    if '0.rs' in i:
                        rs = i['0.rs']
                    else:
                        newmdddrun.append(i)
                for i in range(0,len(newmdddrun)):
                    listkey = list(newmdddrun[i].keys())[0]
                    newmdddrun[i][listkey]['DISANG'] = rs
                tempconfig["runtime-config"] = newmdddrun
                tempconfig["md-configuration"] = mdddcon
                temp["md-conig"] = tempconfig
                temp['traj'] = trajj
                temp["structure"] = [(d +"/" + file + "1/MDInput_" + file + "_rmH_aH_min_rmW.pdb") , (d +"/" + file + "1.py")]
                temp["ligand"] = {"smiles": "c1cc2c(cc1N(=O)=O)cno2", "cif": "file-in-future", "binding": "precomplex","binding_method": ["reference_SI","https://www.nature.com/articles/nature06879"]}
                temp["mutation"] = file
                pdbpah = ""
                for pdbfile in os.listdir(d +"/" + file + "1"):
                    if "_rmH_aH_min_rmW.pdb" in pdbfile:
                        pdbpath = pdbfile
                seqList = list(SeqIO.parse((d +"/" + file + "1/" + pdbpath), "pdb-atom"))
                temp["sequence"] = str(seqList[0].seq)
                result[file] = temp 		
json_obj = json.dumps(result)
with open("result.json", "w") as outfile:
    outfile.write(json_obj)
