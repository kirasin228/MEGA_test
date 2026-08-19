from models.Task import Task


class Test:
    def __init__(self, name):
        self.name = name
        self.list_tasks = []

    def add_task(self, task):
        self.list_tasks.append(task)

    def count_task(self):
        return len(self.list_tasks)

    def __str__(self):
        s=[]
        for i in self.list_tasks:
            s.append(str(i))
        s= ", ".join(s)
        return "["+s+"]"

t1 = Task("революцио..ый", "революционный", 3)
t2 = Task("не..видеть", "не видеть", 1)
tt = Test("test")
tt.add_task(t1)
tt.add_task(t2)
print(tt)
print(tt.count_task())