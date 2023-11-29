import sys
class Autobus:
    def __init__(self, number, start, end, time):
        self.start = start
        self.end = end
        self.number = number
        self.time = time

    def info(self):
        return "Route number: {}\nStarting point: {}\nDestination point: {}\nTravel time: {}\n-----------------------------\n".format(self.number, self.start, self.end,  self.time)
    
    def set_number(self, value):
        self.number = value

    def get_number(self):
        return self.number

    def set_start(self, value):
        self.start = value

    def get_start(self):
        return self.start
    
    def set_end(self, value):
        self.end = value

    def get_end(self):
        return self.end
    
    def set_time(self, value):
        self.time = value

    def get_time(self):
        return self.time
    
def create_autopark():
    n = int(input('Enter the number of buses: '))
    buses = []
    for i in range(n):
        num = int(input(f'Enter bus #{i+1} number: '))
        start = input(f'Enter the starting point of bus #{i+1}: ')
        end = input(f'Enter the destination point of bus #{i+1}: ')
        time = input(f'Enter the travel time of bus #{i+1}: ')
        print('-----------------------------')
        buses.append(Autobus(num, start, end, time))

    with open('buses.txt', 'w') as file:
        for i in range(len(buses)):
            file.write(str(buses[i].info()))

def read_file():
    buses = []
    with open("buses.txt") as file:
        lines = file.readlines()
        words = []
        i = 4
        while i <= len(lines):
            lines.pop(i)
            i+=4

        for line in lines:
            words.append(line.replace('\n', '').split(sep=' ')[-1])

        while len(words) >= 4:
            buses.append(Autobus(int(words[0]), words[1], words[2], words[3]))
            for i in range(4):
                words.pop(0)

        return buses
    
def show_autopark(buses):
    for bus in buses:
        print(bus.info())

def sort_by_number(buses):
    park = {}
    for bus in buses:
        park.update({bus.get_number():bus})

    new_park = {k: v for k, v in sorted(park.items(), key=lambda item: item[0], reverse=True)}
    for key in new_park.keys():
        print(new_park[key].info())

def search_by_point(city:str, buses):
    for bus in buses:
        if bus.get_start() == city or bus.get_end() == city:
            print(bus.info())

# create_autopark()
autopark = read_file()
show_autopark(autopark)
sort_by_number(autopark)
search_by_point('Pinsk', autopark)