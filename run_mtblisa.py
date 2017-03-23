#!/usr/bin/env python3

import sys
import shutil
import argparse
import os

help_text = """
ISA slicer - a wrapper for isatools.io.mtbls

Basic usage:
    run_mtblisa.py <command> <study_id> [--outpath path]

To get ISA-Tab from MetaboLights:

    run_mtblisa.py GET <study_id>
eg. run_mtblisa.py GET MTBLS1
    # writes ISArchive to out.zip

To get ISA-JSON from MetaboLights:

    run_mtblisa.py GETJ <study_id>
eg. run_mtblisa.py GETJ MTBLS1
    # writes ISA JSON file to out.json

To get factor names from a study:

    run_mtblisa.py GET_FACTORS <study_id>
eg. run_mtblisa.py GET_FACTORS MTBLS1
    # writes result to out.json

To get factor values from a study:

    run_mtblisa.py GET_FVS <study_id> <factor_name>
eg. run_mtblisa.py GET_FVS "Gender"
    # writes result to out.json

To get data file references from a study (take care to ensure escaping of double quotes):

    run_mtblisa.py GET_DATA_FILES <study_id> <factor_selection>
eg. run_mtblisa.py GET_DATA_FILES {\"Gender\":\"Male\"}
    # writes result to out.json

"""

parser = argparse.ArgumentParser(usage=help_text)
parser.add_argument("command", nargs=2)
parser.add_argument("--outpath", help="Output path  .")
args = parser.parse_args()

cmd = args.command[0]
study_id = args.command[1]

outpath = args.outpath if args.outpath else os.getcwd()
os.chdir(outpath)

try:
    from isatools.io import mtbls as MTBLS
except ImportError as e:
    raise RuntimeError("Could not import isatools.io.mtbls package")
if cmd == 'GET':
    tmpdir = MTBLS.get(study_id)
    if tmpdir is not None:
        shutil.make_archive('out', 'zip', tmpdir)
        shutil.rmtree(tmpdir)
        print("ISA-Tab written to out.zip")
    else:
        print("There was an i/o problem with the ISA-Tab.")
elif cmd == 'GETJ':
    isajson = MTBLS.getj(study_id)
    if isajson is not None:
        import json
        with open("out.json", 'w') as outfile:
            json.dump(isajson, outfile, indent=4)
        print("ISA-JSON written to out.json")
    else:
        print("There was an i/o problem with the ISA-Tab.")
elif cmd == 'GET_FACTORS':
    factor_names = MTBLS.get_factor_names(study_id)
    if factor_names is not None:
        import json
        with open("out.json", 'w') as outfile:
            json.dump(list(factor_names), outfile, indent=4)
        print("Factor names written to out.json")
    else:
        print("There was an i/o problem with the ISA-Tab.")
elif cmd == 'GET_FVS':
    fvs = MTBLS.get_factor_values(study_id, sys.argv[3])
    if fvs is not None:
        import json
        with open("out.json", 'w') as outfile:
            json.dump(list(fvs), outfile, indent=4)
        print("Factor values written to out.json")
    else:
        print("There was an i/o problem with the ISA-Tab.")
elif cmd == 'GET_DATA_FILES':
    if len(sys.argv) > 2:
        import json
        data_files = MTBLS.get_data_files(study_id, json.loads(sys.argv[3]))
        if data_files is not None:
            import json
            with open("out.json", 'w') as outfile:
                json.dump(data_files, outfile, indent=4)
            print("Data files written to out.json")
        else:
            print("There was an i/o problem with the ISA-Tab.")
    else:
        data_files = MTBLS.get_data_files(study_id)
        if data_files is not None:
            import json
            with open("out.json", 'w') as outfile:
                json.dump(data_files, outfile, indent=4)
            print("Data files written to out.json")
        else:
            print("There was an i/o problem with the ISA-Tab.")
else:
    print(help_text)
