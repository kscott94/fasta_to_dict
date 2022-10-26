def fasta_to_dict(fasta):
     """
     convert fasta file to a python dictionary
    :param fasta: path to fasta file
    :return: python dictionary
    """
    fasta_ids = []  # Initialize a list to be populated with fasta headers
    fasta_id_position = []   # Initialize a list to be populated with index positions of each fasta header
    fasta_seqs = []  # Initialize a list to be populated with fasta sequences
    with open(fasta, 'r') as file:
        id_index = 0  # We will keep track of the index position of each line as we parse the fasta file
        file = file.readlines()
        for line in file:
            if line[0] == '>':  # This is how we will identify if the line is a fasta header or sequence
                fasta_ids.append(line[1:].strip())  # If it is a header, then we will add it the fasta_ids list
                fasta_id_position.append(id_index)  # and its position to the fasta_id_pos list
                id_index += 1  # After this line is processed we will move to the next line in the fasta file
            else:
                id_index += 1 # After this line is processed we will move to the next line in the fasta file

        # This next part is super tricky.

        # First, I need to add an additional value (the length of the fasta file) to the fasta_id_pos list in order for
        # the next for-loop to move to the end of the fasta file without the index going out of range.
        fasta_id_position.append(len(file))

        # Now I am calculating the index positions between each header position, which contain fasta sequences
        # that correspond to the previous fasta header.
        for i in range(len(fasta_id_position)-1):  # For every fasta header, I need to find its corresponding sequence
            pos = fasta_id_position[i]  # We are starting at line 1 (not zero), because that is where the first sequence should be
            seq_position_ls = [j for j in range(pos+1,fasta_id_position[i+1])]  # making a list that contains all index positions with sequences for this header
            seq = ''    # Here is where I will put the fasta sequence when I find it

            # we will now find the lines at the know index positions that contain the sequences for this header, and
            # concatenate those lines to the variable, seq
            for k in seq_position_ls:
                seq += file[k].replace("\n", "")
            # I can now add this fasta sequence to the fasta_seq list.
            fasta_seqs.append(seq)
    # I have two lists, one with hte fasta header and the other with the fasta sequence.
    # These two lists are ordered so that each list position is paired. I will zip those lists together
    # and convert it to a dictionary. This dictionary will be the returned output of this function.
    fasta_dict = dict(zip(fasta_ids, fasta_seqs))
    return fasta_dict
