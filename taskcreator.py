import random
import os

def get_task_names(dir):
    list_ans =[]
    for file in os.listdir(dir):
        fille = open("tasks\\\\"+file, 'r', encoding='utf-8')
        list_ans.append(fille.readline())
        fille.close()
    return list_ans

def file_read(file_name):
    file = open(file_name,'r', encoding='utf-8')
    data = file.readlines()
    file.close()
    return data[1:]


def prepare_data(data):#список из словарей
    words =[]
    for i in range(len(data)):
        line = data[i].split(';')
        word={
            'task': line[0],
            'correct': line[1],
            'level': int(line[2])
        }
        words.append(word)
    return words

def filter_level(data, levl): #фильтер по уровню
    level_data = []
    for elem in data:
        if elem['level']==levl:
            level_data.append(elem)
    return level_data

def create_tasks(data,n): #
    tasks_result = random.sample(data, n)
    return tasks_result


a = file_read('tasks/nn_or_n_in_pril.txt')#25-max
s = prepare_data(a)
d = filter_level(s,3)
q = create_tasks(d, 25)
print(q)
print(''' ''')
print(create_tasks(filter_level(prepare_data(file_read('tasks/pre_pri.txt')),2),50)) #50 - максимум