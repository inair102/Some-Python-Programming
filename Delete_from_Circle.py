import sys,ast
class Circle:
	def makeCircle(self,N,M,K):
		n = [1 for col in range(0,N)]
		nodesToDelete = N-K
		count=1
		printResult= '['
		while nodesToDelete>0:
			for i in range(0,N):
				if n[i]==1 and count==M and nodesToDelete>0:
					n[i]=0
					count=1
					nodesToDelete=nodesToDelete-1
				elif n[i]==1:
					count=count+1
		nodes=0
		for i in range(0,N):
			if n[i]==1 and nodes<K-1:
				printResult = printResult + str(i) + ','
				nodes=nodes+1
			elif n[i]==1:
				printResult = printResult + str(i) 

		return printResult + ']'

if __name__ == "__main__":
	c = Circle()
	N = ast.literal_eval(sys.argv[1])
	M = ast.literal_eval(sys.argv[2])
	K = ast.literal_eval(sys.argv[3])
	print "The last remaining numbers are", c.makeCircle(N,M,K)
