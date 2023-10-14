import logging
import requests
import urllib.parse

prefix = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX kwgr: <http://stko-kwg.geog.ucsb.edu/lod/resource/>
PREFIX kwg-ont: <http://stko-kwg.geog.ucsb.edu/lod/ontology/>
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX iospress: <http://ld.iospress.nl/rdf/ontology/>
"""


def fetch_query_results(query: str, filename: str) -> None:
    """
    Runs a SPARQL query and saves the results in CSV

    :param query:
    :param filename: The name ofthe file to write  results to
    :return: None
    """
    query = urllib.parse.quote_plus(query)
    resp = requests.get(
        f"https://stko-kwg.geog.ucsb.edu/graphdb/repositories/KWG-V2-Vienna?query={query}&Accept=text/csv"
    ).text
    with open(filename, "w+") as out_file:
        out_file.write(resp)


def get_expert_expertise() -> None:
    """
    Retrieves all the experts and their expertise and writes them to disk.

    :return: None
    """
    logging.info("Downloading Expertise Data...")
    query = f"""
            {prefix}
            SELECT ?expert_name ?predicate ?expertiseLabel
                WHERE {{
                ?entity rdf:type iospress:Contributor.
                ?entity rdfs:label ?expert_name.
                ?entity kwg-ont:hasExpertise ?expertise.
                ?expertise rdfs:label ?expertiseLabel.
                BIND ("is an expert in" as ?predicate)
            }}
            """
    fetch_query_results(query, "expert-expertise.csv")
    logging.info("Finished Downloading Expertise Data")


def get_expert_location() -> None:
    """
    Retrieve the location of each expert and write to disk

    :return: None
    """
    query = f"""{prefix}
            SELECT ?expert_name ?predicate ?location_name
            WHERE {{
                ?entity rdf:type iospress:Contributor.
                ?entity rdfs:label ?expert_name.
                ?entity iospress:contributorAffiliation ?affiliation.
                ?affiliation kwg-ont:sfWithin ?affiliationLoc .
                ?affiliationLoc kwg-ont:quantifiedName ?location_name
                BIND("is located in" as ?predicate)
            }}
            """
    logging.info("Downloading Expertise Location Data")
    fetch_query_results(query, "expert-locations.csv")
    logging.info("Finished Downloading Expertise Location Data")


get_expert_expertise()
get_expert_location()
