team_1 = "Georgia Tech"
team_1_score = 28
team_2 = "Georgia"
team_2_score = 28


# - If one team beat the other, print:
#     "[winner] beat [loser] by [margin]"
# - If neither team won, print:
#     "[team_1] played [team_2] and it was a tie"


if team_1_score > team_2_score:
    print(team_1 , "beat" , team_2 , "by" , team_1_score - team_2_score)
elif team_1_score < team_2_score:
    print(team_2 , "beat" , team_1 , "by" , team_2_score - team_1_score)
else:
    print(team_1 , "played" , team_2 , "and it was a tie")
