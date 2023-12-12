from .blender import BlenderDataset
from .llff import LLFFDataset
import sys 
print(sys.path[0])
sys.path.append('/home/leohsu-cs/DLCV2023/hw4')
from dataset import KlevrDataset

dataset_dict = {'blender': BlenderDataset,
                'llff': LLFFDataset,
                'klevr': KlevrDataset
                }