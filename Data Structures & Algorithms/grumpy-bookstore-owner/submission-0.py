class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        # Count unsatisfied customers in first window
        sum = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                sum += customers[i]

        l = 0
        res = sum
        max_l = l
        max_r = minutes - 1

        # Find the window that saves the most unsatisfied customers
        for i in range(minutes, len(customers)):

            if grumpy[l] == 1:
                sum -= customers[l]

            if grumpy[i] == 1:
                sum += customers[i]

            if sum > res:
                res = sum
                max_l = l + 1
                max_r = i

            l += 1

        satisfied = 0

        # Count customers that will be satisfied
        for i in range(len(customers)):

            # Technique is active
            if i >= max_l and i <= max_r:
                satisfied += customers[i]

            # Outside technique, owner must naturally not be grumpy
            elif grumpy[i] == 0:
                satisfied += customers[i]

        return satisfied




        