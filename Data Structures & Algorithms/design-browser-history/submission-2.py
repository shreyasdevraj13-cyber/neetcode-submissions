class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur = 0
        self.bound = 0
        

    def visit(self, url: str) -> None:
        self.cur += 1
        if self.cur < len(self.history):
            self.history[self.cur] = url
        else:
            self.history.append(url)
        self.bound = self.cur

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.history[self.cur]
        

    def forward(self, steps: int) -> str:
        self.cur = min(self.bound, self.cur + steps)
        return self.history[self.cur]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)