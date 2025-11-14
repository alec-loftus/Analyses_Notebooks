# build_loop.py
from modeller import environ, selection
from modeller.automodel import loopmodel

# --- USER SETTINGS ---
pdb_code = '5go9_scaffold'       # filename without .pdb
alignment_file = 'scaffold.ali'
target_name = 'target'
chain = 'B'
loop_start = 240             # first missing residue number
loop_end   = 242             # last missing residue number
# ----------------------

env = environ()

# Define loop modeller that refines only the missing region
class MyLoop(loopmodel):
    def select_loop_atoms(self):
        return selection(self.residue_range('%d:%s' % (loop_start, chain),
                                            '%d:%s' % (loop_end, chain)))

# Build the loop
a = MyLoop(env,
           alnfile=alignment_file,
           knowns=pdb_code,
           sequence=target_name)

a.starting_model = 1
a.ending_model   = 50        # build 50 models; increase if you want more sampling
a.loop.starting_model = 1
a.loop.ending_model   = 50

a.make()

