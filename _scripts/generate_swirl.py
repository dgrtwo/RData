#!/usr/bin/env python
"""
Generate YAML files for Swirl interactive quizzes.

These are placed in a folder RData-quizzes outside of the site's folder. This
directory is on the "quizzes" branch of the RData repository.
"""

import os
import shutil

import yaml

OUTFOLDER = os.path.join("..", "RData-quizzes")

DATA_DIR = "_data"
OUTLINE_FILE = os.path.join(DATA_DIR, "outline.yml")
QUIZ_FILE = os.path.join(DATA_DIR, "quizzes.yml")

UNIVERSAL_FILES = [os.path.join("_swirl", "customTests.R")]

with open(OUTLINE_FILE) as outline_inf, open(QUIZ_FILE) as quiz_inf:
    lessons = yaml.load(outline_inf)
    quizzes = yaml.load(quiz_inf)

    meta = quizzes["meta"]
    for lesson_number, lesson in enumerate(lessons):
        lesson_number += 1

        initLesson = lesson.get("initLesson", "") + "\n"

        for segment_number, segment in enumerate(lesson["segments"]):            
            segment_number += 1

            meta["Course"] = "%d. %s" % (lesson_number, lesson["title"])
            meta["Lesson"] = "%d.%d %s" % (lesson_number, segment_number,
                                            segment["title"])

            try:
                les = quizzes[lesson_number]
                seg = les["segments"][segment_number]
                questions = seg["Questions"]
            except KeyError:
                continue

            if "video" in segment:
                vq = {"Class": "video", "Output":
                    "Would you like to re-watch the video for this segment?",
                    "VideoLink": "http://youtu.be/" + segment["video"]}
                questions = [vq] + questions

            outdir = os.path.join(OUTFOLDER, meta["Course"].replace(" ", "_"),
                                   meta["Lesson"].replace(" ", "_"))
            if not os.path.exists(outdir):
                os.makedirs(outdir)

            for uf in UNIVERSAL_FILES:
                shutil.copy(uf, outdir)

            with open(os.path.join(outdir, "lesson.yaml"), "w") as outf:
                yaml.dump([meta] + questions, outf)

            initLesson = "\n".join((les.get("initLesson", ""),
                                    seg.get("initLesson", "")))
            with open(os.path.join(outdir, "initLesson.R"), "w") as outf:
                outf.write(initLesson)
