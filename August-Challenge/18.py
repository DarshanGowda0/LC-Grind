class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # naive soln - keep incrmntr of candies, keep incrmtr for people % num_ppl
        
        c_i = 1
        p_i = 0
        arr = [0] * num_people
        while candies > 0:
            arr[p_i] += min(c_i, candies)
            candies -= c_i
            p_i = (p_i + 1) % num_people
            c_i += 1
            
        return arr