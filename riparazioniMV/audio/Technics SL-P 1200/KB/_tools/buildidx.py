import csv, re, json, collections
meta = json.load(open('sheets_meta.json'))
RX = re.compile(r'(?<![A-Z])(IC|TJ|VR|CN|FC|FL|ZD|BT|RL|Q|D|R|C|L|S|T|X)([0-9OIL]{3,4})')
PART = re.compile(r'^((AN|MN|BA|TA|TC|LA|NJM|HA|UPC|M5|SVG|UN|MA|LN|SN|TL|NE|UPD|MB|HD|SE|RH|TD|SL|ON|KIA|SI|2S[ABCDJK])[0-9][0-9A-Z\-]{1,10})$')
fix = str.maketrans({'O': '0', 'I': '1', 'L': '1'})
rows = []
for s, m in meta.items():
    W, H = m['size']
    for rot in ('r0', 'r90'):
        with open(f'tsv/{s}_{rot}.tsv', newline='') as fh:
            for r in csv.DictReader(fh, delimiter='\t', quoting=csv.QUOTE_NONE):
                t = (r.get('text') or '').strip().strip('.,:;()[]|')
                if not t or float(r['conf']) < 20:
                    continue
                x = int(r['left']) + int(r['width']) // 2
                y = int(r['top']) + int(r['height']) // 2
                if rot == 'r90':
                    x, y = y, H - 1 - x
                tu = t.upper()
                tu = re.sub(r'^[1L|]C(?=[0-9OIL])', 'IC', tu)
                found = []
                for m1 in RX.finditer(tu):
                    p, n = m1.group(1), m1.group(2).translate(fix)
                    if not n.isdigit():
                        continue
                    if len(n) > 3 and p != 'IC':
                        n = n[:3]
                    found.append((p + n, 'ref'))
                if PART.match(tu):
                    found.append((tu, 'part'))
                tiles = [tt['tile'][:-4] for tt in m['tiles']
                         if tt['box'][0] <= x < tt['box'][2] and tt['box'][1] <= y < tt['box'][3]]
                for tok, kind in found:
                    rows.append((tok, kind, s, x, y, '/'.join(tiles), float(r['conf'])))
rows.sort()
out = []
for r in rows:
    if out and out[-1][0] == r[0] and out[-1][2] == r[2] and abs(out[-1][3] - r[3]) < 40 and abs(out[-1][4] - r[4]) < 40:
        continue
    out.append(r)
with open('KB/index_components.tsv', 'w') as f:
    f.write('# token\tkind\tsheet\tx300\ty300\ttiles\tocr_conf\n')
    for r in out:
        f.write('%s\t%s\t%s\t%d\t%d\t%s\t%.0f\n' % r)
print(len(out))
print(collections.Counter(r[0][:2] for r in out).most_common(20))
