import re
import subprocess
import glob
import time

SOLVERS = [
    "sat-solvers/SAT_Competition_2014_Lingeling/code/binary/lingeling",
    "sat-solvers/SAT_Competition_2014_Lingeling_druplig/code/binary/lingeling",
    "sat-solvers/SAT_Competition_2014_BFS-Glucose/code/binary/BFSglucose",
    "sat-solvers/SAT_Competition_2014_Riss/code/binary/riss",
    "sat-solvers/SAT_Competition_2014_SWDiA5BY/code/binary/SWDiA5BY_static"
]

PROBLEMS = glob.glob("nrosner-cnf/bonnie.exp.dc.uba.ar/~nrosner/cnf/*/*.cnf")

if __name__ == "__main__":
    for problem_filepath in PROBLEMS:
        for solver_filepath in SOLVERS:
            problem_file = open(problem_filepath)

            t1 = time.clock()
            try:
                output = subprocess.check_output([solver_filepath],
                                                 stdin=problem_file)
            except subprocess.CalledProcessError as e:
                # Solvers may return non-zero exit codes even when all is good
                output = e.output

            t2 = time.clock()

            solution_pattern = re.compile("s (SATISFIABLE|UNSATISFIABLE)$")
            solution_lines = [line for line in output.split("\n")
                              if solution_pattern.match(line)]

            print "%s | %f | %s | %d" % \
                  (problem_filepath, t2 - t1, solver_filepath,
                   len(solution_lines))
