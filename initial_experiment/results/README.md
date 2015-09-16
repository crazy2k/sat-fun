# Definitions

* **Problem:** A boolean formula expressed in conjunctive normal form (CNF).
* **Problem family:** A set of related problems that can be uniquely identified
  by a number representing their size. (*Vague definition!*)

# Goal

Answer the following two questions:

* Is it true that there’s no single solver that outperforms (in terms of speed)
  all other solvers for different problem families in the experiment? (In other
  words, is there a silver-bullet-solver?)
* Is it true that, for any problem family in the experiment, there exists some
  size $s_0$ such that the best solver is almost always the same for problems
  bigger than $s_0$? (In other words, can the knowledge of a solver performing
  good for some sizes help find the best solver for greater sizes of the
  problem?)

# Problem families

* `avl_hbnd`
* `chordbug`
* `markgcp_compl`
* `obt`
* `sll_AcEq_Circular_QConn_Exactly`

# Solvers

The ideas was to use state-of-the-art, comparable solvers, so five solvers that
had good performances in 2014’s International SAT Competition were chosen. All
solvers are sequential, for simplicity.

* `SAT_Competition_2014_Lingeling`
* `SAT_Competition_2014_BFS-Glucose`
* `SAT_Competition_2014_Lingeling_druplig`
* `SAT_Competition_2014_Riss`
* `SAT_Competition_2014_SWDiA5BY`

# Results

The following shows, for each problem, which of the solvers performed best and
what was its time.