import numpy as np

#1
trial = np.arange(35)
print("#1 trial:\n", trial)

#2
trialB = trial.reshape(7, 5)
print("\n#2 trialB (7x5):\n", trialB)

#3
trial = np.resize(trial, (4, 10))
print("\n#3 trial resized to 4x10:\n", trial)

#4
second_row_trialB = trialB[1]
print("\n#4 second row of trialB:\n", second_row_trialB)

#5
last_three_first_row_trialB = trialB[0, -3:]
print("\n#5 last three columns of first row in trialB:\n", last_three_first_row_trialB)

#6
div_by_2_from_trial = trial[trial % 2 == 0]
print("\n#6 elements in trial divisible by 2:\n", div_by_2_from_trial)

#7
trialC = trial + 7
print("\n#7 trialC (trial + 7):\n", trialC)

#8
trialD = np.sqrt(trial)
print("\n#8 trialD (sqrt of trial):\n", trialD)

#9
trialE = trial * trialC
print("\n#9 trialE (elementwise product of trial and trialC):\n", trialE)

#10
concat_trial_trialC = np.concatenate((trial, trialC), axis=0)
print("\n#10 concatenated trial and trialC:\n", concat_trial_trialC,"\n\n\n\n")
