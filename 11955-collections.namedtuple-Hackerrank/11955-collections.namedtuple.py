# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n = int(input())
Student = namedtuple('Student', input().split())
print(f"{sum(int(Student(*input().split()).MARKS) for _ in range(n)) / n:.2f}")


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna