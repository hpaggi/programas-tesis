import asyncio
import aiomas

class TestAgent(aiomas.Agent):
     def __init__(self, container, name):
         super().__init__(container, name)
         print('Ohai, I am %s' % name)

     @asyncio.coroutine
     def run(self, addr):
         """The agent's "main" function."""
         remote_agent = yield from self.container.connect(addr)
         ret = yield from remote_agent.service(42)
         print('%s got %s from %s' % (self.name, ret, addr))

     @aiomas.expose
     def service(self, value):
         """Exposed function that can be called by remote agents."""
         return value

# A Container is the home for a number of agents.
c = aiomas.Container(('localhost', 5555))
agents = [c.spawn(TestAgent) for i in range(2)]



# Run agent 0 and let it call a method from agent 1
loop = asyncio.get_event_loop()
loop.run_until_complete(agents[0].run('agent://localhost:5555/1'))
#agent://localhost:5555/0 got 42 from agent://localhost:5555/1

c.shutdown()