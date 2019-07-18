"""
All the algorithms for Project#4 - Computing
Alignments of Sequences
"""

def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    """
    The function computes a scoring matrix(a dictionary of dictionaries)
    whose entries are indexed by pairs of characters in alphabet plus '-' 
    The score for any entry indexed by one or more dashes is dash_score. 
    The score for the remaining diagonal entries is diag_score. Finally, 
    the score for the remaining off-diagonal entries is off_diag_score.

    Arguments:
        alphabet {set} -- a set of characters
        diag_score {integer} -- the diagnal score for the scoring matrix
        off_diag_score {integer} -- the off diagnal score
        dash_score {[type]} -- the score that includes atleast one dash
    
    Returns:
        a dictionary of dictionary -- the scoring matrix 
    """
    # initialize the scoring matrix
    scoring_matrix = {}
    # add the dash character to the set of alphabets
    all_chars = alphabet.union("-")

    # create a dictionary of dictionary for scores 
    for char_i in all_chars:
        scoring_matrix[char_i] = {}
        for char_j in all_chars:
            if (char_i == "-" or char_j == "-"):
                scoring_matrix[char_i][char_j] = dash_score            
            elif (char_i == char_j):
                scoring_matrix[char_i][char_j] = diag_score
            else:
                scoring_matrix[char_i][char_j] = off_diag_score


    return scoring_matrix

def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
    """
    Takes as input two sequences seq_x and seq_y whose elements share a common 
    alphabet with the scoring matrix scoring_matrix. The function computes and 
    returns the alignment matrix for seq_x and seq_y. If global_flag is True, 
    the global alignment matrix is computed. If global_flag is False, local 
    alignment matrix is computed

    For global alignment matrix S, each entry S[i][j] contains the maximum score 
    over every possible global alignment of the pair of sequences seq_x[0...i-1] and
    seq_y[0...j-1] 

    For local alignment matrix S, each entry entry S[i][j] contains the maximum score 
    over every possible alignment of the pair of sequences seq_x[0...i-1] and 
    seq_y[0...j-1] except for the case when  S[i][j] < 0, S[i][j]  is set to zero

    Arguments:
        seq_x {string} -- a string of alphabets whose elements share a common alphabet 
                          with scoring matrics
        seq_y {string} -- a string of alphabets whose elements share a common alphabet 
                          with scoring matrics
        scoring_matrix {a dictionary of dictionaries} -- the scoring matrix with each
                                                         alphabet plus '-' combination
                                                         scores
        global_flag {bolean -- flag to choose between global and local alignment
    
    Returns:
        list of lists -- an alignment matrix for seq_x and seq_y 
    """
    # let align_matrix = S. Then initialize S[0][0] = 0
    align_matrix = [[0]]

    # set the alignment matrix's column 0 to appropriate score either based on local or global
    # alignment selected
    for idx in range(1, len(seq_x) + 1):
        align_matrix.append([align_matrix[idx - 1][0] + scoring_matrix[seq_x[idx - 1]]["-"] ])
        if not global_flag and align_matrix[idx][0] < 0:
            align_matrix[idx][0] = 0

    # set the alignment matrix's row 0 to appropriate score either based on local or global
    # alignment selected
    for idx in range(1, len(seq_y) + 1):
        align_matrix[0].append(align_matrix[0][idx - 1] + scoring_matrix["-"][seq_y[idx - 1]])
        if not global_flag and align_matrix[0][idx] < 0:
            align_matrix[0][idx] = 0

    # set the remaining alignment matrix(S) values based on previous 3 values of S[i-1][j-1], S[i-1][j],
    # and S[i][j-1]
    for idx_x in range(1, len(seq_x) + 1):
        for idx_y in range(1, len(seq_y) + 1):
            val1 = align_matrix[idx_x - 1][idx_y - 1] + scoring_matrix[seq_x[idx_x - 1]][seq_y[idx_y - 1]]
            val2 = align_matrix[idx_x - 1][idx_y] + scoring_matrix[seq_x[idx_x - 1]]["-"]
            val3 = align_matrix[idx_x][idx_y - 1] + scoring_matrix["-"][seq_y[idx_y - 1]]
            align_matrix[idx_x].append(max(set([val1, val2, val3])))
            if not global_flag and align_matrix[idx_x][idx_y] < 0:
                align_matrix[idx_x][idx_y] = 0

    return align_matrix

def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    Takes as input two sequences seq_x and seq_y whose elements share a common alphabet
    with the scoring matrix scoring_matrix. This function computes a global alignment of
    seq_x and seq_y using the global alignment matrix alignment_matrix. The function returns
    a tuple of the form (score, align_x, align_y) where score is the score of the global 
    alignment align_x and align_y. Note that align_x and align_y should have the same 
    length and may include the padding character '-'.

    Arguments:
        seq_x {string} -- a string of alphabets
        seq_y {string} -- a string of alphabets
        scoring_matrix {dictionary of dictionaries} -- the scoring matrix
        alignment_matrix {list of lists} -- the global alignment matrix
    
    Returns:
        tuple -- returns (score, align_x, align_y) where score is the score of the global 
                 alignment align_x and align_y.
    """

    # intialize the indicies to the lengths of the sequences
    idx_x = len(seq_x)
    idx_y = len(seq_y)
    align_x = ""
    align_y = ""
    score = 0

    while (idx_x != 0 and idx_y != 0):
        if (alignment_matrix[idx_x][idx_y] == (alignment_matrix[idx_x - 1][idx_y - 1] 
            + scoring_matrix[seq_x[idx_x - 1]][seq_y[idx_y - 1]])):
            align_x = seq_x[idx_x - 1] + align_x
            align_y = seq_y[idx_y - 1] + align_y
            score += scoring_matrix[seq_x[idx_x - 1]][seq_y[idx_y - 1]]
            idx_x -= 1
            idx_y -= 1
        
        else:
            if (alignment_matrix[idx_x][idx_y] == (alignment_matrix[idx_x - 1][idx_y] 
                + scoring_matrix[seq_x[idx_x - 1]]["-"])):
                align_x = seq_x[idx_x - 1] + align_x
                align_y = "-" + align_y
                score += scoring_matrix[seq_x[idx_x - 1]]["-"]
                idx_x -= 1

            else:
                align_x = "-" + align_x
                align_y = seq_y[idx_y - 1] + align_y
                score += scoring_matrix["-"][seq_y[idx_y - 1]]
                idx_y -= 1
    
    while idx_x != 0:
        align_x = seq_x[idx_x - 1] + align_x
        align_y = "-" + align_y
        score += scoring_matrix[seq_x[idx_x - 1]]["-"]
        idx_x -= 1

    while idx_y != 0:
        align_x = "-" + align_x
        align_y = seq_y[idx_y - 1] + align_y
        score += scoring_matrix["-"][seq_y[idx_y - 1]]
        idx_y -= 1                
    

    return (score, align_x, align_y)

def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    Takes as input two sequences seq_x and seq_y whose elements share a common alphabet
    with the scoring matrix scoring_matrix. This function computes a local alignment of
    seq_x and seq_y using the local alignment matrix alignment_matrix. The function returns
    a tuple of the form (score, align_x, align_y) where score is the score of the local 
    alignment align_x and align_y. Note that align_x and align_y should have the same 
    length and may include the padding character '-'.

    Arguments:
        seq_x {string} -- a string of alphabets
        seq_y {string} -- a string of alphabets
        scoring_matrix {dictionary of dictionaries} -- the scoring matrix
        alignment_matrix {list of lists} -- the global alignment matrix
    
    Returns:
        tuple -- returns (score, align_x, align_y) where score is the score of the global 
                 alignment align_x and align_y.
    """
    
    # initialize the variables
    max_value = float("-inf")
    idx_x = -1
    idx_y = -1
    align_x = ""
    align_y = ""
    score = 0

    # find the location (row, col) of the maximum value in alignment_matrix
    for row in range(len(alignment_matrix)):
        for col in range(len(alignment_matrix[row])):
            if alignment_matrix[row][col] > max_value:
                max_value = alignment_matrix[row][col]
                idx_x = row
                idx_y = col

    while alignment_matrix[idx_x][idx_y] != 0 and idx_x != 0 and idx_y != 0:
        if (alignment_matrix[idx_x][idx_y] == (alignment_matrix[idx_x - 1][idx_y - 1] 
            + scoring_matrix[seq_x[idx_x - 1]][seq_y[idx_y - 1]])):
            align_x = seq_x[idx_x - 1] + align_x
            align_y = seq_y[idx_y - 1] + align_y
            score += scoring_matrix[seq_x[idx_x - 1]][seq_y[idx_y - 1]]
            idx_x -= 1
            idx_y -= 1
        
        else:
            if (alignment_matrix[idx_x][idx_y] == (alignment_matrix[idx_x - 1][idx_y] 
                + scoring_matrix[seq_x[idx_x - 1]]["-"])):
                align_x = seq_x[idx_x - 1] + align_x
                align_y = "-" + align_y
                score += scoring_matrix[seq_x[idx_x - 1]]["-"]
                idx_x -= 1

            else:
                align_x = "-" + align_x
                align_y = seq_y[idx_y - 1] + align_y
                score += scoring_matrix["-"][seq_y[idx_y - 1]]
                idx_y -= 1
             
    return (score, align_x, align_y)
