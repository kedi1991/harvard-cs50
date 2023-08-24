persons = [{"name":"okurut henry","school":"makerere", "age":24},{"name":"oong","school":"kyambogo", "age":94}, {"name":"Miguel olivares","school":"alicante university", "age":54}]

def sortFiles(item):
    item.sort(key= lambda item: item["school"])

# we can instead use lambda function thst takes an input and and output

# def f(cpxItem):
#     return cpxItem["name"]

sortFiles(persons)

print(persons)