class BrowserHistory:

    def __init__(self, homepage: str):
        self.arr = [homepage]
        self.cur = 0

    def visit(self, url: str) -> None:
        # print("visit", url, self.cur, self.arr)
        if self.cur < len(self.arr) - 1:
            self.cur += 1
            self.arr[self.cur] = url
            while len(self.arr) > self.cur + 1:
                self.arr.pop()
        else:
            self.cur += 1
            self.arr.append(url)
            
        # print("visit", url, self.arr, self.cur)

    def back(self, steps: int) -> str:
        # print("back", steps, self.cur, self.arr)
        self.cur = max(0, self.cur - steps)
        # print("returning", self.arr[self.cur])
        return self.arr[self.cur]

    def forward(self, steps: int) -> str:
        self.cur = min(len(self.arr) - 1, self.cur + steps)
        # print("forward", self.arr[self.cur])
        return self.arr[self.cur]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

 
# 0 1 2 3
# l g f l 
# c = 0