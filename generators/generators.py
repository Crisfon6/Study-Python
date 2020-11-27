#---------------------------- generator
#------------------ yield
# def generatePairs(limit):
#     num= 1
#     myList= []
#     while num<limit:
#         myList.append(num*2)
#         num+=1
#     return myList
# def generatorPairs(limit):
#     num= 1
#     print("function")
#     while num<limit:
#         print("while")
#         yield num*2
#         print("yield")
#         num+=1
#         print("num")

# print(generatePairs(20))#without use yiel
# pairsGenerator = generatorPairs(10)#using yield... get all 
# # print(pairsGenerator)
# ##-----------get value by value
# print(next(pairsGenerator))#get element by element
# print("more code...")
# print(next(pairsGenerator))


#------------------- yield from 
#recorre the elements inside a element yield

def return_city(*citys):
    print("func")
    for el in citys:
        # for subEl in el: ## this use if not existed yield from
        #     yield subEl
        print("for")
        yield from el
        print("end")

citys_returned = return_city("Valencia","Venecia","Toronto")
print(next(citys_returned))
print(next(citys_returned))
print(next(citys_returned))
print(next(citys_returned))
print(next(citys_returned))
print(next(citys_returned))
print(next(citys_returned))
print(next(citys_returned))
print(next(citys_returned))
print(next(citys_returned))