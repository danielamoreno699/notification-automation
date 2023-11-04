def read():
    with open('src/prices.csv', 'r') as file:
        content = file.readlines()
        print(content)
    return content

print(read())