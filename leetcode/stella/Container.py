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
        self.routes[source][stationName].append(t - enter_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if startStation in self.routes and endStation in self.routes[startStation]:
            all_times = self.routes[startStation][endStation]
            return sum(all_times) / len(all_times)


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


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = []
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted
        by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        feeds = []
        users = (self.follows.get(userId) or set()) | {userId}
        for idx in range(1, len(self.tweets) + 1):
            if len(feeds) >= 10:
                break
            feed = self.tweets[-1 * idx]
            if feed[0] in users:
                feeds.append(feed[1])
        return feeds

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follows[followerId] = self.follows.get(followerId) or set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in (self.follows.get(followerId) or set()):
            self.follows[followerId].remove(followeeId)


def design_tweeter(operators: [], operands: []):
    tweeter, output = None, []
    for i, operator in enumerate(operators):
        operand = operands[i]
        if operator in ["Twitter"]:
            tweeter = Twitter()
            output.append(None)
        elif operator in ['postTweet']:
            output.append(tweeter.postTweet(*operand))
        elif operator in ['getNewsFeed']:
            output.append(tweeter.getNewsFeed(*operand))
        elif operator in ['follow']:
            output.append(tweeter.follow(*operand))
        elif operator in ['unfollow']:
            output.append(tweeter.unfollow(*operand))
    return output


class MinStack:

    def __init__(self):
        self.mins = []
        self.data = []

    def push(self, val: int) -> None:
        self.data.append(val)
        self.mins.append(min(self.mins[-1], val) if self.mins else val)

    def pop(self) -> None:
        if self.data:
            self.data.pop()
            self.mins.pop()

    def top(self) -> int:
        return self.data[-1] if self.data else None

    def getMin(self) -> int:
        return self.mins[-1] if self.mins else None


def min_stack(operators: [], operands: []):
    stack, output = None, []
    for i, operator in enumerate(operators):
        operand = operands[i]
        if operator in ["MinStack"]:
            stack = MinStack()
            output.append(None)
        elif operator in ["push"]:
            output.append(stack.push(*operand))
        elif operator in ["getMin"]:
            output.append(stack.getMin())
        elif operator in ["pop"]:
            output.append(stack.pop())
        elif operator in ["top"]:
            output.append(stack.top())
    return output


def sum_of_subarray_minimums(arr: List[int]) -> int:
    sum_of_minimums, greater_than_dict, less_than_list = 0, {}, []
    for i in range(0, len(arr)):
        sum_of_minimums += arr[i]
        gt_idx = None
        if less_than_list and less_than_list[-1] > arr[i]:
            for j in range(len(less_than_list) - 1, -1, -1):
                if less_than_list[j] > arr[i]:
                    gt_idx = j
                else:
                    break
            sum_of_minimums += sum(less_than_list[:gt_idx])
        else:
            sum_of_minimums += sum(less_than_list)
        if gt_idx is not None:
            greater_than_dict[arr[i]] = greater_than_dict.get(arr[i]) or 0
            greater_than_dict[arr[i]] += len(less_than_list) - gt_idx
            less_than_list = less_than_list[:gt_idx]
        keys = list(greater_than_dict.keys())
        for k in keys:
            if k > arr[i]:
                greater_than_dict[arr[i]] = greater_than_dict.get(arr[i]) or 0
                greater_than_dict[arr[i]] += greater_than_dict[k]
                greater_than_dict.pop(k)
        for k, v in greater_than_dict.items():
            sum_of_minimums += k * v
        if arr[i] in greater_than_dict:
            greater_than_dict[arr[i]] += 1
        else:
            less_than_list.append(arr[i])
    return sum_of_minimums % (10 ** 9 + 7)


def maximum_nesting_depth_of_two_valid_parentheses_string(seq: str) -> List[int]:
    left_stack, queue = [], []
    for s in seq:
        if s == "(":
            if left_stack and left_stack[-1] == "A":
                left_stack.append("B")
                queue.append(1)
            else:
                left_stack.append("A")
                queue.append(0)
        elif s == ")":
            if left_stack.pop() == "A":
                queue.append(0)
            else:
                queue.append(1)
    return queue

