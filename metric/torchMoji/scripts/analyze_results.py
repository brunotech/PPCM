from __future__ import print_function

import sys
import glob
import numpy as np

DATASET = 'SS-Twitter' # 'SE1604' excluded due to Twitter's ToS
METHOD = 'new'

# Optional usage: analyze_results.py <dataset> <method>
if len(sys.argv) == 3:
    DATASET = sys.argv[1]
    METHOD = sys.argv[2]

RESULTS_DIR = 'results/'
RESULT_PATHS = glob.glob(f'{RESULTS_DIR}/{DATASET}_{METHOD}_*_results.txt')

if not RESULT_PATHS:
    print(
        f"Could not find results for \'{DATASET}\' using \'{METHOD}\' in directory \'{RESULTS_DIR}\'."
    )
else:
    scores = []
    for path in RESULT_PATHS:
        with open(path) as f:
            score = f.readline().split(':')[1]
        scores.append(float(score))

    average = np.mean(scores)
    maximum = max(scores)
    minimum = min(scores)
    std = np.std(scores)

    print(f'Dataset: {DATASET}')
    print(f'Method:  {METHOD}')
    print(f'Number of results: {len(scores)}')
    print('--------------------------')
    print(f'Average: {average}')
    print(f'Maximum: {maximum}')
    print(f'Minimum: {minimum}')
    print(f'Standard deviaton: {std}')
