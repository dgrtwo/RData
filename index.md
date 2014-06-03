---
layout: default
title: Data Analysis and Visualization Using R
---

Data Analysis and Visualization Using R
============

This is a course that combines video and interactive elements to teach the statistical programming language R.

{% for i in (1..4) %}
{% for page in site.pages %}
{% if page.layout == 'lesson'%}
{% if page.index == i %}
* [{{ page.title }}]({{ site.baseurl }}{{ page.url }})
{% endif %}
{% endif %}
{% endfor %}
{% endfor %}
