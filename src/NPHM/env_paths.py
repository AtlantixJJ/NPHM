import json

CODE_BASE = f'/home/jianjinx/data/My3D/thirdparty/NPHM'
ASSETS = f'{CODE_BASE}/assets/'
SUPERVISION_IDENTITY = f'{CODE_BASE}/dataset/point_cloud/identity'
SUPERVISION_DEFORMATION_OPEN = f'{CODE_BASE}/dataset/point_cloud/expression'
DATA_SINGLE_VIEW = f'{CODE_BASE}/dataset/NPHM_raw/single_view_synthetic_benchmark'
DATA = f'{CODE_BASE}/dataset/NPHM_raw'

DUMMY_DATA = f'{CODE_BASE}/dataset/dummy_data/dataset/'
DUMMY_single_view = f'{CODE_BASE}/dataset/dummy_data/single_view/'

EXPERIMENT_DIR = f'{CODE_BASE}/expr'
FITTING_DIR = f'{CODE_BASE}/expr/fitting'

ANCHOR_INDICES_PATH = ASSETS + 'lm_inds_39.npy'
ANCHOR_MEAN_PATH = ASSETS + 'anchors_39.npy'
FLAME_LM_INDICES_PATH = ASSETS + 'flame_up_lm_inds.npy'

NUM_SPLITS = 200
NUM_SPLITS_EXPR = 100

with open(CODE_BASE + '/dataset/neutrals_open.json') as f:
    _neutrals = json.load(f)
with open(CODE_BASE + '/dataset/neutrals_closed.json') as f:
    _neutrals_closed = json.load(f)
neutrals = {int(k): v for k,v in _neutrals.items()}
neutrals_closed = {int(k): v for k,v in _neutrals_closed.items()}

subjects_eval = [199, 286, 290, 291, 292, 293, 294, 295, 297, 298]

subjects_test = [99, 283, 143, 38, 241, 236, 276, 202, 98, 254, 204, 163, 267, 194, 20, 23, 209, 105, 186, 343, 341,  363, 350]




invalid_expressions_test = {
    143: [0, 1, 5],
    163: [6 ], # --> FLAME fitting failed to move in proper coordinate system
    38: [ 1, 5, 8, 9, 10, 11, 15, 16, 17, 18, 19], # hair changes --> maybe train or eval set
    236: [8, ],
    202: [24,],
    98: [0],
    254: [1, ],
    204: [16, ],
    267: [0, 7,  13, 22],
    194: [0, 1, 2, 3,  9, 11, 14, 18, 22 ],
    20: [17, 6, 11, 13, ],
    209: [7, 8, 9,  10, 15, 20, ],
    105: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    186: [7, 8, 9,  11, 21, ],
    343: [9, 11, ],
    363: [1, 11, 12, 14, ],
    350: [4, ],
}

for s in subjects_test:
    if s not in invalid_expressions_test.keys():
        invalid_expressions_test[s] = []


bad_scans = {
    261: [19],
    88: [19],
    79: [16, 17, 18, 19, 20],
    100:[0],
    125:[1, 4, 5],
    106:[20],
    362:[20],
    363:[1],
    345:[12],
    360:[6, 14],
    85:[2],
    292:[9],
    298:[23, 24, 25, 26],
}
