#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    # Don't need this definition
    # route = [None] * length 

    # Add trips to hashtable, when I see the starting location, create the route and add that location as the first item in the list
    for ticket in tickets:
        if ticket.source == "NONE":
            route = [ticket.destination] 
        hash_table_insert(hashtable, ticket.source, ticket)

    # Keep adding locations to the route until I get to a route with a destination of 'NONE'
    while route[-1] != "NONE":
        next_step = hash_table_retrieve(hashtable, route[-1])
        route.append(next_step.destination)
        if route[-1] == "NONE":
            break

    return route
