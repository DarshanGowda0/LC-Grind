class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            if i % 15 == 0:
                res+="FizzBuzz",
            elif i%5 == 0:
                res+="Buzz",
            elif i%3 == 0:
                res+="Fizz",
            else:
                res+=str(i),
        
        return res