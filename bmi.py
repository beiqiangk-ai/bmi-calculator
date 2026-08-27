def calculate_bmi(height_cm,weight):
    """计算BMI并返回结果,身高按厘米输入"""
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return bmi

def get_status(bmi):
    """根据BMI返回健康状态"""
    if bmi < 18.5:
        return "偏瘦"
    elif bmi < 24:
        return "正常"
    elif bmi < 28:
        return "偏胖"
    else:
        return "肥胖"
    
while True:
    height_input = input("请输入身高(厘米,比如170),输入'退出'结束程序:")

    if height_input == "退出":
        print("程序已结束,再见!")
        break
    
    weight_input = input("请输入体重(公斤,比如65):")

    try:
        height = float(height_input)
        weight = float(weight_input)

        bmi = calculate_bmi(height,weight)
        status = get_status(bmi)

        print("你的BMI是: %.2f, 状态: %s" % (bmi,status))
        print("_" * 20)

    except ValueError:
        print("输入有误，请输入数字!请重新开始。")
