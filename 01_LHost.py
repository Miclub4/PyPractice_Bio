import wget
import gzip
import os
link1 = 'ftp://ftp.ncbi.nlm.nih.gov/refseq/release/viral/viral.1.genomic.gbff.gz'
link2 = 'ftp://ftp.ncbi.nlm.nih.gov/refseq/release/viral/viral.2.genomic.gbff.gz'
wget.download(link1)
wget.download(link2)

# .gz -> .txt change

Gene_File1_Source = "viral.1.genomic.gbff.gz"
Gene_File2_Source = "viral.2.genomic.gbff.gz"

with gzip.open(Gene_File1_Source, "rb") as file:
    file_content = file.read()
    Gene_File1 = "GeneFile1.txt"
    with open(Gene_File1, "wb") as file:
        file.write(file_content)
with gzip.open(Gene_File2_Source, "rb") as file:
    file_content = file.read()
    Gene_File1 = "GeneFile2.txt"
    with open(Gene_File1, "wb") as file:
        file.write(file_content)


def Cutter(File_name, File_name2):
    fh = open(File_name)
    HH = open("LocusHost.txt", "w")
    for line in fh:
        if line.startswith("LOCUS"):
            HH.write(line[12:21] + "\t")
        if line.startswith("                     /host="):
            HH.write(line[28:].replace('\"', ''))
        if line.startswith("                     /lab_host="):
            HH.write(line[32:].replace('\"', ''))
    HH.close()
    fh.close()

    oh = open("LocusHost.txt", "r")
    nh = open(File_name2, "w")
    for line in oh:
        host = ""
        if (line.startswith("NC") or line.startswith("AC")):
            x = line.split()
            a = 0
            for z in x:
                if z[1:3] == "C_":
                    a = a + 1
                if z[1:3] != "C_":
                    host = host + z + " "
            if host:
                nh.write(x[a - 1] + "\t" + host + "\n")
        if not (line.startswith("NC") or line.startswith("AC")):
            nh.write(x[a - 1] + "\t" + line)
    oh.close()
    nh.close()


Cutter("GeneFile1.txt", "LocusHostFinal1.txt")
Cutter("GeneFile2.txt", "LocusHostFinal2.txt")

with open("LocusHostFinal1.txt") as fp:
    data = fp.read()
with open("LocusHostFinal2.txt") as fp:
    data2 = fp.read()

data += "\n"
data += data2

with open("LHost.txt", "w") as fp:
    fp.write(data)



os.remove("GeneFile1.txt")
os.remove("GeneFile2.txt")
os.remove("LocusHostFinal1.txt")
os.remove("LocusHostFinal2.txt")
os.remove("viral.1.genomic.gbff.gz")
os.remove("viral.2.genomic.gbff.gz")
os.remove("LocusHost.txt")