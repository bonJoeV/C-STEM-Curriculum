{% for page in site.pages %}
  {% if page.classrooms contains 'grades4-6' %}
    <div class="item">
      <h3>{{ page.title | escape: false }}</h3>
      <p>{{ page.description | escape: false }}</p>
    </div>
  {% endif %}
{% endfor %}
