markdown_text = """
# This is a sample report of the <train.csv> containing Californian house prices

Here's some summary data:

![Summary Data](./fig/sample2.png)

Here is a box 'n whisker graph containing all the columns of a the data.

![Image](./fig/sample.png)


After some cleaning, it'll look like: 

![Image](./fig/sample2.png)

"""


# Open a file to write the markdown content
with open("report.md", "w", encoding='utf-8') as file:
    file.write(markdown_text)

print("Markdown file created!")
