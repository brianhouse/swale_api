#!/usr/bin/env python3

import argparse, json
import actions
from mongo import db
from housepy import config, log

parser = argparse.ArgumentParser(description="Retrieve a signal")
parser.add_argument("-s", "--start", type=str, nargs=1)
parser.add_argument("-e", "--end", type=str, nargs=1)
parser.add_argument("-t", "--type",  type=str, nargs=1)
parser.add_argument("-f", "--field",  type=str, nargs="?")
parser.add_argument("-o", "--output",  type=str, nargs=1)
args = vars(parser.parse_args())
args = {key: value[0] if (value is not None) else None for (key, value) in args.items()}
if 'type' in args:
    args['type_'] = args['type']
    del args['type']
print(args)



result = actions.retrieve(db, args['start'], args['end'], args['type_'])

if args['output'] == "json":
    print(json.dumps(result, indent=4, default=lambda obj: str(obj)))
elif args['output'] == "stream":
    pass