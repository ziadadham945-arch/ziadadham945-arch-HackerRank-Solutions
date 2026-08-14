# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())

# Top Half
for i in range(1, n, 2):
    print(('.|.' * i).center(m, '-'))

# Center
print('WELCOME'.center(m, '-'))

# Bottom Half
for i in range(n - 2, 0, -2):
    print(('.|.' * i).center(m, '-'))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna