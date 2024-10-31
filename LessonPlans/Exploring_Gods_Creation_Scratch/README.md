---
layout: default
title: "Introduction to Coding with Scratch Jr & Scratch"
classroom: []
lesson: 
curriculam: "yes"
author: "Joe Vandermark"
published: "31 Oct 2024"
---


# STEM Lesson Plans with Scratch Jr

Welcome to the collection of STEM lesson plans integrating **Scratch Jr** for various grade levels. Each lesson is designed to combine coding education with faith-based learning, encouraging students to explore technology responsibly and creatively.

## Lesson Plans

### Kindergarten
{% assign lesson_kindergarten_pages = site.pages | where: "lesson", "Exploring_Gods_Creation_Scratch" | where_exp: "item", "item.classroom contains 'kindergarten'" %}
{% for page in lesson_kindergarten_pages %}
- [{{ page.title }}]({{ page.url  | absolute_url }})
{{page.description }}
{% endfor %}


### Grades 1-3
{% assign lesson_grades1_3_pages = site.pages | where: "lesson", "Exploring_Gods_Creation_Scratch" | where_exp: "item", "item.classroom contains 'grades1_3'" %}
{% for page in lesson_grades1_3_pages %}
- [{{ page.title }}]({{ page.url  | absolute_url }})
{{page.description }}
{% endfor %}


### Grades 4-6
{% assign lesson_grades4_6_pages = site.pages | where: "lesson", "Exploring_Gods_Creation_Scratch" | where_exp: "item", "item.classroom contains 'grades4_6'" %}
{% for page in lesson_grades4_6_pages %}
- [{{ page.title }}]({{ page.url  | absolute_url }})
{{page.description }}
{% endfor %}

---

### Description

These lesson plans aim to:

- Introduce students to basic and advanced coding concepts using Scratch Jr.
- Foster creativity, problem-solving, and critical thinking skills.
- Integrate Catholic teachings and values into technology education.

---

### How to Use

1. **Navigate to the Lesson Plan**: Click on the link for the desired grade level to access the lesson plan.
2. **Review Materials**: Each lesson plan includes an overview, objectives, materials needed, lesson steps, Catholic integration, assessment methods, and closing prayer.
3. **Engage with Parent Resources**: At the end of each lesson, there are resources for parents to support their child's learning at home.

---

**Note:** These lesson plans are part of an ongoing effort to enrich STEM education with ethical and spiritual dimensions, preparing students to use technology for the common good.

