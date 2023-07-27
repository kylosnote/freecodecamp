import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs):
        self.list = kwargs
        self.contents = [[k]*v for (k,v) in kwargs.items()]
        self.contents = [item for sublist in self.contents for item in sublist]  # hmmm

    def draw(self, number):
        if number > len(self.contents):
            return self.contents
        drawn_list = []
        for i in range(number):

            drawn_color = self.contents.pop(random.randrange(len(self.contents)))
            drawn_list.append(drawn_color)
            self.list[drawn_color] = self.list[drawn_color]-1

        return drawn_list

    def __str__(self):
        return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    win = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        draw_result = hat_copy.draw(num_balls_drawn)
        count = 0
        for (color, appear_time) in expected_balls.items():
            if draw_result.count(color) >= appear_time:
                count += 1
            if count == len(expected_balls):
                win += 1

    return win/num_experiments