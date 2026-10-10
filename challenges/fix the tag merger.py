# The function below is meant to combine two sets of tags into a single set containing every unique tag from both. It has a bug — find it and fix it.

# Requirements

# Function name: merge_tags (do not rename it)
# Takes two parameters: tags1 and tags2, both sets of strings
# Returns a single set containing every tag that appears in either tags1 or tags2, with no duplicates
# Examples

# merge_tags({"python", "web"}, {"web", "css"}) → {"python", "web", "css"}
# merge_tags(set(), {"a", "b"}) → {"a", "b"}
# merge_tags({"x"}, set()) → {"x"}
# merge_tags(set(), set()) → set()
# Constraints

# Either set may be empty.
# The two sets may share some, all, or none of their tags.
# Note: Your solution will be tested against multiple cases, including both sets being empty and the two sets sharing every tag.

def merge_tags(tags1, tags2):
    merged = tags1 | tags2
    return merged
