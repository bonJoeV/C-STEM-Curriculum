---
layout: default
title: "Page List"
---
{% for page in site.pages %}
  {% if page.classrooms contains 'grades4-6' %}
    <div class="item">
      <h3>{{ page.title | escape: false | strip_html }}</h3>
      <p>{{ page.description | escape: false | strip_html }}</p>
    </div>
  {% endif %}
{% endfor %}
