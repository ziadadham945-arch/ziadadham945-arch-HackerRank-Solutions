

# Complete the solve function below.
def solve(s):
    for word in s.split(' '):
        s = s.replace(word, word.capitalize())
    return s


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna