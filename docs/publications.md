# Publications

(For a full list, see [Publons](https://publons.com/researcher/2243867/alexandra-palacio-morales/))


{% set pub_years = publications_by_year() %}

{% for year, pubs in pub_years.items() %}
### {{ year }}
{% for pub in pubs %}
- **{{ pub.title }}**  
  <em>{{ pub.authors }}</em>  
  [{{ pub.link.display }}]({{ pub.link.url }})
{% endfor %}
{% endfor %}