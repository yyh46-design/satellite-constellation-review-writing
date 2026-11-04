"""Assemble V3.4: abstract and chapters 1-3 plus references from V3.3,
chapter 4 and chapter 5 from the confirmed plain-text files.
Usage: python3 -I assemble_v34.py V3.3.md CH4.md CH5.md OUT.md"""
import re
import sys

v33, ch4, ch5, out = sys.argv[1:5]
V = open(v33, encoding='utf-8').read()
head = V[:V.index('\n# 4 ') + 1]
refs = V[V.index('\n# 参考文献'):]


def to_md(text):
    lines, md, table = text.strip('\n').split('\n'), [], []

    def flush():
        if table:
            md.append('| ' + ' | '.join(table[0]) + ' |')
            md.append('|' + '---|' * len(table[0]))
            for r in table[1:]:
                md.append('| ' + ' | '.join(r) + ' |')
            md.append('')
            table.clear()

    for ln in lines:
        if '\t' in ln:
            table.append(ln.split('\t'))
            continue
        flush()
        if not ln.strip():
            continue
        if re.match(r'^\d \S', ln):
            md += ['# ' + ln, '']
        elif re.match(r'^\d\.\d\.\d \S', ln):
            md += ['### ' + ln, '']
        elif re.match(r'^\d\.\d \S', ln):
            md += ['## ' + ln, '']
        elif re.match(r'^表\d+ ', ln):
            md += ['**' + ln + '**', '']
        else:
            m = re.match(r'^(（\d）[^。]*。) (.*)$', ln)
            md += (['**' + m.group(1) + '** ' + m.group(2)] if m else [ln]) + ['']
    flush()
    return '\n'.join(md) + '\n'


body = to_md(open(ch4, encoding='utf-8').read()) + '\n' + to_md(open(ch5, encoding='utf-8').read())
open(out, 'w', encoding='utf-8').write(head + body + refs)
print('written', out)
