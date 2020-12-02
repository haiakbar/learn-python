import random
import copy

class Hat:
    
    def __init__(self, **data):
        self.contents = []
        
        for key, value in data.items():
            for i in range(value):
                self.contents.append(key)
    
    def draw(self, num_to_draw):
        
        #copy_contents = copy.copy(self.contents)
        drawed_balls = []
        
        if num_to_draw >= len(self.contents):
            contents_copy = copy.copy(self.contents)
            self.contents.clear()
            return contents_copy
        
        for i in range(num_to_draw):
            #removed = random.choice(copy_contents)
            removed = random.choice(self.contents)
            #copy_contents.remove(removed)
            self.contents.remove(removed)
            drawed_balls.append(removed)
        
        return drawed_balls

def match(expected_balls, expected_dict, drawn):
    
    for item in expected_balls:
        source_count = drawn.count(item)
        if expected_dict[item] > source_count:
            return False
    return True

def experiment(**data):
    hat = data['hat']
    expected = data['expected_balls']
    balls_drawn = data['num_balls_drawn']
    num_experiments = data['num_experiments']
    
    num_success = 0
    expected_balls = []
    
    for item in expected.keys():
        expected_balls.append(item)
    
    for i in range(num_experiments):
        drawn = hat.draw(balls_drawn)
        
        for balls in drawn:
            hat.contents.append(balls)
        
        if match(expected_balls, expected, drawn):
            num_success += 1
    
    return num_success/num_experiments