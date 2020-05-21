class BMI:
    def __init__(self):
        try:
            height = float(input("Input your height (m) :"))
            weight = float(input("Input your weight (kg) :"))
            self.bmi_value = round(weight / (height ** 2), 1)
        except Exception as err:
            print(err)

    def printBMI(self):
        print("Your BMI is ",self.bmi_value)


class ChinaBMI(BMI):
    def printBMI(self):
        if self.bmi_value < 18.5:
            print("你的BMI的值是：{} \n体型偏瘦".format(self.bmi_value))
        elif 18.5 <= self.bmi_value < 24:
            print("你的BMI的值是：{} \n体型正常".format(self.bmi_value))
        elif 18.5 <= self.bmi_value < 28:
            print("你的BMI的值是：{} \n体型偏胖".format(self.bmi_value))
        elif self.bmi_value >= 28:
            print("你的BMI的值是：{} \n体型肥胖".format(self.bmi_value))


BMI1 = BMI()
BMI1.printBMI()

# ChinaBMI1 = ChinaBMI()
# ChinaBMI1.printBMI()
