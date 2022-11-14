#Begin Portion 1#
import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        self.connections.update({connection_id: connection_load})
        # Add the connection to the dictionary with the calculated load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        self.connections.pop(connection_id)

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        for connection in self.connections.values():
            total += connection
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())
    
#End Portion 1#

server = Server()
server.add_connection("192.168.1.1")

print(server.load())

server.close_connection("192.168.1.1")
print(server.load())

#Begin Portion 2#
class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]
    
    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        if self.avg_load() > 50:
            #print("Average Load is: " + str(self.avg_load()))
            self.ensure_availability()
        server = random.choice(self.servers)
        # Add the connection to the dictionary with the selected server
        self.connections.update({connection_id: server})
        # Add the connection to the server
        server.add_connection(connection_id)
        #print(self.servers)
        #print(self.connections)

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        for server in self.servers:
            if connection_id in server.connections:
        # Close the connection on the server
                #server.connections.pop( connection_id )
                self.servers.remove(server)
        # Remove the connection from the load balancer
        if connection_id in self.connections:
            self.connections.pop(connection_id)
        #print("Currently added servers:" + str(self.servers))

    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        sum_loads = 0
        total_servers = len(self.servers)
        for server in self.servers:
            sum_loads += server.load()
        if total_servers > 0:    
            return sum_loads / total_servers
        else:
            return 0

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        self.servers.append(Server())
        

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))
#End Portion 2#

l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())

l.servers.append(Server())
print(l.avg_load())

l.close_connection("fdca:83d2::f20d")
print(l.avg_load())

for connection in range(20):
    l.add_connection(connection)
print(l)

print(l.avg_load())


