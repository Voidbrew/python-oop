import time

class Singleton:
    def __new__(cls):
        if hasattr(cls,'instance'):
            return cls.instance
            
        cls.instance = super(Singleton,cls).__new__(cls)
        cls.printable = 0

    def print(self):
        return print(self.printable)

start_time = time.time()

Singleton()
for i in range(10000000):
    Singleton.printable = i
Singleton().print()

print(time.time()-start_time)
