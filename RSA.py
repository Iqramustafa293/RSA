from fpylll import *
from hashlib import md5
import numpy as np
from numpy.linalg import linalg
from numpy.linalg import inv
import math

matrix = IntegerMatrix.from_matrix([[1,-3,7],[11,23,5],[19,13,2]])
print ("Matrix With Values: ")
print (matrix)
LLL.reduction(matrix)
print ("Matrix After Reduction: ")
print (matrix)
shortestvector = SVP.shortest_vector(matrix)
print ("Shortest Vector Matrix: ")
print (shortestvector)
result1 = GaussSieve(matrix, algorithm=2)()
print ("After Gauss Sieve Algo: ")
print (result1)
y = [11,23,5]
n = np.cross(result1, y)
[l,m,n]=n
print ("cross product of p' and q:", [l,m,n])
result2 = ([l,m,n])
magnitude = round(math.sqrt(sum(v**2 for v in result2)))
print ("Vector magnitude is of n is: ", magnitude)
vector1 = (result1)
magnitude1 = round(math.sqrt(sum(v**2 for v in vector1)))
print ("Vector magnitude  of x is: ", magnitude1)
vector2 = (y)
magnitude2 = round(math.sqrt(sum(v**2 for v in vector2)))
print ("Vector magnitude of y is: ", magnitude2)
sin_theta = magnitude/(magnitude1*magnitude2)
angle = round(np.degrees(np.arcsin(sin_theta)))
print ("angle is: ", angle)
totient = magnitude-1
totient = totient
print ("totient of magnitude n is:", totient)
y_x = m/l
theta=round(np.degrees(np.arctan(y_x)))
theta= int(theta)
print ("angle theta :", theta)
z_r = n/magnitude
phi = round(np.degrees(np.arccos(z_r)))
phi = int(phi)
print ("angle phi :", phi)
x_ct= np.cos(np.radians(theta))
print ("cos of theta=", x_ct)
x_st= np.sin(np.radians(theta))
print ("sin of theta=", x_st)
y_cp= np.cos(np.radians(phi))
print ("cos of phi=", y_cp)
y_sp= np.sin(np.radians(phi))
print ("sin of phi=", y_sp)
x1 = int (round(totient * x_ct * y_sp))
y2 = int(round(totient * x_st* y_sp))
z2 = int(round(totient* y_cp))
matrix2 = [x1, y2, z2]
print ("Current Matrix derived from totient using polar coordinates: ")
print (matrix2)
print('saad code')
matrix3 = IntegerMatrix.from_matrix([[l,m,n],[x1, y2, z2]])
print ("Matrix With Values: ")
print (matrix3)
LLL.reduction(matrix3)
print ("Matrix After Reduction: ")
print (matrix3)
shortestvector = SVP.shortest_vector(matrix3)
print ("shortest vector: ")
print (shortestvector)
result3 = GaussSieve(matrix3, algorithm=2)()
print ("After Gauss Sieve Algo, we get the e: ")
print (result3)
e=np.array((result1,result2,result3))
e1=e.transpose()
print ("Encryption_key =" , e1)
k=2
ke= k*e1
print ("multiplication with scalar =" , ke)
Inverse=inv(np.matrix(ke))
#Inverse= np.linalg.inv(ke)
print ("Inverse of ke =" , Inverse)
#d1=k*Inverse
#print "Decryption_key =" , d1
m = np.array([[1,2,3],[4,5,6],[7,8,9]])
print ("Msg to be encrypted =" , m)
encrypted_msg=np.dot(m, e1)
print ("encrypted_msg =" , encrypted_msg)
decrypted_msg = (encrypted_msg*k)
decrypted_ms =  np.dot(decrypted_msg,Inverse)
print ("decrypted_msg =" , decrypted_ms)
#print hashlib.black2b(b"Nobody inspects the spammish repetition", digest_size=9).hexdigest()
h = hashlib.md5()
m.update(b"Nobody inspects")
m.update(b" the spammish repetition")
print (m.digest())

