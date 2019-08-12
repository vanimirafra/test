from find_path import*
from add_route import*
from delete_route import*
import yaml
with open("/home/mirafra/Documents/Graph/graph.yml", 'r') as stream:
    G = yaml.safe_load(stream)
length=len(G)
source=input("enter the source")
destination=input("enter the destination")
#flight_no=int(input("enter flight number"))

print(delete_flight(G, source, destination))
print(G)



