import yaml
with open("/home/mirafra/Documents/Graph/graph.yml", 'r') as stream:
    G = yaml.safe_load(stream)
length=len(G)
source=input("enter the source")
destination=input("enter the destination")


def find_path(G, source, destination,length ):
    path = [source]
    list = [iter(G[source])]
    while  list:
        newpath =  list[-1]
        paths = next( newpath , None)
        if paths is None:
            list.pop()
            path.pop()
        elif len(path) < length:
            if paths == destination:
                yield path + [destination]
            elif paths not in path:
                path.append(paths)
                list.append(iter(G[paths]))
        else:
            pass

route= find_path(G, source, destination,length )
for i in route:
    print(i)






