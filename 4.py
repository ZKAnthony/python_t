'''
file= open('my file.txt','r') 
content=file.readline()
print(content)


second_read_time=file.readline()  # 读取第二行
print(second_read_time)


file= open('my file.txt','r') 
content=file.readlines() # python_list 形式
print(content)
'''


def age(n):
    if n == 1:
        return 18
    else:
        return age(n-1) + 2


print(age(5))