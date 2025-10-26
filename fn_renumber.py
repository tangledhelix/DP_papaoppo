#!/usr/bin/env python3
#
# Find footnotes, renumber them to a simple linear series, each
# a unique integer in the entire book.
#
# Before: Footnote_1_1, Footnote_1_2, Footnote_2_1, Footnote_2_2
# After:  Footnote_1_1, Footnote_2_2, Footnote_3_3, Footnote_4_4

import re
import sys

fncount = 1
data = {}

n = None

# create a map
with open("papaoppo.html", "r") as f:
    for line in f.readlines():
        if match := re.search(r'id="Footnote_(\d+_\d+)"', line):
            data[match[1]] = fncount
            print(f"{match[1]} => {fncount}")
            fncount += 1

# now go back over the file and regex it and write result back out
with open("papaoppo.html", "r") as fin:
    with open("papaoppo-new.html", "w") as fout:
        for line in fin.readlines():
            if match := re.search(r'Footnote_\d+.*Footnote\d+', line):
                print("Found multiple footnotes on one line")
                sys.exit(1)
            n = None
            #                        1                   2        3                   4        5                      6    7
            if match := re.search(r'^(.*<a id="FNanchor_)(\d+_\d+)(" href="#Footnote_)(\d+_\d+)(" class="fnanchor">\[)(\d+)(\]</a>.*)$', line):
                if match[2] in data:
                    n = data[match[2]]
                else:
                    print(f"ERROR NOT FOUND IN DATA {match[2]}")
                    sys.exit(1)
                print(f"Anchor {match[2]} -> Footnote {match[4]} (Label {match[6]}) => _{n}_{n}")
                line = f"{match[1]}{n}_{n}{match[3]}{n}_{n}{match[5]}{n}{match[7]}\n"
            #                          1                   2        3                   4        5                   6    7
            elif match := re.search(r'^(.*<a id="Footnote_)(\d+_\d+)(" href="#FNanchor_)(\d+_\d+)(" class="label">\[)(\d+)(\]</a>.*)$', line):
                if match[2] in data:
                    n = data[match[2]]
                else:
                    print(f"ERROR NOT FOUND IN DATA {match[2]}")
                    sys.exit(1)
                print(f"Footnote {match[2]} -> Anchor {match[4]} (Label {match[6]}) => _{n}_{n}")
                line = f"{match[1]}{n}_{n}{match[3]}{n}_{n}{match[5]}{n}{match[7]}\n"

            fout.write(line)
