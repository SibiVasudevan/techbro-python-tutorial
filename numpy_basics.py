import numpy as np

basic_array = np.array([1,2,3]) # That's cute
chad_array = np.array([[1,2,3], [4,5,6]]) # Now we're talking multi-dimensional

sigma_zeros = np.zeros(5) # [0,0,0,0,0]
gigachad_ones = np.ones((3,4)) # 3x4 matrix of pure ones energy

a = np.array ([1,2,3])
b = np.array([4,5,6])

result = a*b # Element-wise multiplication go brr
print(result) #[4,10,18]
print(np.dot(a,b)) # OG dot product

chad_move = a*2 # Broadcasting - cause real devs don't write loops

array = np.arange(9) # [0,1,2,3,4,5,6,7,8]
matrix = array.reshape(3,3) # Matrix transformation: ACTIVATED

transposed = matrix.T # Flip the script entirely!

# Regular devs: Use loops
# 10x devs: Use boolean indexing
data = np.array([10,20,30,40,50,60])
chad_filter = data[data>30] #Instant filtering: [40,50,60]
mega_filter = data[(data>20) & (data<50)] # [30,40]

random_matrix = np.random.rand(3,3) # 3x3 matrix of pure randomness