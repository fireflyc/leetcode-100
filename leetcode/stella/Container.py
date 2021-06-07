
from typing import List


def count_triplets(nums: List[int]) -> int:
    tuples = {}
    for m in nums:
        for n in nums:
            nm = n & m
            tuples[nm] = tuples.get(nm) or 0
            tuples[nm] += 1
    count = 0
    for n in nums:
        for k in tuples:
            if n & k == 0:
                count += tuples[k]
    return count


class UndergroundSystem:

    def __init__(self):
        self.user_check_in = {}
        self.routes = {}
        pass

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.user_check_in[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        source, enter_time = self.user_check_in[id][0], self.user_check_in[id][1]
        self.routes[source] = self.routes.get(source) or {}
        self.routes[source][stationName] = self.routes[source].get(stationName) or []
        self.routes[source][stationName].append(t-enter_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if startStation in self.routes and endStation in self.routes[startStation]:
            all_times = self.routes[startStation][endStation]
            return sum(all_times)/len(all_times)


def design_underground_system(operators: [], operands: []):
    metro, output = None, []
    for i, operator in enumerate(operators):
        operand = operands[i]
        if operator in ['UndergroundSystem']:
            metro = UndergroundSystem()
            output.append(None)
        elif operator in ['checkIn']:
            output.append(metro.checkIn(*operand))
        elif operator in ['checkOut']:
            output.append(metro.checkOut(*operand))
        elif operator in ['getAverageTime']:
            output.append(metro.getAverageTime(*operand))
    return output
