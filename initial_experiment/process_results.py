import fileinput
import pprint
import os

from common import FAMILY_FILEPATHS, SOLVERS

def add_data_from_line(line, data):
    problem_filepath, delta_s, solver_filepath, timed_out_s, valid_s  =\
        line.split("|")
    delta = float(delta_s)
    timed_out = timed_out_s.strip() == "TO"
    valid = valid_s.strip() == "V"
    problem_sfilepath = os.path.basename(problem_filepath).strip()
    solver_sfilepath = solver_filepath.split("/")[1].strip()

    if problem_sfilepath not in data:
        data[problem_sfilepath] = {}

    if solver_sfilepath not in data[problem_sfilepath]:
        if not timed_out and valid:
            data[problem_sfilepath][solver_sfilepath] = delta

def best_times(data):
    bests = {}

    for problem in data:
        best_solver = None
        best_time = None
        bests[problem] = {}
        for solver in data[problem]:
            if best_time is None or data[problem][solver] < best_time:
                best_time = data[problem][solver]
                best_solver = solver

        bests[problem] = (best_solver, best_time)

    return bests

def split_in_families(bests):
    split_bests = {}
    for family_filepath_tpl, family_range in FAMILY_FILEPATHS:
        family_sfilepath_tpl = os.path.basename(family_filepath_tpl)
        split_bests[family_sfilepath_tpl] = {}
        for i in family_range:
            problem_filepath = family_filepath_tpl % i
            problem_sfilepath = os.path.basename(problem_filepath)

            if problem_sfilepath in bests:
                split_bests[family_sfilepath_tpl][problem_sfilepath] = \
                    bests[problem_sfilepath]

    return split_bests

def analyze_one_step(split_bests):
    comp_count = 0
    good_count = 0
    for family_filepath_tpl, family_range in FAMILY_FILEPATHS:
        family_sfilepath_tpl = os.path.basename(family_filepath_tpl)
        if not split_bests[family_sfilepath_tpl]:
            continue

        for i in family_range[:-1]:
            problem_filepath = family_filepath_tpl % i
            next_problem_filepath = family_filepath_tpl % (i + 1)

            problem_sfilepath = os.path.basename(problem_filepath)
            next_problem_sfilepath = os.path.basename(next_problem_filepath)

            best_solver, best_time = \
                split_bests[family_sfilepath_tpl][problem_sfilepath]
            next_best_solver, next_best_time = \
                split_bests[family_sfilepath_tpl][next_problem_sfilepath]
            if best_solver is not None and next_best_solver is not None:
                comp_count += 1
                if best_solver == next_best_solver:
                    good_count += 1

    return float(good_count)/comp_count

if __name__ == "__main__":
    data = dict()
    for line in fileinput.input():
        add_data_from_line(line, data)

    pprint.pprint(split_in_families(best_times(data)))
    print("Percentage of times the best solver for the next size was the same " +
            "as for the current size:",
          analyze_one_step(split_in_families(best_times(data))))

