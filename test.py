import os
x = os.listdir('tasks')
print(x)
file_names=os.listdir("tasks")
print(file_names)
files = {index: os.path.join("tasks", file) for index, file in enumerate(file_names)}
print(files)