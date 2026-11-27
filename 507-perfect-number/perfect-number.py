class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # if num==1:
        #     return False
        # sum=0
        # for i in range(1,num):
        #     if num%i==0:
        #         sum+=i
        # return sum==num
                

        if num <= 1:
            return False

        total = 1

        for i in range(2, num):
            if i * i > num:
                break

            if num % i == 0:
                total += i

                if i != num // i:
                    total += num // i

        return total == num