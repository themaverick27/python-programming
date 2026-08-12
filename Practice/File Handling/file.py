p = open(r"C:\Users\aniwe\Downloads\python_topics.txt")
#print(p.read())

t = open("test.txt", 'w')
t.write("Hello, I am writing some content in this file.")
t.close()

t = open('test.txt', 'a')
t.write("And now I am appending some content in this file.")
t.close()