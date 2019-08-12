import yaml
with open("/home/mirafra/Documents/Graph/graph.yml", 'r') as stream:
    G = yaml.safe_load(stream)
source=input("enter the source")
destination=input("enter the destination")


def delete_flight(G, source, destination):
    flight_no = G[source].get(destination)
    G[source].pop(destination)
    return 'Flight ' + str(flight_no) + ' from ' + source + ' to ' + destination + ' deleted  successfully'

print(G)
print(delete_flight(G, source, destination))
print(G)


