---
layout: default
title: Data Analysis and Visualization Using R
---

Data Analysis and Visualization Using R
============

This is a course that combines video, HTML and interactive elements to teach the statistical programming language R.

{% for lesson in site.data.outline %}
{% capture lessonnumber %}{{ forloop.index }}{% endcapture %}
* [Lesson {{ lessonnumber }}: {{ lesson.title }}](lessons/lesson{{ lessonnumber}})
{% for segment in lesson.segments %}
{% capture segmentnumber %}{{ forloop.index }}{% endcapture %}
 * [{{ lessonnumber }}.{{ segmentnumber }} {{ segment }}](lessons/lesson{{ lessonnumber}}/segment{{ segmentnumber }})
{% endfor %}
{% endfor %}
