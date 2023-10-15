
import re

# put angles around all numbers
# catch them as a group and then replace the group.
text = "Turn the 35 boxes into the 100 boxes."
re.sub(r"([0-9]+)", r"<\1>", text)
re.sub(r'(\d+)', r'<\1>', text)


# capture group
# which text will the patter match
pattern = r"the (.*)er they (.*), the \1er we \2"
text1 = "the faster they ran, the faster we ran"
text2 = "the faster they ran, the faster we ate"

re.match(pattern, text1)
re.match(pattern, text2)
matched = re.match(pattern, text1)
print(matched)
type(matched)
# entire matched string
matched.group(0)
# each group being captured
matched.group(1)
matched.group(2)
# start and end position for matched string
matched.start()
matched.end()

# not capture group  (?: pattern ).
# "some" just match no capture, "cats" match and capture
pattern = r"(?:some|a few) (people|cats) like some \1"
text1 = "some cats like some cats"
text2 = "some cats like some dogs"
re.match(pattern, text1)
re.match(pattern, text2)
# entire matched string
matched = re.match(pattern, text1)
matched.group(0)
# each group being captured
matched.group(1)
matched.group(2)


# The (?=pattern) is a part of a regular expression known as a "positive lookahead" assertion.
# It is used to match a specific pattern only if it is followed by another specific pattern,
# without including the second pattern in the match.

# The (?!pattern) is a part of a regular expression known as a "negative lookahead" assertion.
# It is used to match a specific pattern only if it is NOT followed by another specific pattern.

text = "I like apple pie, but not apple juice or apple sauce."

# apple not followed by juice
pattern1 = r"apple(?! juice)"
# apple followed by pie
pattern2 = r"apple(?= pie)"

# should find two
re.findall(pattern1, text)
# should find one
re.findall(pattern2, text)
