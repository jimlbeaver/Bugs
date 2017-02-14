import transforms3d.euler as E
import transforms3d.affines as AFF
import numpy as np

R90 = np.deg2rad(90)
T = [0, 0, 0]
R = E.euler2mat( R90, 0, 0)
Z = [1, 1, 1]

bug = AFF.compose( T, R, Z )
print('Bug Pos\n', bug.astype(int))

bug2pgxform = [[1,0,0,0], [0,-1,0,0], [0,0,-1,0], [0,0,0,1]] #reflect across xy plane

pgbug = np.matmul(bug2pgxform, bug)

print('PGBug Pos\n', pgbug.astype(int))
