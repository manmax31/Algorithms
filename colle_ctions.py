import collections

# Counter
string = "Roger is Great. Roger plays great tennis"
counts = collections.Counter(string.split())
print(counts.most_common(5))
print(counts.elements())

# Default Dict
d = collections.defaultdict(int)
for s in string.split():
    d[s] += 1
print(d)

# DeQueue
q = collections.deque()
q.append(1)
q.appendleft(2)
q.append(2)
q.append(2)
q.extend([2,3])
print(q)
print(q.count(2))


# Named Tuple
point = collections.namedtuple('Point', ['x', 'y'])
p = point(10, 20)
print(p.x, p.y)

# Ordered Dict
od = collections.OrderedDict()
od['Roger'] = 1
od['Rafa'] = 2
od['Andy'] = 3
print(od)


