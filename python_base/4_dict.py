# 定义字典
dicts = {"username":"zhangsan",'password':123456}

# 打印字典中的所有key
print(dicts.keys())

# 打印字典中的所有value
print(dicts.values())


# 向字典中添加键/值对
dicts["age"] = 22

# 循环打印字典key 和value
for k, v in dicts.items():
    print("dicts keys is %r " %k)
    print("dicts values is %r " %v)

# 删除键是'password'的项
dicts.pop('password')

# 打印字典以列表方法返回
print(dicts.items())
