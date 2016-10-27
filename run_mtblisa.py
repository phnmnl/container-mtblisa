import sys
# TODO: Finish this and check it works!
cmd = sys.argv[1]
study_id = sys.argv[2]
try:
    from isatools.io import mtbls as MTBLS
except ImportError as e:
    raise RuntimeError("Could not import isatools.io.mtbls package")
if cmd == 'GET':
    tmpdir = MTBLS.get(study_id)
elif cmd == 'GETJ':
    isajson = MTBLS.getj(study_id)
elif cmd == 'GET_FACTORS':
    factor_names = MTBLS.get_factor_names(study_id)
elif cmd == 'GET_FVS':
    fvs = MTBLS.get_factor_values(study_id, sys.argv[3])
elif cmd == 'GET_DATA_FILES':
    if sys.argv[3]:
        data_files = MTBLS.get_data_files(study_id, sys.argv[3])
    else:
        data_files = MTBLS.get_data_files(study_id)
else:
    help = """
        Basic usage:
            run_mtblisa.py <CMD> <study_id>

        To get ISA-Tab from MetaboLights:

            run_mtblisa.py GET <study_id>

        eg. run_mtblisa.py GET MTBLS1

        To get ISA-JSON from MetaboLights:

            run_mtblisa.py GETJ <study_id>

        eg. run_mtblisa.py GETJ MTBLS1

        To get factor names from a study:

            run_mtblisa.py GET_FACTORS <study_id>

        eg. run_mtblisa.py GET_FACTORS MTBLS1

        To get factor values from a study:

            run_mtblisa.py GET_FVS <study_id> <factor_name>

        eg. run_mtblisa.py GET_FVS "Gender"

        To get data file referemces from a study:

            run_mtblisa.py GET_DATA_FILES <study_id> <factor_selection>

        eg. run_mtblisa.py GET_DATA_FILES "{ \"Gender\": \"Male\" }"

    """