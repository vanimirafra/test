'''import yaml
with open("/home/mirafra/Documents/Graph/graph.yml", 'r') as stream:
    G = yaml.safe_load(stream)

source=input("enter the source")
destination=input("enter the destination")
flight_no=int(input("enter flight number"))

def add_flight(G, source, destination, flight_no):
    return G[source].update({destination: flight_no})


add_flight(G, source, destination, flight_no)
print(G)'''


