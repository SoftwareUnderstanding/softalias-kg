from SPARQLWrapper import SPARQLWrapper, TURTLE

# Set up the SPARQL endpoint
endpoint_url = "https://query.wikidata.org/sparql"
sparql = SPARQLWrapper(endpoint_url)

# Construct the SPARQL query
query_metadata = """
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

CONSTRUCT {
  ?software a <https://schema.org/SoftwareApplication> ;
    <https://schema.org/name> ?label ;
    <https://w3id.org/softalias/alias> ?labelURI;
    <https://schema.org/provider> "Wikidata" ;
    <https://schema.org/description> ?desc ;
    <https://schema.org/url> ?repo ;
    <https://schema.org/url> ?url2 ;
    <https://schema.org/url> ?url .
    
   ?labelURI a <https://w3id.org/softalias/SoftwareAlias>;
          <https://schema.org/name> ?label .
  
} WHERE {
  ?software wdt:P31/wdt:P279* wd:Q341;
           
           rdfs:label ?label .
 filter (lang(?label) = "en")
 
  OPTIONAL {?software wdt:P1324 ?repo}.
  OPTIONAL {?software wdt:P2699 ?url2}.
  OPTIONAL {?software wdt:P856 ?url}.
  OPTIONAL {?software schema:description ?desc.
            filter(lang(?desc) = "en")}
            
  BIND(URI(CONCAT("https://w3id.org/softalias/alias/", ENCODE_FOR_URI(?label))) AS ?labelURI)
  
}
"""

#"""
#OPTIONAL {?software skos:altLabel ?c  
#           filter (lang(?c) = "en")}.
#"""

sparql.setQuery(query_metadata)
sparql.setReturnFormat(TURTLE)

results = sparql.queryAndConvert()
#print(results.serialize())
filename = "metadata.ttl"
with open(filename, "w", encoding="utf-8") as file:
    file.write(results.serialize())
    
query_alias = """
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

CONSTRUCT {
  ?aliasURI a <https://w3id.org/softalias/SoftwareAlias>;
          <https://schema.org/name> ?alias .
} WHERE {
  ?software wdt:P31/wdt:P279* wd:Q341;
           rdfs:label ?label .
 filter (lang(?label) = "en")
 
 ?software skos:altLabel ?alias .
 filter (lang(?alias) = "en") 
           
 BIND(URI(CONCAT("https://w3id.org/softalias/alias/", ENCODE_FOR_URI(?alias))) AS ?aliasURI)
}
"""
#

sparql.setQuery(query_alias)
sparql.setReturnFormat(TURTLE)

results = sparql.queryAndConvert()
#print(results.serialize())
filename = "alias_labels.ttl"
with open(filename, "w", encoding="utf-8") as file:
    file.write(results.serialize())
    
# For some reason the construct query returns incomplete results if not separated.

query_alias2 = """
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

CONSTRUCT {
  ?software a <https://schema.org/SoftwareApplication> ;
    <https://w3id.org/softalias/alias> ?aliasURI. 
  
} WHERE {
  ?software wdt:P31/wdt:P279* wd:Q341;
           rdfs:label ?label .
 filter (lang(?label) = "en")
 
 ?software skos:altLabel ?alias .
 filter (lang(?alias) = "en") 
           
 BIND(URI(CONCAT("https://w3id.org/softalias/alias/", ENCODE_FOR_URI(?alias))) AS ?aliasURI)
}
"""

sparql.setQuery(query_alias2)
sparql.setReturnFormat(TURTLE)

results = sparql.queryAndConvert()
#print(results.serialize())
filename = "alias.ttl"
with open(filename, "w", encoding="utf-8") as file:
    file.write(results.serialize())

