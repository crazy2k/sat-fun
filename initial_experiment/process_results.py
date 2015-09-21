import fileinput
import pprint
import os

from common import FAMILY_FILEPATHS

def add_data_from_line(line, data):
    if line.startswith("WARNING! DIMACS"):
        return

    problem_filepath, delta_perf_s, _, solver_filepath, timed_out_s, valid_s = line.split("|")
    delta = float(delta_perf_s)
    timed_out = timed_out_s.strip() == "TO"
    valid = valid_s.strip() == "V"
    problem_sfilepath = os.path.basename(problem_filepath).strip()
    solver_sfilepath = solver_filepath.split("/")[3].strip()

    if problem_sfilepath not in data:
        data[problem_sfilepath] = {}

    if solver_sfilepath not in data[problem_sfilepath]:
        if valid or timed_out:
            data[problem_sfilepath][solver_sfilepath] = delta if not timed_out \
                else float("inf")

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

        for i in family_range:
            problem_filepath = family_filepath_tpl % i
            next_problem_filepath = family_filepath_tpl % (i + 1)

            problem_sfilepath = os.path.basename(problem_filepath)
            next_problem_sfilepath = os.path.basename(next_problem_filepath)

            family_bests = split_bests[family_sfilepath_tpl]
            if problem_sfilepath in family_bests and \
                            next_problem_sfilepath in family_bests:

                best_solver, best_time = \
                    split_bests[family_sfilepath_tpl][problem_sfilepath]
                next_best_solver, next_best_time = \
                    split_bests[family_sfilepath_tpl][next_problem_sfilepath]

                if best_time != float("inf") \
                        and next_best_time != float("inf") \
                        and best_solver is not None \
                        and next_best_solver is not None:
                    comp_count += 1
                    if best_solver == next_best_solver:
                        good_count += 1

    return float(good_count)/comp_count

def format_results_dict(results):
    for family in results:
        print("------------------")
        print("Family: ", family)
        print()
        for problem in sorted(results[family]):
            best_solver, best_time = results[family][problem]
            print("  Problem:", problem)
            print("  Best solver:", best_solver)
            print("  Best time:", best_time)
            print()

if __name__ == "__main__":
    data = dict()
    for line in fileinput.input():
        add_data_from_line(line, data)

    pprint.pprint(data)
    format_results_dict(split_in_families(best_times(data)))
    print("Percentage of times the best solver for the next size was the same " +
            "as for the current size:",
          analyze_one_step(split_in_families(best_times(data)))*100)

