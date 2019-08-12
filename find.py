class Graph:

    def __init__(self):
        data = {
            'chicago': {'boston': 702, 'miami': 708},
            'philadelphia': {'boston': 712, 'chicago': 705, 'miami': 717, 'atlanta': 713},
            'boston': {'chicago': 701, 'philadelphia': 711},
            'miami': {'philadelphia': 718},
            'atlanta': {'miami': 715},

        }
        self.data = data
        self.V = data.keys()


    def find_path(self, data, source, destination, path=[]):
        path = path + [source]
        if source == destination:
            return [path]
        paths = []
        for node in data[source]:
            if node not in path:
                newpaths = self.find_path(data, node, destination, path)
                for newpath in newpaths:
                    paths.append(newpath)

        return paths


    def find_route(self,source, destination):
        return self.find_path(self.data, source, destination)
g=Graph()

