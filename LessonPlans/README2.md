---
layout: default
title: "Page List"
---

## Curriculum Kindergarten
{% assign kindergarten_pages = site.pages | where: "classroom", "kindergarten" %}

{% for page in kindergarten_pages %}
- [{{ page.title }}]({{ page.url  | absolute_url }}) - {{page.description }}
{% endfor %}

## Curriculum Grades 1-3
{% assign grades1_3_pages = site.pages | where: "classroom", "grades1_3" %}

{% for page in grades1_3_pages %}
- [{{ page.title }}]({{ page.url  | absolute_url }}) - {{page.description }}
{% endfor %}

## Curriculum Grades 4-6
{% assign grades4_6_pages = site.pages | where: "classroom", "grades4_6" %}

{% for page in grades4_6_pages %}
- [{{ page.title }}]({{ page.url  | absolute_url }}) - {{page.description }}
{% endfor %}


### All Curriculam

{% assign curriculam_pages = site.pages | where: "curriculam", "yes" %}

{% for page in curriculam_pages %}
- [{{ page.title }}]({{ page.url  | absolute_url }}) - {{page.description }}
{% endfor %}

