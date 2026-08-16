class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for detail in details:
            ten = int(detail[11])
            one = int(detail[12])
            age = one + 10 * ten
            if age > 60:
                res += 1
        return res



        