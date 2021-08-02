from py2neo import Graph
import pandas as pd
graph = Graph("http://localhost:7474", auth=("neo4j", "Winfo_123"))
name1="Alice"
df=graph.run("MATCH (a:Person) RETURN a.name").to_data_frame()
print(df)