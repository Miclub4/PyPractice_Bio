from pathlib import Path
import json


# Data source: http://www.combio.pl/files/edwards.zip

virus_source = Path('virus/')
host_source = Path('host/')
Viruses = open('VirusBase.json', 'w')
Hosts = open('HostsBase.json', 'w')

VirusBase={}
HostBase={}

def BaseMaker(Base, location, type):
    for entry in location.iterdir():
        n=open(entry,'r')
        count=0
        countall=0
        for line in n:
            if not line.startswith('>'):
                count += line.count('G') + line.count('C')
                countall += len(line)
                Dif=((count/countall)*100)
                Base[entry.name[:-4]]=Dif
    json.dump(Base, type, indent=3)
    type.close()

BaseMaker(VirusBase, virus_source, Viruses)
BaseMaker(HostBase, host_source, Hosts)


# GC content distance

a=open('Distance.txt', 'w')
Vn=open('VirusBase.json')
Hn=open('HostsBase.json')
Vdata=json.load(Vn)
HData=json.load(Hn)

for key1,value1 in Vdata.items():
    for key2,value2 in HData.items():
        a.write(f'{key1}\t{key2}\t{round(abs(value1-value2),2)}%\n')
a.close()
Vn.close()
Hn.close()