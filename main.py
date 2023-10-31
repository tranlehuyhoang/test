import os

def makeCommits(days):
    if days < 1:
        return
    else:
        dates = f"{days} days ago"
        with open('data.txt', 'a') as file:
            file.write(f'{dates} <- this was the commit for the day!!\n')
        # staging
        os.system('git add data.txt')
        # commit
        os.system('git commit --date="' + dates + '" -m "First commit for the day!"')
        # push
        os.system('git push -u origin main')
        makeCommits(days-1)

makeCommits(365)