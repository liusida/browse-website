from browse_website.browse_website import scrape_with_selenium

# Example 1:
# Get formatted HTML from https://liusida.github.io/
text = scrape_with_selenium("https://liusida.github.io/", return_format="HTML")
print(text[:100])
print(len(text))

# Example 2:
# Get cleaned text from https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/
text = scrape_with_selenium("https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/")
print(text[:100])
print(len(text))
