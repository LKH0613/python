import matplotlib.pyplot as plt

f = open("Alice.txt", "r", encoding = "utf-8")
book = f.read()

words = input("검색하려는 단어 5개:")
words = words.split()
cnt = []

for word in words:
    n = book.count(word)
    cnt.append(n)
    
f.close()
    
plt.rc("font", family = "Malgun Gothic")
plt.title("단어 개수 결과")
plt.xlabel("검색 단어")
plt.ylabel("단어 개수")
plt.bar(words, cnt)
plt.show()

'''
for _ in range(5):
    words.append(input())

for word in words:
    n = book.count(word)
    print("%s : %d번" %(word, n))

f.close()
'''
'''
words = input("검색하려는 단어 5개:")

words = words.split()

for word in words :
    n = book.count(word)
    print("%s : %d번" %(word, n))

f.close()
'''
