# weaviate_ontology_visualization
Uses PyGraphviz to visualize a Weaviate schema (ontology)

## How to use:

Paste your ontology schemas in the folders `weaviate_data`: `things` and `actions`, with the filenames `schema.json` in each folder.

_Note: only test it with Python3_


Generate visualization:
`$ python viz_schemas.py  | dot -Tpdf > schema.pdf`

For Windows systems:
`$ python viz_schemas.py > viz_code.txt`
The code generated and written to viz_code.txt can be copied to https://dreampuf.github.io/GraphvizOnline/ to view the graph.
