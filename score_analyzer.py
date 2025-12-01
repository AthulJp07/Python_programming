print('Enter the no of students:')
n=int(input())
score =[]
for i in range(n):
    score.append(int(input(f"Enter the score of student {i+1}\n")))

avg = sum(score)/n
max_score = max(score)
min_score = min(score)
pass_count = len([s for s in score if s>=40])
print(f'The average score is {avg}')
print(f'The highest score is {max_score}')
print(f'The lowest score is {min_score}')
print(f'The number of students who passed is {pass_count}')