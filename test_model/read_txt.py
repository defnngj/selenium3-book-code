# 读取文件
with(open("./data_file/user_info.txt", "r")) as user_file:
    data = user_file.readlines()

# 格式化处理
users = []
for line in data:
    user = line[:-1].split(":")
    users.append(user)

# 打印users二维数组
print(users)

"""
# 调用Mail类
mail = Mail(driver)

# 用户名为空
mail.login(users[0][0], users[0][1])

# 密码为空
mail.login(users[1][0], users[1][1])

# 用户名密码错误
mail.login(users[2][0], users[2][1])

# 管理员登录 admin
mail.login(users[3][0], users[3][1])

"""
