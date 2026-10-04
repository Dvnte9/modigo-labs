# The function below is supposed to take a list of posts (each with a list of tags) and return the set of every distinct tag used across all of them. 
#It has a bug — find it and fix it.

# Requirements

# Function name: all_unique_tags (do not rename it)
# Takes one parameter: posts, a list of dictionaries, each shaped like {"title": string, "tags": list of strings}
# Returns a set containing every distinct tag used across all posts
# If posts is empty, return an empty set
# Examples

# all_unique_tags([{"title": "A", "tags": ["python", "web"]}, {"title": "B", "tags": ["web", "css"]}]) → {"python", "web", "css"}
# all_unique_tags([]) → set()
# all_unique_tags([{"title": "A", "tags": []}]) → set()
# Constraints

# posts may be empty.
# A post's tags list may be empty.
# The same tag may appear across multiple posts.
# Note: Your solution will be tested against multiple cases, including an empty post list and a post with no tags at all.


def all_unique_tags(posts):
    tags = set()
    for post in posts:
        tags.update(post["tags"])
    return tags
