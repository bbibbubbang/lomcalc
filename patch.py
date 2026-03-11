with open("index.html", "r") as f:
    content = f.read()

content = content.replace('width: 100%;\n            padding: 0.5rem;', 'width: 100%;\n            max-width: 15rem;\n            padding: 0.5rem;')

with open("index.html", "w") as f:
    f.write(content)
