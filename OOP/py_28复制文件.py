# 打开文件
file_read = open("README.txt")
file_write = open("README[附件].txt","w")

# 读写文件
text = file_read.read()
file_write.write(text)

#关闭文件
file_read.close()
file_write.close()