# to view the generated graph: paste outcome to https://dreampuf.github.io/GraphvizOnline/

import weaviate_data

dbs = weaviate_data.load()

SKIP_DATATYPES=["string", "int", "number", "boolean", "date", "geoCoordinates"]

print("digraph  G {")
print(" node[shape=none];")

for db_name in dbs:
    db = dbs[db_name]
    cluster_name = "cluster_" + db_name.replace(" ","_")
    print()
    print("subgraph",  cluster_name, "{")
    print("  node [style=filled];")
    print('  label = "{}";'.format(db_name))

    def graphviz_class_name(class_name):
       return cluster_name + class_name

    for klass in db.schema.classes:
        label_html = "<table border='1' cellborder='1'>"
        label_html += "<tr><td colspan='2' bgcolor='green'><b>{}</b></td></tr>".format(klass.class_name)
        label_rel = []
        for prop in klass.properties:
            label_html+= "<tr><td>{}</td><td port='{}'>{}</td></tr>".format(prop.name, prop.name, " or ".join(prop.datatype))
            for datatype in prop.datatype:
                if datatype not in SKIP_DATATYPES:
                    label_rel.append("  {}:{} -> {};".format(graphviz_class_name(klass.class_name), prop.name, graphviz_class_name(datatype)))
        label_html += "</table>"
        print('  {} [label=<{}>];'.format(graphviz_class_name(klass.class_name), label_html))
        print("\n".join(label_rel))

    print("}")
    print()

print("}")