class BrowserHistory:

    def __init__(self, homepage: str):
        # Initialize the history list with the homepage and set the current pointer
        self.history = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        # Clear all forward history by deleting elements after the current pointer
        del self.history[self.curr + 1:]
        # Append the new url and move the pointer forward
        self.history.append(url)
        self.curr += 1

    def back(self, steps: int) -> str:
        # Move back by 'steps', but don't go below index 0
        self.curr = max(0, self.curr - steps)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        # Move forward by 'steps', but don't go beyond the last index
        self.curr = min(len(self.history) - 1, self.curr + steps)
        return self.history[self.curr]