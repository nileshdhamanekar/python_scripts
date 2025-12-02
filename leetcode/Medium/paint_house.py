# https://leetcode.com/problems/paint-house/submissions/
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # Approach 1: Works in most cases 
        # Need to be fixed for input:[[3,5,3],[6,17,6],[7,13,18],[9,10,18]]
        # best_cost = dict()
        # for house_index, house in enumerate(costs):
        #     min_cost = next_min_cost = min_index = next_min_index = float('Inf')
        #     for color_index, cost in enumerate(house):
        #         if cost <= min_cost:
        #             min_cost, min_index = cost, color_index
        #         if cost >= min_cost and cost <= next_min_cost and color_index != min_index:
        #             next_min_cost, next_min_index = cost, color_index
        #     if house_index != 0 and best_cost[house_index-1]["min_index"] == min_index:
        #         best_cost[house_index] = {"min_index": next_min_index, "min_cost": next_min_cost}
        #     else:
        #         best_cost[house_index] = {"min_index":min_index, "min_cost": min_cost}
        # total_min_cost = 0
        # for key in best_cost.keys():
        #     total_min_cost += best_cost[key]["min_cost"]
        # return total_min_cost
        
        # Approach 2: Dynamic programming
        # Resource: https://www.youtube.com/watch?v=fZIsEPhSBgM
        if not costs:
            return 0
        for i in range(2, len(costs)):
            costs[i][0] += min(costs[i-1][1], costs[i-1][2])
            costs[i][1] += min(costs[i-1][0], costs[i-1][2])
            costs[i][2] += min(costs[i-1][0], costs[i-1][1])
        return min(costs[-1][0], costs[-1][1], costs[-1][2])