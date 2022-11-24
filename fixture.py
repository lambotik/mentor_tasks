import os.path
from pathlib import Path

# r=root, d=directories, f = files
path_env = Path('E:\\Games\\wot\\res\\content\\Environment\\env_null_model')
list_of_files_in_env = []
for r, d, f in os.walk(path_env):
    for file in f:
        if file.endswith('.model') or file.endswith('.visual'):
            list_of_files_in_env.append(file)
            # print('Пути к файлам (model,visual):',os.path.join(r, file))
print('Список фалов (.model,.visual):', *list_of_files_in_env, sep='\n', end='\n')

path_normal = Path('E:\\Games\\wot\\res\\content\\Decor\\dec_001_BranchesCommon\\normal')
list_of_files_in_normal = []
for r, d, f in os.walk(path_normal):
    for file in f:
        if file.endswith('.model') or file.endswith('.visual'):
            list_of_files_in_normal.append(file)
            # print('Пути к файлам (model,visual):', os.path.join(r, file))
print('\nСписок фалов (.model,.visual):', *list_of_files_in_normal, sep='\n', end='\n')

