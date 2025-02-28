import argparse
def myopts():
	parser = argparse.ArgumentParser()
	parser.add_argument('-database', default='dataset/training/', help='Path to database (default inputs/database)')
	parser.add_argument('-query', default='dataset/testing/', help='Path to query (default inputs/query)')
	parser.add_argument('-branches', type=int, default=5, help='Number of Branches in Tree')
	parser.add_argument('-maxDepth', type=int, default=5, help='Number of Branches in Tree')
	return parser.parse_args()
