import argparse
import json
import os

def get_project_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_config(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(description='DevOps Scripts')
    parser.add_argument('-c', '--config', help='Configuration file', required=True)
    args = parser.parse_args()

    config = load_config(args.config)
    project_root = get_project_root()

    # Your code here
    print('Project Root:', project_root)
    print('Config:', config)

if __name__ == '__main__':
    main()