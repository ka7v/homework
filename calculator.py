def addition(num:int,num2:int):
    return num + num2
def subtraction(num,num2):
    return num - num2
def multiplication(num, num2):
    return num * num2
def division(num, num2):
    return num / num2
def func5():
    print('calculator stopped')

print("please select operation -\n" \
      "1. addition\n"
      "2. subtraction\n"
      "3. multiplication\n"
      "4. division\n"
      "5. stop")
action = 0
while True:
    action = input("input the acion number")
    inp_num = int(input("input num:"))
    inp_num2 = int(input("input 2 num:"))
    calculator = {'1':addition(inp_num, inp_num2),
                  '2':subtraction(inp_num, inp_num2),
                  '3':multiplication(inp_num, inp_num2),
                  '4':division(inp_num, inp_num2),
                  }
    print(calculator[action])