import math
from collections import Counter


class Stat:
    def __init__(self, num_list: list):
        self.num_list = num_list

    def count(self):
        return len(self.num_list)

    def sum(self):
        return sum(self.num_list)

    def get_min(self):
        return min(self.num_list)

    def get_max(self):
        return max(self.num_list)

    def range(self):
        return self.get_max() - self.get_min()

    def mean(self):
        return self.sum() / self.count()

    def median(self):
        sorted(self.num_list)
        return self.num_list[int(self.count() / 2)] if self.count() % 2 != 0 else (
                sum(self.num_list[int(self.count() / 2) - 1], self.num_list[int(self.count() / 2)]) / 2)

    def mode(self):
        return Counter(self.num_list).most_common(1)

    def variance(self, type='population'):
        if type == "sample":
            var = sum((x - self.mean()) ** 2 for x in self.num_list) / self.count() - 1
        else:
            var = sum((x - self.mean()) ** 2 for x in self.num_list) / self.count()
        return var

    def std_dev(self, type='population'):
        return math.sqrt(self.variance(type))

    def freq_dist(self):
        counter = sorted(Counter(self.num_list).items(), key=lambda x: x[1], reverse=True)
        return [(int(elm[1]) * 4.0, elm[0]) for elm in counter]
