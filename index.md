---
layout: default
title: Data Analysis and Visualization Using R
---

Data Analysis and Visualization Using R
============

This is a course that combines video and interactive elements to teach the statistical programming language R.

{% for page in site.pages %}
{% if page.layout == 'lesson' %}  
* [{{ page.title }}]({{ page.url }})
{% endif %}
{% endfor %}
