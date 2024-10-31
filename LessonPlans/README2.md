---
layout: default
title: "Page List"
---
{% for page in site.pages %}
  {% if page.categories contains 'grades4-6' %}
    <div class="item">
      <h3>{{page.title}}</h3>
      <p>{{page.description}}</p>
    </div>
  {% endif %}
{% endfor %}