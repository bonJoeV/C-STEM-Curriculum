---
layout: default
title: "Page List"
---

{% for page in site.pages %}
  {% if page.categories contains 'grades4_6' %}
    <div class="item">
      <h3>{{page.title}}</h3>
      <p>{{page.description}}</p>
    </div>
  {% endif %}
{% endfor %}

---

{% for p in site.pages %}
   {% if p.categories contains 'grades4_6' %}
     * [{{ p.title }}]({{ p.url | absolute_url }})
        <small>{{ p.excerpt }}</small>
   {% endif %}
{% endfor %}


{% for page in site.pages %}
  {% if page.classrooms contains 'grades4-6' %}
    <div class="item">
      <h3>{{ page.title | escape: false }}</h3>
      <p>{{ page.description | escape: false }}</p>
    </div>
  {% endif %}
{% endfor %}
