import os.path
from pathlib import Path

# r=root, d=directories, f = files
path_env = Path('E:\\Games\\wot\\res\\content\\Environment\\env_null_model')
for r, d, f in os.walk(path_env):
    for file in f:
        if file.endswith('.model') or file.endswith('.visual'):
            print(os.path.join(r, file))

path_normal = Path('E:\\Games\\wot\\res\\content\\Decor\\dec_001_BranchesCommon\\normal')
for r, d, f in os.walk(path_normal):
    for file in f:
        if file.endswith('.model') or file.endswith('.visual'):
            print(os.path.join(r, file))
