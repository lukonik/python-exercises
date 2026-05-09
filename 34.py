trial = [1, 2, 3, 4, 5]
paid = [4, 5, 6, 7, 8]

set_trial = set(trial)
set_paid = set(paid)

print(f"Both: {set_trial & set_paid} ")
print(f"Trial Only: {set_trial.difference(set_paid)} ")
print(f"Not both: {set_trial.symmetric_difference(set_paid)} ")
