# https://leetcode.com/problems/subdomain-visit-count
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        result = dict()
        for item in cpdomains:
            count, cpdomain = item.split(" ")
            domains = list()
            splits = cpdomain.split(".")
            for i in range(len(splits)):
                domains.append(".".join(splits[i:]))
            for domain in domains:
                if domain in result.keys():
                    result[domain] += int(count)
                else:
                    result[domain] = int(count)
        final_result = list()
        for key,value in result.items():
            final_result.append("{0} {1}".format(value, key))
        return final_result
    