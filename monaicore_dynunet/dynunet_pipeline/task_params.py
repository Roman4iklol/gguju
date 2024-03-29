# Copyright (c) MONAI Consortium
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

task_name = {
    "01": "Task01_BrainTumour",
    "02": "Task02_Heart",
    "03": "Task03_Liver",
    "04": "Task04_Hippocampus",
    "05": "Task05_Prostate",
    "06": "Task06_Lung",
    "07": "Task07_Pancreas",
    "08": "Task08_HepaticVessel",
    "09": "Task09_Spleen",
    "10": "Task10_Colon",
}

patch_size = {
    "01": [128, 128, 128],
    "02": [160, 192, 80],
    "03": [128, 128, 128],
    "04": [40, 56, 40],
    "05": [320, 256, 20],
    "06": [192, 160, 80],
    "07": [224, 224, 40],
    "08": [192, 192, 64],
    "09": [192, 160, 64],
    "10": [192, 160, 56],
}

spacing = {
    "01": [1.0, 1.0, 1.0],
    "02": [1.25, 1.25, 1.37],
    "03": [0.77, 0.77, 1],
    "04": [1.0, 1.0, 1.0],
    "05": [0.62, 0.62, 3.6],
    "06": [0.79, 0.79, 1.24],
    "07": [0.8, 0.8, 2.5],
    "08": [0.8, 0.8, 1.5],
    "09": [0.79, 0.79, 1.6],
    "10": [0.78, 0.78, 3],
}

clip_values = {
    "01": [0, 0],
    "02": [0, 0],
    "03": [-17, 201],
    "04": [0, 0],
    "05": [0, 0],
    "06": [-1024, 325],
    "07": [-96, 215],
    "08": [-3, 243],
    "09": [-41, 176],
    "10": [-30, 165.82],
}

normalize_values = {
    "01": [0, 0],
    "02": [0, 0],
    "03": [99.40, 39.36],
    "04": [0, 0],
    "05": [0, 0],
    "06": [-158.58, 324.7],
    "07": [77.99, 75.4],
    "08": [104.37, 52.62],
    "09": [99.29, 39.47],
    "10": [62.18, 32.65],
}

data_loader_params = {
    "01": {"batch_size": 8},
    "02": {"batch_size": 2},
    "03": {"batch_size": 8},
    "04": {"batch_size": 9},
    "05": {"batch_size": 2},
    "06": {"batch_size": 2},
    "07": {"batch_size": 2},
    "08": {"batch_size": 2},
    "09": {"batch_size": 2},
    "10": {"batch_size": 2},
}

deep_supr_num = {
    "01": 3,
    "02": 3,
    "03": 3,
    "04": 1,
    "05": 4,
    "06": 3,
    "07": 3,
    "08": 3,
    "09": 3,
    "10": 3,
}
