I attached inter-subunit PCS data for CTD. However, we should be careful with these data since they’re all within 0.05 ppm (close to the “intrinsic” errors of PCS data due to 1H residual CSA). Fortunately, some residues still show sizeable PCSs (resi 176-181, 189,193) which should be reliable. The most valuable inter-subunit PCSs arise from the protons (HZ2 and HE1) in indole ring of W184. I attached one excel file (Exp_inter_HZ2 corresponds to 19F PCS value) including PCS data for Trp184.
 
For now, I’m not sure if it’s worth the time using inter-subunit PCS for your restrained MD. I wish I used a more “powerful” PCS tag, e.g., lanthanide then I will have more sizeable inter-subunit PCS data and in this case , it will definitely benefit your MD simulation.

I attached my data files (*.npc), first is GB1_NTA cobalt and the second is intra-subunit PCSs for CTD. The 1-3 columns are residue index, observed nucleus and observed PCS values, respectively. The fourth column is the experimental error and it’s set 0.
I have five parameters, I’ll list them below:
For dHis GB1_NTA_cobalt (use 2QMT structure): delta-chi,ax=-6.342; delta-chi,rh=-1.411; phi=60.42, theta=75.172, omega =107.84.
For CTD (use 4IPY): delta-chi,ax=-4.462; delta-chi,rh=-0.908; phi=41.261, theta=95.419, omega =85.478
 
But they may have different “definitions” in Paramagpy (Numbat) from that in Amber.
# calc_ca_pcs
