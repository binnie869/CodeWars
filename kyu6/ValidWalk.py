def isValidWalk(walk):
    walk_dict = {'u':0, 's':0}
    if len(walk)!=10:
    	return False
    else:
    	for step in walk:
        	if step == 'n':
        		walk_dict['u'] +=1
        	elif step == 's':
        		walk_dict['u'] -=1
        	elif step == 'e':
        		walk_dict['s'] +=1
        	else:
        		walk_dict['s'] -=1
    	if walk_dict['u'] == 0 and walk_dict['s'] == 0:
    		return True
    	else:
    		return False