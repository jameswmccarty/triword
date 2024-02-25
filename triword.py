# puzzle solver for https://triword.net/

from collections import Counter

def solve(puzz: str, size: int, ws: set[str]) -> str:
	counts = Counter()
	parts = puzz.lower().split("/")
	ws = { w for w in ws if len(w) in { size+len(p) for p in parts } }
	for w in ws:
		for p in parts:
			if len(p)+size == len(w):
				if w.endswith(p):
					counts[w[0:size]] += 1
				elif w.startswith(p):
					counts[w[-size:]] += 1
	return ' '.join(sorted( k for k,v in counts.items() if v >= 3 ))

if __name__ == "__main__":

	with open("./enable1.txt") as infile:
		ws = { word.lower().strip() for word in infile }

	print(solve("TUN/GON/IN",3,ws))

	print(solve("RLY/LIN/MIL",4,ws))
