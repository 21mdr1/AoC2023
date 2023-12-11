# parse input
# probably hold them in a list? or maybe a class, because why not

# history class
# contains history content
# has substracting function
# keeps last number of each line
# has predict next number function

class History:
    def __init__(self, f):
        self.report = f
        self.next_value = None
        self.last_values = []
    
    def get_next_step(self, last_step):
        next_step = []
        for i in range(0, len(last_step)-1):
            next_step.append(last_step[i+1] - last_step[i])
        return next_step
    
    def predict_next_number(self, line):
        last_step = line
        self.last_values = [last_step[-1]]
        while not(sorted(last_step)[0] == sorted(last_step)[-1] == 0):
            last_step = self.get_next_step(last_step)
            self.last_values.append(last_step[-1])

        prediction = None
        for i in range(len(self.last_values)-1, 0, -1):
            if prediction is None:
                prediction = self.last_values[i] + self.last_values[i-1]
            else: 
                prediction+= self.last_values[i-1]
        return prediction
    
    def predict_first_number(self, line):
        last_step = line
        self.last_values = [last_step[0]]
        while not(sorted(last_step)[0] == sorted(last_step)[-1] == 0):
            last_step = self.get_next_step(last_step)
            self.last_values.append(last_step[0])

        prediction = None
        for i in range(len(self.last_values)-1, 0, -1):
            if prediction is None:
                prediction = self.last_values[i-1] - self.last_values[i]
            else: 
                prediction = self.last_values[i-1] - prediction
        return prediction
    
    def sumOfPredictions(self):
        predictions = [self.predict_next_number(line) for line in self.report]
        return sum(predictions)
    
    def sumOfPrePredictions(self):
        predictions = [self.predict_first_number(line) for line in self.report]
        return sum(predictions)


f = [list(map(int, line.strip().split(' '))) for line in open("../input/input_9.txt").readlines()]

history = History(f)

print(history.sumOfPrePredictions())