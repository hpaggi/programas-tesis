import aiomas

class HelloWorld(aiomas.Agent):
     def __init__(self, container, name):
         # We must pass a ref. to the container to "aiomas.Agent":
          super().__init__(container)
          self.name = name  # Our agent's name

     async def run(self):
         # This method defines the task that our agent will perform.
         # It's usually called "run()" but you can name it as wou want.
          print(self.name, 'says:')
          clock = self.container.clock
          for i in range(25):
               await clock.sleep(0.1)
               print('Hello, World!')
               
# Containers need to be started via a factory function:
container = aiomas.Container.create(('localhost', 5555))

# Now we can instantiate an agent an start its task:
agent = HelloWorld(container, 'Monty')
aiomas.run(until=agent.run())
container.shutdown()  # Close all connections and shutdown the server