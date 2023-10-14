# GPT Augmented KnowWhereGraph

GPT augmented with expert-expertise data from KnowWhereGraph, inspired by work from the one and only [Maxime Labonne](https://github.com/mlabonne).

## Background

[KnowWhereGraph](knowwheregraph.org) is a multi-billion relation knowledge graph that contains information about places, people, and their interactions. This repository retrieves a subset of that information and integrates it into GPT for high level question/answering.

## Running

Running the code first requires [poetry](https://python-poetry.org/docs/).

1. Initialize a new environment with `poetry shell`
2. Fetch the data from KnowWhereGraph with `poetry python3 fetch-data.py`
3. Edit `question` variable with a question about an expert or expertise.
4. Add your OpenAI API key to the environment with `export OPENAI_API_KEY=your_key_here` 
4. Load the data & ask the question with `poetry run main.py`

## Demo

The default question is about the location of a particular expert, `Where is D. Keellings located in?`.

The entities are extracted (about the expert in person) and the associated triples are listed out in the context.

```commandline
Entities Extracted:
 D. Keellings
Full Context:
D. Keellings is an expert in Climate-Related
D. Keellings is an expert in Hurricane
D. Keellings is an expert in Precipitation-Related
D. Keellings is an expert in Rain
D. Keellings is an expert in Rainfall-Related
D. Keellings is an expert in Storm
D. Keellings is an expert in Tropical Cyclone
D. Keellings is an expert in Weather-Related
D. Keellings is an expert in Wind
D. Keellings is an expert in Climate Change
D. Keellings is an expert in Drought
D. Keellings is an expert in Ecology
D. Keellings is an expert in Flood
D. Keellings is an expert in Vulnerable Populations
D. Keellings is an expert in Covid 19
D. Keellings is an expert in Disease
D. Keellings is an expert in Landslide
D. Keellings is an expert in Malaria
D. Keellings is an expert in Population At Risk
D. Keellings is an expert in Public Health
D. Keellings is an expert in Vaccine
D. Keellings is an expert in Earthquake
D. Keellings is an expert in Tornado
D. Keellings is an expert in Extreme Flood
D. Keellings is an expert in Heat Wave
D. Keellings is an expert in Falciparum Malaria
D. Keellings is an expert in Extreme Temperature
D. Keellings is located in Tuscaloosa, Alabama, United States
```

With the chain complete, the full answer is correctly given.
```commandline
> Finished chain.
 D. Keellings is located in Tuscaloosa, Alabama, United States.
```
