@cmd.extend
def find_dsfpairs(chain):
    cmd.select("cys_sel", f"{chain} and CYS/SG and bound_to CYS/SG") #creates selection "cys_sel"

    disulfides=cmd.find_pairs("cys_sel", "cys_sel", 1, 1, 2.5) #returns a list of (model,index) tuples
    disulfidepairs=[[tuple[0][1], tuple[1][1]] for tuple in disulfides] #create a new list of tuples (second element of the first inner tuple of the tuple, second element of the second inner tuple of the tuple) for each tuple/element in the list "disulfides". 
    for pair in disulfidepairs: 
        pair.sort()
    disulfidepairs_dup_rm=[]
    [disulfidepairs_dup_rm.append(x) for x in disulfidepairs if x not in disulfidepairs_dup_rm] #removes pair duplicates

    disulfidepairs_resi=[]
    for pair in disulfidepairs_dup_rm:
        myspace = {"dsfpair": []}
        cmd.iterate(f"ID " + str(pair[0]), "dsfpair.append(resi)", space = myspace) 
        cmd.iterate(f"ID " + str(pair[1]), "dsfpair.append(resi)", space = myspace) # result: {"dsfpair":['resi1', 'resi2']}     
        tup = tuple(myspace["dsfpair"]) #result: tup = ('res1', 'res2')
        disulfidepairs_resi.append(tup) #appends the pair as a tuple into a list 
        
    return print("Residue pairs forming disulfide bonds:" + str(disulfidepairs_resi))
