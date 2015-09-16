import re
import subprocess
import threading
import time

SOLVERS = [
    "sat-solvers/SAT_Competition_2014_Lingeling/code/binary/lingeling",
    "sat-solvers/SAT_Competition_2014_Lingeling_druplig/code/binary/lingeling",
    # "sat-solvers/SAT_Competition_2014_BFS-Glucose/code/binary/BFSglucose",
    # "sat-solvers/SAT_Competition_2014_Riss/code/binary/riss",
    # "sat-solvers/SAT_Competition_2014_SWDiA5BY/code/binary/SWDiA5BY_static"
]

FAMILY_FILEPATHS = [
    ("nrosner-cnf/bonnie.exp.dc.uba.ar/~nrosner/cnf/avl_HeightBound/avl_hbnd-s%02d.als.cnf", range(2, 16)),
    ("nrosner-cnf/bonnie.exp.dc.uba.ar/~nrosner/cnf/chord_FindSuccWorks/chordbug-s%02d.als.cnf", range(4, 11)),
    ("nrosner-cnf/bonnie.exp.dc.uba.ar/~nrosner/cnf/markSweepGC_Completeness/markgcp_compl-s%02d.als.cnf", range(4, 16)),
    ("nrosner-cnf/bonnie.exp.dc.uba.ar/~nrosner/cnf/originalBinTreeEquivalence/obt-s%02d.als.cnf", range(4, 16)),
    ("nrosner-cnf/bonnie.exp.dc.uba.ar/~nrosner/cnf/singlyLinkedLists_3DefsCircularEquiv/sll_AcEq_Circular_QConn_Exactly-s%02d.als.cnf", range(12, 21)),
    ("nrosner-cnf/bonnie.exp.dc.uba.ar/~nrosner/cnf/stableMutexRing_Closure/stableMutexRing-s10.als.cnf", range(10, 19))
]

TIMEOUT = 5*60*60   # 5 hours

def solve_family(family_filepath, solver_filepath):
    family_filepath_tpl, family_range = family_filepath
    for i in family_range:
        problem_filepath = family_filepath_tpl % i
        timed_out, delta, valid = solve_problem(problem_filepath,
                                                solver_filepath)

        timed_out_s = "TO" if timed_out else "!TO"
        valid_s = "V" if valid else "!V"

        print("%s | %f | %s | %s | %s" %
              (problem_filepath, delta, solver_filepath, timed_out_s, valid_s))

        # Don't try with bigger instances if timed out
        if timed_out:
            return

def solve_problem(problem_filepath, solver_filepath):
    problem_file = open(problem_filepath)

    t1 = time.clock()
    output, timed_out = run_solver(solver_filepath, problem_file, TIMEOUT)
    t2 = time.clock()

    delta = t2 - t1
    output = output.decode("UTF-8") if not timed_out else output

    # A basic validity check of the output
    valid = False
    if not timed_out:
        solution_pattern = re.compile("s (SATISFIABLE|UNSATISFIABLE)$")
        solution_lines = [line for line in output.splitlines()
                          if solution_pattern.match(str(line))]
        valid = len(solution_lines) == 1

    return timed_out, delta, valid

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

