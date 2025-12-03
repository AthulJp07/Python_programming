marks=[]
def add_mark(mark):
    marks.append(mark)

def delete_db(index):
    marks.pop(index)

def print_marks(i):
    for mark in marks[i]:
        print(mark)

def performance(i):
    print(f"Total Marks: {sum(marks[i])}")
    print(f"Average Marks: {sum(marks[i]/len(marks[i]))}")