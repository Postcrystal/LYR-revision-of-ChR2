# LYR-revision-of-ChR2  

This script could edit the torsion angel of LYR in ChR2(pdb)

## Premise
To start with, please make you ChR2 protein become a monomer with tools like VMD or YASARA etc. Secondly, put your PDB file into Gaussian View or other softwares to edit the dihedral C13-C16 (All-Trans). Thirdly, choose an appropriate angel of torsion of LYR. Lastly, generate the relative PDB file.

## Instruction
1. Dowdload convert.py and LYR_coor_change.sh into your computer.

2. sh LYR_coor_change.sh torsion_structure.pdb angle(recommended) initial_structure.pdb

3. You will get the edited initial structure coordinates with a torsion angle.

4. Replace the results for initial structure PDB file.

example:
sh LYR_coor_change.sh 6eid_monomer_149.pdb for_cut_149 6eid_monomer.pdb
Results(partial):

## Contact
If you any question, you could send emails to 282869443@qq.com
