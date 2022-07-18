#!/bin/bash


for PDB in *.pdb ; do

    CMD="     parm m01_2kod_12A.prmtop \n"
    CMD="$CMD trajin $PDB \n"
    CMD="$CMD autoimage \n"
    CMD="$CMD trajout ai_$PDB pdb \n"
    CMD="$CMD run"

    echo -e "$CMD" > cpp.in
    cpptraj -i cpp.in > cpp.out

done
