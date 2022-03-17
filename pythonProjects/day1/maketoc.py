import glob
import os

LESSON = '0*.py'
TOCFILE = 'toc.md'
DIRS = 'day?'

with open(TOCFILE, 'w', encoding='UTF8') as toc:
    for dir_ in glob.glob(DIRS):
        for file in glob.glob(os.path.join(dir_, LESSON)):
            toc.write(f'#[{file}]({file})\n')
            for linum, line in enumerate(open(file, encoding='UTF8')):
                if not line.startswith('##'):
                    continue
                line = line.strip()
                toc.write(f'{line} : {line + 1}\n')
            toc.write(f'\n{"-" * 60}\n')