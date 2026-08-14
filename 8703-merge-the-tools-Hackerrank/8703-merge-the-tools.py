def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        sub = string[i:i + k]
        seen = set()
        result = []
        for char in sub:
            if char not in seen:
                seen.add(char)
                result.append(char)
        print("".join(result))
    # your code goes here



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna