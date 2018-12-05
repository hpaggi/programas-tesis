import asyncio
import aiomas
class Callee(aiomas.Agent):
    # This agent does not need to override "__init__()".
    
    # "expose"d methods can be called by other agents:
    @aiomas.expose
    def spam(self, times):
        """Return a lot of spam."""
        return 'spam' * times


class Caller(aiomas.Agent):

    async def run(self, callee_addr):
        print(self, 'connecting to', callee_addr)
        # Ask the container to make a connection to the other agent:
        callee = await self.container.connect(callee_addr)
        print(self, 'connected to', callee)
        # "callee" is a proxy to the other agent.  It allows us to call
        # the exposed methods:
        result = await callee.spam(10)
        print(self, 'got', result)


container = aiomas.Container.create(('localhost', 5555))
callee = Callee(container)
caller = Caller(container)
aiomas.run(until=caller.run(callee.addr))

container.shutdown()