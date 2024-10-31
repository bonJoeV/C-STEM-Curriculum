{% for page in site.pages %}
  {% if page.categories contains 'grades4_6' %}
    <div class="item">
      <h3>{{page.title}}</h3>
      <p>{{page.description}}</p>
    </div>
  {% endif %}
{% endfor %}



{% for p in site.pages %}
   {% if p.categories contains 'grades4_6' %}
     * [{{ p.title }}]({{ p.url | absolute_url }})
        <small>{{ p.excerpt }}</small>
   {% endif %}
{% endfor %}