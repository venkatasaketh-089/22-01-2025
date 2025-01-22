class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = [homepage]  # List to store the history of URLs
        self.current_index = 0      # Index to track the current page

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        # Visit a new URL and clear forward history
        self.history = self.history[:self.current_index + 1]  # Keep history up to current
        self.history.append(url)  # Add the new URL
        self.current_index += 1    # Move current index to the new URL

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        # Move back in history
        self.current_index = max(0, self.current_index - steps)  # Ensure index doesn't go below 0
        return self.history[self.current_index]  # Return the current URL after moving back

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        # Move forward in history
        self.current_index = min(len(self.history) - 1, self.current_index + steps)  # Ensure index doesn't go out of bounds
        return self.history[self.current_index]  # Return the current URL after moving forward

# Example Usage:
browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")      # You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com")     # You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com")      # You are in "facebook.com". Visit "youtube.com"
print(browserHistory.back(1))            # Output: "facebook.com"
print(browserHistory.back(1))            # Output: "google.com"
print(browserHistory.forward(1))         # Output: "facebook.com"
browserHistory.visit("linkedin.com")     # You are in "facebook.com". Visit "linkedin.com"
print(browserHistory.forward(2))         # Output: "linkedin.com"
print(browserHistory.back(2))            # Output: "google.com"
print(browserHistory.back(7))            # Output: "leetcode.com"
