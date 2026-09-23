class Listnode:

    def __init__(self, val):
        self.prev = None
        self.val = val
        self.next = None
    
class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = Listnode(homepage)
        
    def visit(self, url: str) -> None:
        if self.cur.next:
            self.cur.next.prev = None
        self.cur.next = Listnode(url)
        self.cur.next.prev = self.cur
        self.cur = self.cur.next 
        

    def back(self, steps: int) -> str:
        while steps and self.cur.prev:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val
        
    def forward(self, steps: int) -> str:
        while steps and self.cur.next:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)