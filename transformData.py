dir = './data/'
float = {'neutral': 0, 'positive': 0, 'mixed':0, 'negative': 0}

f = open(dir + 'training.txt')
index = 0
for line in f:
	index +=1
	line = line.rstrip('\n')
	ele = line.partition('@@')
	tag = ele[2].strip('"@ ')
	if ( float.get(tag) ):
		tmpf = open(dir + tag + '/file' + str(float[tag]), 'w')
		float[tag]+=1
		#print "first: ", ele[0], " ******** ", ele[2]
		tmpf.write(ele[0])
		tmpf.close()
	else:
		print "Oops: " , index
		
	
	