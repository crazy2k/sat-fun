import re
import subprocess
import threading
import time

SOLVERS = [
    "../local/sat-solvers/SAT_Competition_2014_Lingeling/code/binary/lingeling",
    "../local/sat-solvers/SAT_Competition_2014_Lingeling_druplig/code/binary/lingeling",
    # "../local/sat-solvers/SAT_Competition_2014_BFS-Glucose/code/binary/BFSglucose",
    # "../local/sat-solvers/SAT_Competition_2014_Riss/code/binary/riss",
    # "../local/sat-solvers/SAT_Competition_2014_SWDiA5BY/code/binary/SWDiA5BY_static"
]

FAMILY_FILEPATHS = [
    ("../local/nrosner-cnf/bonnie.exp.dc.uba.ar/~nrosner/cnf/avl_HeightBound/avl_hbnd-s%02d.als.cnf", range(2, 16)),
    ("../local/nrosner-cnf/bonnie.exp.dc.uba.ar/~nrosner/cnf/chord_FindSuccWorks/chordbug-s%02d.als.cnf", range(4, 11)),
    ("../local/nrosner-cnf/bonnie.exp.dc.uba.ar/~nrosner/cnf/markSweepGC_Completeness/markgcp_compl-s%02d.als.cnf", range(4, 16)),
    ("../local/nrosner-cnf/bonnie.exp.dc.uba.ar/~nrosner/cnf/originalBinTreeEquivalence/obt-s%02d.als.cnf", range(4, 16)),
    ("../local/nrosner-cnf/bonnie.exp.dc.uba.ar/~nrosner/cnf/singlyLinkedLists_3DefsCircularEquiv/sll_AcEq_Circular_QConn_Exactly-s%02d.als.cnf", range(12, 21)),
    ("../local/nrosner-cnf/bonnie.exp.dc.uba.ar/~nrosner/cnf/stableMutexRing_Closure/stableMutexRing-s10.als.cnf", range(10, 19))
]

TIMEOUT = 5*60*60   # 5 hours

def solve_family(family_filepath, solver_filepath):
    family_filepath_tpl, family_range = family_filepath
    for i in family_range:
        problem_filepath = family_filepath_tpl % i
        timed_out, delta_perf, delta_time, valid = solve_problem(problem_filepath,
                                                solver_filepath)

        timed_out_s = "TO" if timed_out else "!TO"
        valid_s = "V" if valid else "!V"

        print("%s | %f | %f | %s | %s | %s" %
              (problem_filepath, delta_perf, delta_time, solver_filepath,
               timed_out_s, valid_s))

        # Don't try with bigger instances if timed out
        if timed_out:
            return

def solve_problem(problem_filepath, solver_filepath):
    problem_file = open(problem_filepath)

    # We calculate time in different ways, just in case
    t1_time = time.time()
    t1_perf = time.perf_counter()
    output, timed_out = run_solver(solver_filepath, problem_file, TIMEOUT)
    t2_perf = time.perf_counter()
    t2_time = time.time()

    delta_perf = t2_perf - t1_perf
    delta_time = t2_time - t1_time
    output = output.decode("UTF-8") if not timed_out else output

    # A basic validity check of the output
    valid = False
    if not timed_out:
        solution_pattern = re.compile("s (SATISFIABLE|UNSATISFIABLE)$")
        solution_lines = [line for line in output.splitlines()
                          if solution_pattern.match(str(line))]
        valid = len(solution_lines) == 1

    return timed_out, delta_perf, delta_time, valid

def run_solver(solver_filepath, problem_file, timeout):
    output = None
    timed_out = False
    try:
        output = subprocess.check_output([solver_filepath],
                                         stdin=problem_file,
                                         timeout=TIMEOUT)
    except subprocess.CalledProcessError as e:
        # Solvers may return non-zero exit codes even when all is good
        output = e.output
    except subprocess.TimeoutExpired as e:
        timed_out = True

    return output, timed_out

if __name__ == "__main__":
    for family_filepath in FAMILY_FILEPATHS:
        for solver_filepath in SOLVERS:
            solve_family(family_filepath, solver_filepath)

