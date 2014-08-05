#!/usr/bin/env python
"""
Turn the code_lesson.Rmd knitr files into individual text files
"""

import sys
import os
import re

input_dir = os.path.join("_transcript", "raw")
output_dir = os.path.join("_transcript", "transcripts")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for f in os.listdir(input_dir):
    input_file = os.path.join(input_dir, f)
    lesson_number = re.search("lesson(\d)", f).groups()[0]

    last_newline = False
    outf = None

    with open(input_file) as inf:
        for l in inf:
            m = re.match("Segment (\d):", l)
            if m is not None:
                if outf:
                    outf.close()

                output_file = os.path.join(output_dir,
                                        "lesson%s_segment%s.txt" %
                                        (lesson_number, m.groups()[0]))
                outf = open(output_file, "w")

            if outf is None:
                # no file yet
                continue

            if "</a>" in l:
                # skip hyperlink anchor lines
                continue

            if len(l) == 1:
                # skip multiple newlines in a row
                if last_newline:
                    continue
                last_newline = True
            else:
                last_newline = False

            if l.endswith(":\n"):
                # remove : at end of lines
                l = l[:-2] + "\n"

            outf.write(l)
