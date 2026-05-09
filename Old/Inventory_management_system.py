class Resource:
    def __init__(self,name,manufacturer, total, allocated):
        self._name = name
        self._manufacturer = manufacturer
        self._total = total
        self._allocated = allocated

    @property
    def name(self):
        return self._name

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def total(self):
        return self._total

    @property
    def allocated(self):
        return self._allocated

    def __str__(self):
        return self.name

    @property
    def category(self):
        return type(self).__name__.lower()

    def __repr__(self):
        return f"Name - {self.name}\nCategory - {self.category}\nManufacturer-{self.manufacturer}\nTotal-{self.total}\nAllocated-{self.allocated}"

    @property
    def available(self):
        return self.total - self.allocated

    def claim(self,n):
        if self.available >= n:
            self._allocated += n
        else:
            print(f"Cannot claim more than {self.available}")

    def free_up(self,n):
        if self.allocated >= n:
            self._allocated -= n
        else:
            print("Cannot free-up more than allocated")

    def died(self,n):
        if self.allocated >= n and self.total >= n:
            self._allocated -=n
            self._total -=n
        else:
            print("Everything is fine and all cpu's are running!")

    def purchased(self,n):
        self._total += n
        print(f"The total cost of the cpu's are {n*20000}")

class CPU(Resource):
    def __init__(self, name, manufacturer, total, allocated,cores,sockets,power_watts):
        super().__init__(name, manufacturer, total, allocated)
        self._cores = cores
        self._power_watts = power_watts
        self._sockets = sockets

    @property
    def cores(self):
        return self._cores

    @property
    def power_watts(self):
        return self._power_watts

    @property
    def sockets(self):
        return self._sockets

    def __repr__(self):
        return f"Sockets-{self.sockets}\nPower Watts - {self.power_watts}\nCores-{self.cores}\nCategory-{self.category}"

class Storage(Resource):
    def __init__(self, name, manufacturer, total, allocated,capacity_gb):
        super().__init__(name, manufacturer, total, allocated)
        self._capacity_gb = capacity_gb

    @property
    def capacity_gb(self):
        return self._capacity_gb

    def __repr__(self):
        return f"Capacity GB - {self.capacity_gb} and Category - {self.category}"

class HDD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_gb,size,rpm):
        super().__init__(name, manufacturer, total, allocated, capacity_gb)
        self._size = size
        self._rpm = rpm

    @property
    def size(self):
        return self._size

    @property
    def rpm(self):
        return self._rpm

    def __repr__(self):
        return f"Rpm - {self.rpm}, Size - {self.size} and Category - {self.category}"

class SSD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_gb,interface):
        super().__init__(name, manufacturer, total, allocated, capacity_gb)
        self._interface = interface

    @property
    def interface(self):
        return self._interface

    def __repr__(self):
        return f"Interface - {self.interface} and Category - {self.category}"

newest_cpu = CPU("Intel Core 7 Processor", "Intel",100, 50, 10, "AM4",100000)
newest_cpu.claim(20)
print(newest_cpu.allocated)
print(repr(newest_cpu))
newest_cpu.free_up(69)
print(newest_cpu.allocated)
newest_cpu.purchased(1000)
print(newest_cpu.total)

