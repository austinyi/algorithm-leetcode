class Logger:
    def __init__(self):
        self.record = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if self.record.get(message, 0) <= timestamp:
            self.record[message] = timestamp + 10
            return True
        return False
        # if message not in self.record:
        #     self.record[message] = timestamp + 10
        #     return True
        # elif message in self.record and self.record[message] <= timestamp:
        #     self.record[message] = timestamp + 10
        #     return True
        # else:
        #     return False


# # Set + Queue
# # https://leetcode.com/problems/logger-rate-limiter/solutions/1535532/three-python-3-solutions-explained
# class Logger:
#     def __init__(self):
#         self.history = set()  # set of past messages younger than 10 timesteps
#         self.queue = list()  # ordered list of messages younger than 10 timesteps

#     def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
#         while self.queue and self.queue[0][0] <= timestamp - 10:
#             self.history.remove(self.queue[0][1])
#             self.queue.pop(0)
#         if message in self.history:
#             return False
#         else:
#             self.history.add(message)
#             self.queue.append((timestamp, message))
#             return True

