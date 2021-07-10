from argparse import ArgumentParser
from conventor import convent
from yaml import load
import yaml


parser = ArgumentParser()
parser.add_argument('-f', help='TeX file to convent')
parser.add_argument('--config', help='config file', default='cfg.json')
args = parser.parse_args()
config = load(args.config)

if __name__ == '__main__':
    with open(args.f) as f:
        document = f.readlines()
    
    md = convent(document, config)
    with open(args.f[:-3] + 'md', 'x') as f:
        f.writelines(md)
    print("Done")
    exit(0)
