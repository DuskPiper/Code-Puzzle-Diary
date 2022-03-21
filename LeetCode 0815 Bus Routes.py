class Solution: # 45, 29
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stopToRoute = dict() # Stop->RoutesAtThisStop
        for route, stops in enumerate(routes):
            for stop in stops:
                if stop not in stopToRoute:
                    stopToRoute[stop] = set()
                stopToRoute[stop].add(route)
                
        # BFS
        visitedRoute = set()
        visitedStop = set()
        counter = 0
        q = set([source])
        while q:
            nextRound = set()
            for stop in q: # curStop
                if stop == target:
                    return counter
                if stop in visitedStop:
                    continue
                visitedStop.add(stop)
                for route in stopToRoute.get(stop, []): # Find all unvisited routes at stop, and all nextStops the routes lead to
                    if route in visitedRoute:
                        continue
                    visitedRoute.add(route) 
                    nextRound.update(routes[route]) # Find all nextStops the route leads to
            q = nextRound
            counter += 1
        return -1
            
                