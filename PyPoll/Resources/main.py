# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
import os
import csv
import numpy as np 


# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
filepath = os.path.join("election_data.csv")
with open(filepath, 'r') as open_file: 
    csv_reader = csv.reader(open_file,delimiter=",")

    next(csv_reader)

    voter_candidate = []
    # unique_candidates = []
    
    cand_votes={}
    cand_opt=[]
    total_votes = 0 

    for row in csv_reader: 
        voter_candidate.append(row[2])
        total_votes = total_votes + 1 

        cand_name=row[2]
        if cand_name not in cand_opt: 
            cand_opt.append(cand_name)
            cand_votes[cand_name]= 0 
        
        cand_votes[cand_name] += 1 
   
# print(cand_votes)

for cand in cand_votes:
    x = cand_votes.get(cand)
    per_x = round(int(x)/int(total_votes) *100 , 2)
    # print(per_x,)
    # print(x)
 

# # As an example, your analysis should look similar to the one below:

# # Election Results
# # -------------------------
# # Total Votes: 3521001
# # -------------------------
# # Khan: 63.000% (2218231)
# # Correy: 20.000% (704200)
# # Li: 14.000% (492940)
# # O'Tooley: 3.000% (105630)
# # -------------------------
# # Winner: Khan
# # -------------------------
print(f'''
        "Election Results"
        "==============================="
        "Total Votes: {total_votes}"
        "==============================="
        ''')

#Could not get the output to work 

# for i in (cand_votes):
#     print(f'''
#     "{cand[i]} : {int(per_x[i])} , % {int(x[i])} "
#     ''')

output = os.path.join("..", "analysis",  'analysis.txt')
with open(output,"w") as new:
    new.write("Election Results")
    new.write("===============================")
    new.write(f"Total Votes: {total_votes}")
    new.write("===============================")