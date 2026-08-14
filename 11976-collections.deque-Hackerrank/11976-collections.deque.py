# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

d = deque()
n = int(input())

for _ in range(n):
    cmd = input().split()
    method = cmd[0]
    
    if len(cmd) > 1:
        getattr(d, method)(cmd[1])
    else:
        getattr(d, method)()

print(*d)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna