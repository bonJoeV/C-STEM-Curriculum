---
layout: default
title: "Introduction to Coding with Scratch Jr & Scratch"
classroom: []
lesson: "Building_Purpose_KEVA_Planks"
curriculam: "yes"
author: "Joe Vandermark"
published: "10 Oct 2024"
---

### C-STEM Coding Curriculum Overview

Our **C-STEM Engineering and Technology Curriculum** engages elementary students in foundational engineering principles and technology skills through interactive, faith-integrated activities. Utilizing hands-on tools like **Keva Planks**, **Makey Makey**, and **Dash Robots**, students explore engineering concepts such as structure, balance, and problem-solving, while reflecting on the Catholic values of stewardship, responsibility, and community. 

Each lesson encourages creativity, critical thinking, and ethical discussions, aligning technology and engineering education with Catholic teachings. This curriculum spans Kindergarten through 6th grade, equipping students with skills and values that inspire them to explore God’s creation through STEM.

For an introduction to our engineering tools and their classroom applications, explore our [Overview of Engineering Tools](./about_engineering_tools.md). This guide provides insights into each tool’s educational benefits, faith integration, and ways to engage students in hands-on learning that honors both innovation and stewardship.


<!-- No need to change below, this is a template for all projects. -->

## Lesson Plans

### Kindergarten
{% assign lesson_kindergarten_pages = site.pages | where: "lesson", { page.lesson } | where_exp: "item", "item.classroom contains 'kindergarten'" %}
{% for page in lesson_kindergarten_pages %}
- [{{ page.title }}]({{ page.url  | absolute_url }})
{{page.description }}
{% endfor %}


### Grades 1-3
{% assign lesson_grades1_3_pages = site.pages | where: "lesson",  { page.lesson } | where_exp: "item", "item.classroom contains 'grades1_3'" %}
{% for page in lesson_grades1_3_pages %}
- [{{ page.title }}]({{ page.url  | absolute_url }})
{{page.description }}
{% endfor %}


### Grades 4-6
{% assign lesson_grades4_6_pages = site.pages | where: "lesson", { page.lesson } | where_exp: "item", "item.classroom contains 'grades4_6'" %}
{% for page in lesson_grades4_6_pages %}
- [{{ page.title }}]({{ page.url  | absolute_url }})
{{page.description }}
{% endfor %}

---

### How to Use

1. **Navigate to the Lesson Plan**: Click on the link for the desired grade level to access the lesson plan.
2. **Review Materials**: Each lesson plan includes an overview, objectives, materials needed, lesson steps, Catholic integration, assessment methods, and closing prayer.
3. **Engage with Parent Resources**: At the end of each lesson, there are resources for parents to support their child's learning at home.

---

**Note:** These lesson plans are part of an ongoing effort to enrich STEM education with ethical and spiritual dimensions, preparing students to use technology for the common good.

