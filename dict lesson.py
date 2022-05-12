# def my_dict(ls:list)-> dict:
#     my_dict = {}
#     for i in ls:
#         my_dict.update({i:i})
#     return my_dict
#
# print(my_dict([12, 42, 84, 78]))

#
# from random import randint, choice
# def student(count, name, lastname):
#     students = {}
#     for i in range(count):
#         students[i] = {
#             'firstname': choice(name),
#             'lastname': choice(lastname),
#             'score': randint(50, 99)
#         }
#     return students
#
# def get_best_student(st_dict):
#     sum_score = 0
#     for i in st_dict:
#         sum_score += st_dict[i]['score']
#     mid_score = sum_score / len(st_dict)
#     print(mid_score)
#     best_student = {}
#     for i in st_dict:
#         if st_dict[i]['score'] > mid_score:
#             best_student[i] = st_dict[i]
#             print(st_dict[i])
#
#
# name1 = ['samvel', 'vardan', 'david', 'sevak', 'karen', 'meliq', 'eva']
# lastname1 = ['adamyan', 'ghazaryan', 'zaqaryan', 'shahbazyan', 'noreyan', 'avetisyan', 'zaqoyan']
#
# print(student(20, name1, lastname1 ))


from random import randint
def func(n):
    st = ''
    for i in range(n):
        st += chr(randint(33, 125))
    return st

def func_1(st):
    dict_1 = {}
    for i in range(10):
        dict_1[i] = st.count(f'{i}')
    return dict_1

my_string = func(100)
print(my_string)
res_dict = func_1(my_string)
print(res_dict)