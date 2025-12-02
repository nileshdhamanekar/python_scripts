# https://leetcode.com/problems/fruit-into-baskets/
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        i = j = max_count = 0
        basket = dict()
        while j < len(tree):
            if tree[j] not in basket and len(basket) < 2:
                basket[tree[j]] = dict()
                basket[tree[j]]["first"] = basket[tree[j]]["last"] = j
            elif tree[j] not in basket and len(basket) >= 2:
                max_count = max(max_count, j-i)
                keys = list(basket.keys())
                if basket[keys[0]]["last"] > basket[keys[1]]["last"]:
                    del basket[keys[1]]
                else:
                    del basket[keys[0]]
                basket[tree[j]] = dict()
                basket[tree[j]]["first"] = basket[tree[j]]["last"] = j
                i = basket[tree[j - 1]]["first"]
            elif tree[j] != tree[j-1]:
                basket[tree[j]]["first"] = basket[tree[j]]["last"] = j
            else:
                basket[tree[j]]["last"] = j
            j += 1
        max_count = max(max_count, j-i)
        return max_count