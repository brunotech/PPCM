from __future__ import print_function

# allow us to import the codebase directory
import sys
import glob
import numpy as np
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

DATASETS = ['SE0714', 'Olympic', 'PsychExp', 'SS-Twitter', 'SS-Youtube',
            'SCv1', 'SV2-GEN'] # 'SE1604' excluded due to Twitter's ToS

def get_results(dset):
    METHOD = 'last'
    RESULTS_DIR = 'results/'
    RESULT_PATHS = glob.glob(f'{RESULTS_DIR}/{dset}_{METHOD}_*_results.txt')
    assert len(RESULT_PATHS)

    scores = []
    for path in RESULT_PATHS:
        with open(path) as f:
            score = f.readline().split(':')[1]
        scores.append(float(score))

    average = np.mean(scores)
    maximum = max(scores)
    minimum = min(scores)
    std = np.std(scores)

    print(f'Dataset: {dset}')
    print(f'Method:  {METHOD}')
    print(f'Number of results: {len(scores)}')
    print('--------------------------')
    print(f'Average: {average}')
    print(f'Maximum: {maximum}')
    print(f'Minimum: {minimum}')
    print(f'Standard deviaton: {std}')

for dset in DATASETS:
    get_results(dset)
