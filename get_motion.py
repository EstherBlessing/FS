import numpy as np
import csv
from re import findall

def get_subject_id(path):
    return findall(r'(PTB.*)-1', path)[0]

def row_to_numbers(row):
    num_list = []
    for element in row:
        num_list.append(float(element))
    return num_list

def find_displacement(volume):
    x, y, z, pitch, yaw, roll = row_to_numbers(volume)
    mm_rotations = (pitch * 50) + (yaw * 50) + (roll * 50)
    mm_translations = x + y + z
    displacement = mm_rotations + mm_translations
    return displacement

def get_max_displacement(subject_volumes):
    max_displacement = 0.0
    for line in subject_volumes:
        volume = line.split()
        displacement = find_displacement(volume)
        if displacement > max_displacement:
            max_displacement = displacement
    return max_displacement

def process_subject(filepath):
    subject_volumes = open(filepath,'r')
    subject_id = get_subject_id(filepath)
    max_displacement = get_max_displacement(subject_volumes) 
    return subject_id, max_displacement

def main():
    out_file = open('subject_max_displacements.csv', 'w')
    writer = csv.writer(out_file)
    writer.writerow(['subject_id', 'max_displacement'])
    # TODO: get this working with sys.stdin. you'll need to import sys
    # TODO: read through this code line by line and understand it. use the REPL
    # to do so.
    # TODO: figure out unix programs to find all relevant filepaths to pass
    # into the standard in of this program, something like ..
    # ls -R | grep 'blah' | python get_motion.py
    # Get "absolute path", not "relative paths": ls -R   fMRI/PTB123123/funct/PB.txt, /Users/blessing/fMRI/PTB123123/funct/PB.txt
    for path in ['/Users/estherblessing/code/data/rp_aPTB201299-1_0005.txt']:
        subject_id, max_displacement = process_subject(path)
        writer.writerow([subject_id, max_displacement])

main()

