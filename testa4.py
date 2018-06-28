#IP Homework 4
#Surabhi S Nath- 2016271
#Akshat Singh- 2016128



import unittest
from a4 import *

class testpoint(unittest.TestCase):
	
	def testMatrixRank(self):
		self.assertEqual(MatrixRank([[0,0,0],[0,0,0],[0,0,0]]),0)
		self.assertEqual(MatrixRank([[1,2,3],[4,5,6],[7,8,9]]),2)
		self.assertEqual(MatrixRank([[2,2,2],[4,4,4],[3,4,3],[4,5,6]]),3)
		self.assertEqual(MatrixRank([[1,565,3548],[3645,65,24],[435,61,23]]),3)
		self.assertEqual(MatrixRank([[-1,2,3,4],[2,3,8,2],[-4,4,1,-2],[2,3,5,7]]),4)
		self.assertEqual(MatrixRank([[0,1,2],[0,5,0],[0,0,0],[0,8,0]]),2)

if __name__=='__main__':
	unittest.main()








