import fileinput
import pprint
import os

def add_data_from_line(line, data):
    problem_filepath, delta_s, solver_filepath, timed_out_s, valid_s  =\
        line.split("|")
    delta = float(delta_s)
    timed_out = timed_out_s.strip() == "TO"
    valid = valid_s.strip() == "V"
    problem_sfilepath = os.path.basename(problem_filepath)
    solver_sfilepath = solver_filepath.split("/")[1]

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
            if best_time == None or data[problem][solver] < best_time:
                best_time = data[problem][solver]
                best_solver = solver

        bests[problem][best_solver] = best_time

    return bests



if __name__ == "__main__":
    data = dict()
    for line in fileinput.input():
        add_data_from_line(line, data)

    #pprint.pprint(data)
    pprint.pprint(best_times(data))

