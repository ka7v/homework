from random import choice, randint


def generate_students(count, name_list, last_name_list):
    students = {}
    for i in range(count):
        students[i] = {
            'firstname': choice(name_list),
            'lastname': choice(last_name_list),
            'score': randint(50, 100)
        }
    return students


def get_best_students(st_dict):
    sum_score = 0
    for i in st_dict:
        sum_score += st_dict[i]['score']
    mid_score = sum_score / len(st_dict)
    print(mid_score)
    for i in st_dict:
        if st_dict[i]['score'] >= mid_score:
            st = f"{st_dict[i]['firstname']} {st_dict[i]['lastname']} score {st_dict[i]['score']}"
            print(st_dict[i])



name_list = ['samvel', 'davit', 'aram', 'meliq', 'sevak', 'karen', 'vardan', 'eva']
last_name_list = ['noreyan', 'harutyunyan', 'adamyan', 'shahbazyan', 'zaqaryan', 'ghazaryan', 'avetisyan', 'zaqoyan']

student_dict = generate_students(20, name_list, last_name_list)
# print(student_dict)
get_best_students(student_dict)