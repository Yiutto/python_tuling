# _*_ coding: utf-8 _*_
"""
    Created by Yiutto on 2023/5/24.
"""

# for + else 了解
# else的代码会在for循环没有break打断的情况下最后运行
for i in range(0,10):
    if i == 4:
        #continue
        break
    print(i)
else:
    print('=======') # break打断后不会运行


# 对比上面发现不同
for i in range(0,10):
    if i == 4:
        #continue
        break
    print(i)
print('=======')  # 即使break打断 也会运行