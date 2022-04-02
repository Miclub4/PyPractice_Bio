from pathlib import Path

# Data source: http://combio.pl/files/pfam.zip

oh = open('Intersection.txt', 'w')

dict = {}
for t in ['virus', 'host']:
    dict[t] = {}
    data_path = Path(f'./{t}/pfam/')
    for f in data_path.iterdir():
        id = f.stem
        dict[t][id] = set()
        fh = open(f)
        for line in fh:
            line = line.strip()
            if line and not line.startswith('#'):
                sl = line.split()
                pfam_id = sl[5]
                evalue = float(sl[12])
                if evalue <= 0.001:
                    dict[t][id].add(pfam_id)
        fh.close()


vids = list(dict['virus'].keys())
hids = list(dict['host'].keys())

for vid in vids:
    for hid in hids:
        intersection = len(dict['virus'][vid].intersection(dict['host'][hid]))
        oh.write(f'{vid}\t{hid}\t{intersection}\n')
oh.close()