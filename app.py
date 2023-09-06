import os

def makeCommits (days):

    if days <1:
        os.system('git push')
    for j in range (0, randint(1, 10)):
        d= str(i)+ ' days ago'
        with open ('file.txt', 'a') as file:
            file.write(d)
        os.system('git add .')
        os.system('git commit --date=" ' + d + ' " -m "commit"')

os.system('git push -u origin main')        