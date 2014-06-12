#!/usr/bin/env python
"""
Generate folders and markdown files for lessons and segments, based on
_data/outline.yml.

This should be run before running Jekyll.
"""

import os
import yaml


OUTLINE_FILE = os.path.join("_data", "outline.yml")


LESSON_HEADER = """---
layout: lesson
lesson: %d
---
"""


SEGMENT_HEADER = """---
layout: segment
lesson: %d
segment: %d
---
"""

QUIZ_HEADER = """---
layout: quiz
lesson: %d
segment: %d
---
"""


with open(OUTLINE_FILE) as outline_inf:
    lessons = yaml.load(outline_inf)
    for lesson_number, lesson in enumerate(lessons):
        lesson_number += 1

        lesson_dir = os.path.join("lessons", "lesson%d" % lesson_number)
        if not os.path.exists(lesson_dir):
            os.mkdirs(lesson_dir)

        # write lesson index page
        with open(os.path.join(lesson_dir, "index.md"), "w") as outf:
            outf.write(LESSON_HEADER % (lesson_number, ))

        for segment_number, segment in enumerate(lesson["segments"]):
            segment_number += 1
            segment_file = os.path.join(lesson_dir,
                                        "segment%d.md" % segment_number)
            with open(segment_file, "w") as segment_outf:
                content = SEGMENT_HEADER % (lesson_number, segment_number)
                segment_outf.write(content)

            # write quiz files
            quiz_dir = os.path.join("quizzes", "lesson%d" % lesson_number)
            quiz_file = os.path.join(quiz_dir, "segment%d.md" % segment_number)
            quiz_content = QUIZ_HEADER % (lesson_number, segment_number)
            if not os.path.exists(quiz_dir):
                os.makedirs(quiz_dir)
            with open(quiz_file, "w") as outf:
                outf.write(quiz_content)
