---
layout: default
title: "Introduction to Coding with Scratch Jr & Scratch"
classroom: []
lesson: "Exploring_Gods_Creation_Scratch"
curriculam: "yes"
author: "Joe Vandermark"
published: "31 Oct 2024"
---

### C-STEM Coding Curriculum Overview

Our **C-STEM Coding Curriculum** introduces elementary students to foundational coding and engineering concepts through engaging, faith-integrated activities. Using tools like **Scratch Jr** and **Scratch**, students explore programming principles by creating interactive stories, animations, and games. Each lesson emphasizes problem-solving, creativity, and ethical reflections, aligning technology education with Catholic values of stewardship, community, and service. This curriculum supports Kindergarten through 6th grade, fostering skills that prepare students for future STEM learning in a meaningful, value-centered environment.

For an introduction to coding with **Scratch Jr** and **Scratch**, explore our [Overview of Scratch Jr and Scratch](./about_scratch.md). This guide covers their unique features, educational benefits, and classroom applications, offering a foundation for engaging students in coding through storytelling, games, and animations.

<!-- No need to change below, this is a template for all projects. -->

## Lesson Plans

### Kindergarten
{% assign lesson_kindergarten_pages = site.pages | where: "lesson", page.lesson | where_exp: "item", "item.classroom contains 'kindergarten'" %}
{% for page in lesson_kindergarten_pages %}
- [{{ page.title }}]({{ page.url  | absolute_url }})
{{page.description }}
{% endfor %}


### Grades 1-3
{% assign lesson_grades1_3_pages = site.pages | where: "lesson",  page.lesson | where_exp: "item", "item.classroom contains 'grades1_3'" %}
{% for page in lesson_grades1_3_pages %}
- [{{ page.title }}]({{ page.url  | absolute_url }})
{{page.description }}
{% endfor %}


### Grades 4-6
{% assign lesson_grades4_6_pages = site.pages | where: "lesson", page.lesson | where_exp: "item", "item.classroom contains 'grades4_6'" %}
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

