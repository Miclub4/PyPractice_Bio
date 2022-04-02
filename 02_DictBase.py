from ete3 import NCBITaxa
import json

ncbi = NCBITaxa()
DictBase={}
f = open("LHost.txt", "r")
n = open("DictBase.json", "w")

def DictMaker(a):
    for key, value in a.items():
        k = ncbi.get_lineage(value[0])
        if 2157 in k or 2 in k:
            k1 = sorted(k)  # lineage = k1
            Dict1['lineage'] = k1
            translate = ncbi.get_taxid_translator(k1)
            rank = ncbi.get_rank(k1)
            for key, value in translate.items():
                L1.append(value)  # lineage_names = L1
                Dict1['lineage_names'] = L1
            for key, value in rank.items():
                X1.append(value)  # lineage_rank = X1
                Dict1['lineage_rank'] = X1
                DictBase[C1] = Dict1

for line in f:
    Dict1={}
    L1 = []
    X1 = []
    x=line.split("\t")
    for y in x:
        if y.startswith("NC_") or y.startswith("AC_"):
            C1=y                                # NC_000000
        if y.endswith("\n"):
            C2=y[:-1]                           # Name
            Dict1['name']=C2
            h=ncbi.get_name_translator([y[:-1]])
            if bool(h) is False:
                z = y.split()
                hostshort = ""
                del z[2:]
                for i in z:
                    hostshort += str(i) + " "
                if ncbi.get_name_translator([hostshort[:-1]]):
                    y = ncbi.get_name_translator([hostshort[:-1]])
                    DictMaker(y)
            else:
                DictMaker(h)

json.dump(DictBase, n, indent=3)
f.close()
n.close()
