import random
score = float(input("Enter score: "))
random_score = random.randint(1,101)
print(random_score)
def score_sort(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif 100 >= score >= 90:
        print("Excellent")
    elif 90 > score >= 50:
        print("Passable")
    else:
        print("Bad")
score_sort(score)

def score_file(score):
    score_file = open("results.txt","w")
    print(score,file=score_file)
    score_file.close()
score_file(score)

def score_sort_random(random_score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif 100 >= score >= 90:
        print("random_score is Excellent")
    elif 90 > score >= 50:
        print("random_score is Passable")
    else:
        print("random_score is Bad")
score_sort_random(random_score)

def score_file_random(random_score):
    score_file = open("results.txt","w")
    print(score,file=score_file)
    score_file.close()
score_file_random(random_score)