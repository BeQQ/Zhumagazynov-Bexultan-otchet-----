class NetworkSimulator:
    def __init__(self, devices):
        self.devices = devices
        self.tasks_queue = []

    def add_task(self, task):
        self.tasks_queue.append(task)

    def round_robin_scheduler(self):
        while self.tasks_queue:
            for device in self.devices:
                if self.tasks_queue:
                    task = self.tasks_queue.pop(0)
                    device.process_task(task)
                else:
                    break

class Device:
    def __init__(self, name):
        self.name = name

    def process_task(self, task):
        print(f"Device {self.name} is processing task: {task}")


device1 = Device("Router1")
device2 = Device("Switch1")
device3 = Device("Server1")

network_simulator = NetworkSimulator([device1, device2, device3])

tasks = ["Data1", "Data2", "Data3", "Data4"]

for task in tasks:
    network_simulator.add_task(task)

network_simulator.round_robin_scheduler()


servers = ["server1", "server2", "server3"]
current_server = 0

def round_robin():
   global current_server
   server = servers[current_server]
   current_server = (current_server + 1) % len(servers)
   return server


for _ in range(10):
   selected_server = round_robin()
   print("Запрос направлен на сервер:", selected_server)

