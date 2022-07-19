"""
Plot a 3D scatter plot of: 
    X = Helical Angle (°)
    Y = RMSD to Xtal (Å)
    Z = Q-factor to HIV-1 CA CTD D1 (or PCS value of HE1/HZ2)
"""

import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import true

def plot_3d(z, zlabel=None, savefig=None, ax=None, vmin=0.02, vmax=0.20, filter=False):
    """
    3d plot with x as angle and y as xtal rmsd.
    """
    if ax is None:
        ax = plt.gca()

    # import datasets
    angle = np.loadtxt("4-500agg/1-75_39_c2_angle.dat")[:,1]
    rmsd = np.loadtxt("4-500agg/rms_bb_xtal.dat")[:,1]

    # all three datasets
    xyz = np.vstack((angle, rmsd, z))
    xyz = np.rot90(xyz, 1)

    # only show data between vmin and vmax
    if filter is True:
        filter_arr = []
        for i in xyz:
            if i[2] < vmin or i[2] > vmax:
                filter_arr.append(False)
            else:
                filter_arr.append(True)
        # run filter on xyz
        xyz = xyz[filter_arr]
        scat = ax.scatter(xyz[:,0], xyz[:,1], c=xyz[:,2], s=1.5, vmin=0.02, vmax=0.2)
    else:
        scat = ax.scatter(xyz[:,0], xyz[:,1], c=xyz[:,2], s=1.5, vmin=vmin, vmax=vmax)

    ax.set_xlabel("Angle")
    ax.set_ylabel("RMSD to Xtal ($\AA$)")
    ax.set_title(zlabel)
    #cbar = plt.colorbar(scat)
    #cbar.set_label(zlabel)

    if savefig:
        plt.savefig(savefig, dpi=300, transparant=True)

    return scat

qfs = np.loadtxt("4-500agg/qfs.txt")
pcs = np.loadtxt("4-500agg/back_pcs.txt")
he1 = pcs[:,0]
hz2 = pcs[:,1]

fig, ax = plt.subplots(nrows=3, ncols=2, sharex=True, sharey=True, figsize=(9,6))
#plot_3d(qfs, "Q-factors (CTD D1)")

# All
scat1 = plot_3d(he1, "HE1", ax=ax[0,0])
scat2 = plot_3d(hz2, "HZ2", ax=ax[0,1])

# D1 only
plot_3d(he1, "HE1 (D1) PCS=0.145", ax=ax[1,0], vmin=0.12, vmax=0.125, filter=True)
plot_3d(hz2, "HZ2 (D1) PCS=0.199", ax=ax[1,1], vmin=0.18, vmax=0.22, filter=True)

# D2 only
plot_3d(he1, "HE1 (D2) PCS=0.210", ax=ax[2,0], vmin=0.14, vmax=0.23, filter=True)
plot_3d(hz2, "HZ2 (D2) PCS=0.184", ax=ax[2,1], vmin=0.165, vmax=0.25, filter=True)

cbar = plt.colorbar(scat1)
cbar.set_label("PCS")

#                       D1:     D2:
# Exp_intra+inter_HE1   0.145	0.21
# Exp_intra+inter_HZ2	0.199	0.184

fig.tight_layout()

fig.savefig("back_pcs_compare.png", dpi=300, transparent=True)
plt.show()