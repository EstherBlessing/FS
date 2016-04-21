import numpy as np
import re


name1 = '/home/blesse01/BIOM/procUCSF/fMRI/fMRI/PTB201008-1/funct/rp_aPTB201008-1_0005'

def get_filename(string):

    filename = re.findall(r'/home/blesse01/BIOM/procUCSF/fMRI/fMRI/(PTB.*)\-1/', string)[0]

    return filename

print get_filename(name1)

def get_motion(filepath):

    # Open the file
    data = open(filepath,'r')
    
    out = []
    # Look through the data, one line at a time. Note that each line is the 
    # head movement values (first three are translations, second three are 
    # rotations in radians).
    for line in data:
	# Split line into list of strings.
	string_list = line.split()

	# Convert list of strings to floats.
	num_list = []
	for element in string_list:
		num_list.append(float(element))
		
	# Convert list to numpy array so we can math, 
	# get last three numbers (rotations in radians) and multiply by 
        # 50 mm to convert to mm
	# add these three numbers together to get total rotational displacement.
	array = np.array(num_list)
	abs_array = np.abs(array)
	arrayrad = abs_array[3:]
	mul = arrayrad * 50
	rad_sum = mul.sum()

	# get first three numbers (mm translation displacements) and add together
	arraytrans = abs_array[0:3]
	trans_sum = arraytrans.sum()

	# add the sums of the rotations and translations together
	final_sum = rad_sum + trans_sum
	
	#append each final sum to one array called out
	out.append(final_sum)


    #Get the maximum displacement over all volumes to return as the function output
    #together with the filename
    # first turn out from a list to an array
    out_array=np.array(out) 
    maxdisplacement = max(out_array)
    filename = get_filename(name1)
    out = (filename, maxdisplacement)

    # Print out a two column matrix where each row is a volume num and 
    # corresponding max displacement (this is to look at for quality control 
    # purposes

    volume_num = len(out_array)
    out_column=out_array.reshape(volume_num,1)
    volume_list=list(range(volume_num))
    volume_list_array=np.array(volume_list)
    volume_column=volume_list_array.reshape(volume_num,1)

    #jpvelez, how do I get these two columns (out_column and volume_column) 
    #to print out  side by side in a 2 column array where each row is volume number  
    #and cooresponding total displacement??

    print out_column
    print volume_column
    print out
    #print ????
    return out
	
get_motion("/home/blesse01/BIOM/procUCSF/fMRI/fMRI/PTB201008-1/funct/rp_aPTB201008-1_0005.txt")


