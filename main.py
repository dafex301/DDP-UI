"""""
filename = "text.txt"
my_file = open(filename)
my_file_content = my_file.read()
print("Content of " + filename + ":\n" + my_file_content)
my_file.close()
"""""

"""""
filename = "bella-ciao.txt"
my_file = open(filename, mode='a')
print("ciao amore", file=my_file)
my_file.close()
"""""

def hi(name):
    print(f'hi {name}')

hi("Fahrel")