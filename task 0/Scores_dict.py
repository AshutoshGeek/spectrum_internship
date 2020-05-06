import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
scores = {"Day 1": 100, "Day 2": 108, "Day 3":112, "Day 4":115, "Day 5":150,
          "Day 6":178, "Day 7": 143, "Day 8": 132, "Day 9":190, "Day 10": 235,
          "Day 11":253, "Day 12": 298, "Day 13": 328, "Day 14":390, "Day 15": 257,
          "Day 16":288, "Day 17": 393, "Day 18": 425, "Day 19":458, "Day 20": 450,
          "Day 21":473, "Day 22": 333, "Day 23": 452, "Day 24":490, "Day 25": 495,
          "Day 26":488, "Day 27": 543, "Day 28": 532, "Day 29":590, "Day 30": 605}

scores_list=list(scores.values())
Days=np.arange(1,31)

fig= plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(scores_list,Days)
ax.set_ylabel('Days')
ax.set_xlabel('Score')
plt.show()


score_mean=np.mean(scores_list)
score_median=np.median(scores_list)
score_max=np.amax(scores_list)
score_min=np.amin(scores_list)
score_mode=stats.mode(scores_list)

print("Mean of scores is "+ str(score_mean))
print("Median of scores is "+ str(score_median))
print("Max score is "+ str(score_max))
print("Min score is "+ str(score_min))
print("Mode of scores is "+ str(score_mode))
