import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    lines = []
    for i in range(size):
        s = "-".join(alphabet[i:size])
        lines.append((s[::-1] + s[1:]).center(4 * size - 3, '-'))
    print('\n'.join(lines[:0:-1] + lines))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna