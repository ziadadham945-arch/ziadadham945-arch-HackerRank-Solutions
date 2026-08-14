# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = int(input())
words = [input().strip() for _ in range(n)]
counts = Counter(words)

print(len(counts))
print(*counts.values())


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna