# Definitions

*Problem:* A boolean formula expressed in conjunctive normal form (CNF).
*Problem family:* A set of related problems that can be uniquely identified by a number representing their size. (*Vague definition!*)

# Goal

Answer the following two questions:

* Is it true that there’s no single solver that outperforms (in terms of speed) all other solvers for different problem families in the experiment? (In other words, is there a silver-bullet-solver?)
* Is it true that, for any problem family in the experiment, there exists some size $s_0$ such that the best solver is almost always the same for problems bigger than $s_0$? (In other words, can the knowledge of a solver performing good for some sizes help find the best solver for greater sizes of the problem?)

# Problem families

* `avl_hbnd`
* `chordbug`
* `markgcp_compl`
* `obt`
* `sll_AcEq_Circular_QConn_Exactly`

# Solvers

The ideas was to find state-of-the-art, comparable solvers, so five solvers that had good performances in 2014’s International SAT Competition were chosen. All solvers are sequential, for simplicity.

* `SAT_Competition_2014_Lingeling`
* `SAT_Competition_2014_BFS-Glucose`
* `SAT_Competition_2014_Lingeling_druplig`
* `SAT_Competition_2014_Riss`
* `SAT_Competition_2014_SWDiA5BY`

# Results

```
{'avl_hbnd-s02.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 853.0},
 'avl_hbnd-s03.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 822.0},
 'avl_hbnd-s04.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 716.0},
 'avl_hbnd-s05.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 658.0},
 'avl_hbnd-s06.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 718.0},
 'avl_hbnd-s07.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 771.0},
 'avl_hbnd-s08.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 712.0},
 'avl_hbnd-s09.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 715.0},
 'avl_hbnd-s10.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 723.0},
 'avl_hbnd-s11.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 708.0},
 'avl_hbnd-s12.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 689.0},
 'avl_hbnd-s13.als.cnf ': {None: None},
 'avl_hbnd-s14.als.cnf ': {None: None},
 'avl_hbnd-s15.als.cnf ': {None: None},
 'chordbug-s04.als.cnf ': {'SAT_Competition_2014_Riss': 548.0},
 'chordbug-s05.als.cnf ': {'SAT_Competition_2014_Riss': 697.0},
 'chordbug-s06.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 736.0},
 'chordbug-s07.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 707.0},
 'chordbug-s08.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 825.0},
 'chordbug-s09.als.cnf ': {None: None},
 'chordbug-s10.als.cnf ': {None: None},
 'markgcp_compl-s04.als.cnf ': {'SAT_Competition_2014_Riss': 713.0},
 'markgcp_compl-s05.als.cnf ': {'SAT_Competition_2014_Riss': 685.0},
 'markgcp_compl-s06.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 747.0},
 'markgcp_compl-s07.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 828.0},
 'markgcp_compl-s08.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 805.0},
 'markgcp_compl-s09.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 720.0},
 'markgcp_compl-s10.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 741.0},
 'markgcp_compl-s11.als.cnf ': {None: None},
 'markgcp_compl-s12.als.cnf ': {None: None},
 'markgcp_compl-s13.als.cnf ': {None: None},
 'markgcp_compl-s14.als.cnf ': {None: None},
 'markgcp_compl-s15.als.cnf ': {None: None},
 'obt-s04.als.cnf ': {'SAT_Competition_2014_Riss': 552.0},
 'obt-s05.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 695.0},
 'obt-s06.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 736.0},
 'obt-s07.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 794.0},
 'obt-s08.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 722.0},
 'obt-s09.als.cnf ': {'SAT_Competition_2014_Riss': 847.0},
 'obt-s10.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 766.0},
 'obt-s11.als.cnf ': {None: None},
 'obt-s12.als.cnf ': {None: None},
 'obt-s13.als.cnf ': {None: None},
 'obt-s14.als.cnf ': {None: None},
 'obt-s15.als.cnf ': {None: None},
 'sll_AcEq_Circular_QConn_Exactly-s12.als.cnf ': {'SAT_Competition_2014_Riss': 735.0},
 'sll_AcEq_Circular_QConn_Exactly-s13.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 825.0},
 'sll_AcEq_Circular_QConn_Exactly-s14.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 977.0},
 'sll_AcEq_Circular_QConn_Exactly-s15.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 1024.0},
 'sll_AcEq_Circular_QConn_Exactly-s16.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 992.0},
 'sll_AcEq_Circular_QConn_Exactly-s17.als.cnf ': {'SAT_Competition_2014_SWDiA5BY': 904.0},
 'sll_AcEq_Circular_QConn_Exactly-s18.als.cnf ': {None: None},
 'sll_AcEq_Circular_QConn_Exactly-s19.als.cnf ': {None: None},
 'sll_AcEq_Circular_QConn_Exactly-s20.als.cnf ': {None: None}}
```
