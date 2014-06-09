Data Analysis and Visualization Using R: Course Website
=====

This is the source code for the [Data Analysis and Visualization Using R course website](http://dgrtwo.github.io/RData/).

The course, material and site were created by [David Robinson](http://dgrtwo.github.io) with contributions from Neo Christopher Chung. For license and copyright information, see [here](http://dgrtwo.github.io/RData/about).

Technical Details
=====

This page is hosted on [Github Pages](https://pages.github.com/) and powered by static site generator [Jekyll](http://jekyllrb.com/), meaning it's free to host on GitHub. Please feel free to adapt the site to your own course.

The course is divided into **Lessons**, which are each in turn divided into **Segments**. You first build an outline of your courses in the [_data/outline.yml](_data/outline.yml) file, which contains an outline of the course in [YAML](http://www.yaml.org/) format.

The one catch is that if you *add* lessons or segments (not just changing their titles or content), you should re-run the [_scripts/generate_lessons.py](generate_lessons.py) script to create empty pages for them. This requires Python and the [PyYAML](http://pyyaml.org/) package.