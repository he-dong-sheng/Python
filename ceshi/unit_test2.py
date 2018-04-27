# coding:utf8
import unittest

class Test(unittest.TestCase):
	def testMinus(self):
		u'''这里是减法测试'''
		result = 6-5 #实际结果
		hope = 1 	 #期望结果
		self.assertEqual(result,hope)

	def testDivide(self):
		u'''这里是除法测试'''
		result = 7.0/2
		hope = 3.5
		self.assertEqual(result,hope)

if __name__ == '__main__':
	unittest.main()