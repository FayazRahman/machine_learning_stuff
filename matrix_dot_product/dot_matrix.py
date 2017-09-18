def print_matrix(m):
	for r in m:
		print(r)

def check(m):
	return len(set(list(map(len, m)))) == 1

def read_matrices():
	with open('input.txt', 'r') as f:
		lines = f.readlines()
	M = [[]]
	for l in lines:
		l = l.strip()
		if len(l) == 0:
			if len(M[-1]) == 0:
				continue
			else:
				M.append([])
		else:
			if l[-1] =='\n':
				l = l[:-1]
			nums = [float(x) for x in l.split()]
			M[-1].append(nums)
	if len(M[-1]) == 0:
		M = M[:-1]
	for m in M:
		#print_matrix(m)
		if not check(m):
			raise Exception('Invalid data')
	return M

def shape(m):
	return len(m), len(m[0])

def dot(m1, m2):
	m, n = shape(m1)
	p, q = shape(m2)
	assert n == p, "Number of columns of Matrix 1 should equal number of columns of Matrix 2"
	m3 = [[0. for j in range(q)] for i in range(m)]
	for i in range(m):
		for j in range(q):
			for k in range(n):
				m3[i][j] += m1[i][k] * m2[k][j]
	return m3


def write_matrix(m):
	with open('output.txt', 'w') as f:
		for r in m:
			for x in r:
				f.write(str(x) + ' ')
			f.write('\n')


M = read_matrices()
assert len(M) == 2, 'Requires exactly 2 matrices for dot operation'
dot_prod = dot(*M)
print_matrix(dot_prod)
write_matrix(dot_prod)
