import csv
from typing import List

from langchain.graphs.networkx_graph import KnowledgeTriple
from langchain.llms import OpenAI
from langchain.indexes import GraphIndexCreator
from langchain.chains import GraphQAChain


def load_triples(filename: str) -> List:
    """
    Loads CSV file contents into a list of tuples

    :param filename: The name of the CSV file
    :return: A list of tuples
    """
    new_triples = []
    with open(filename) as triples_file:
        reader = csv.reader(triples_file)
        for i, line in enumerate(reader):
            print(line)
            print(line)
            new_triples.append((line[0], line[1], line[2]))
    return new_triples


triples = []
files = ["expert-expertise.csv", "expert-locations.csv"]
for file in files:
    triples += load_triples(file)

index_creator = GraphIndexCreator(llm=OpenAI(temperature=0))
graph = index_creator.from_text('')
graph.get_triples()

graph = index_creator.from_text('')
for (node1, relation, node2) in triples:
    graph.add_triple(KnowledgeTriple(node1, relation, node2))

question = "Where is D. Keellings located in?"
print(f"Answering Question: {question}")
chain = GraphQAChain.from_llm(OpenAI(temperature=0), graph=graph, verbose=True)
print(chain.run(question))
