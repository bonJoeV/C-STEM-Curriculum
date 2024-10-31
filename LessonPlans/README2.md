{% for page in site.pages %}
  {% if page.categories contains 'grades4_6' %}
    <div class="item">
      <h3>{{page.title}}</h3>
      <p>{{page.description}}</p>
    </div>
  {% endif %}
{% endfor %}
