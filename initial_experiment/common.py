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
    ("../local/nrosner-cnf/bonnie.exp.dc.uba.ar/~nrosner/cnf/stableMutexRing_Closure/stableMutexRing-s%02d.als.cnf", range(10, 19))
]
