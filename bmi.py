height = float(input("请输入你的身高(米,比如1.70):"))
weight = float(input("请输入你的体重(公斤,比如65):"))
bmi = weight / (height * height)
print("你的BMI是: %.2f" % bmi)
if bmi < 18.5:
    print("体重状态: 偏瘦")
elif bmi < 24:
    print("体重状态: 正常")
elif bmi < 28:
    print("体重状态: 偏胖")
else:
    print("体重状态: 肥胖")