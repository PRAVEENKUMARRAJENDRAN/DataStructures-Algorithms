class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        opvalue = 0 

        for i in operations:
            if i == "++X" or i == "X++":
                opvalue += 1
            else:
                opvalue -= 1

        return opvalue

        