# 1. 打开文件
file = open("py_23导入.py")

# 2.读取文件内容
text = file.read()
print(text)
print(len(text))

print("-" * 50)

#文件指针已经移动到文件的末尾，无法读取到内容
text = file.read()
print(text)
print(len(text))

# 3。关闭文件
file.close()