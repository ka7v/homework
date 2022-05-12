# def input_product(ls: list, pr_name, pr_price):
#     element = (pr_name, pr_price)
#     ls.append(element)
#
#
# def sell(ls:list, name):
#     for i in range(len(ls)):
#         if ls[i][0] == name:
#             pr = ls.pop(i)
#             print(f'you sell {pr}')
#     print(ls)
#
# def show(ls:list):
#     for i in ls:
#         print(i)
#
# def main():
#     pr_list = []
#     while True:
#         print('1. add product \n2. sell product\n 3. show all product\n 4. exit')
#         n = int(input("please choose action "))
#         if n == 1:
#             name = input('please input name')
#             price = int(input("please input price"))
#             input_product(pr_list, name, price)
#         elif n == 2:
#             name = input("please input name")
#             sell(pr_list, name)
#         elif n == 3:
#             print(show(pr_list))
#         elif n == 4:
#             break
#         else:
#             continue
#
# main()






def func1(*args):
    c = (args)
    my_list1 = []
    my_list2 = []
    for i in range(0, len(c) -1):
        for j in range(1, len(c) -1):
            sum1 = c[0]
            sum2 = c[1] * c[i]
            my_list1.append(sum1)
            my_list2.append(sum2)
    print(my_list1)
    print(my_list2)


func1(1, 52, 12, 14, 41, 12,)