import wget
import csv
from ete3 import NCBITaxa
import json
import os

link3 = 'ftp://ftp.genome.jp/pub/db/virushostdb/virushostdb.tsv'
wget.download(link3)

ncbi = NCBITaxa()
DictBaseDB={}
n = open("DictBaseDB.json", "w")


with open('virushostdb.tsv') as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter='\t')
    next(tsvreader)
    for line in tsvreader:
        DictDB = {}
        L1 = []
        X1 = []
        C1 = []
        C2 = []
        n1 = line[3:4]      #row(refseqid)
        n2 = line[1:2]      #row(virus name)
        n3 = line[7:8]      #row(host tax id)
        n4 = line[10:11]    #row(pmid)
        n5 = line[11:12]    #row(evidence)
        for i3 in n4:
            Cdb3=i3         #pmid
            DictDB['pmid']=C2
            if i3:
                Cdb33=Cdb3.split(', ')
                for items in Cdb33:
                    C2.append(items)
        for i4 in n5:
            Cdb4=i4         #evidence
            DictDB['evidence']=C1
            if i4:
                Cdb44=Cdb4.split(', ')
                for items in Cdb44:
                    C1.append(items)
        for i in n1:
            for z in i.split(", "):
                Cdb=z    # NC_000000 (itp)
        for i1 in n2:
            Cdb1=i1      # name
            DictDB['name']=Cdb1
        for i2 in n3:
            Cdb2=i2     # host tax id
            x=ncbi.get_lineage(Cdb2)
            if x is not None:
                if 2157 in x or 2 in x:
                    x1 = sorted(x)  # lineage = x1
                    DictDB['lineage'] = x1
                    y1 = ncbi.get_taxid_translator(x1)
                    z1 = ncbi.get_rank(x1)
                    for key, value in y1.items():
                        L1.append(value)  # lineage_names = L1
                        DictDB['lineage_names'] = L1
                    for key, value in z1.items():
                        X1.append(value)  # lineage_rank = X1
                        DictDB['lineage_rank'] = X1
                        DictBaseDB[Cdb] = DictDB



json.dump(DictBaseDB, n, indent=3)
n.close()
os.remove("virushostdb.tsv")