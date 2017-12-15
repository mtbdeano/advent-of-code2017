from day7 import day7_find_root, Node


def test_day7_tree():
    Node.clear()
    dean = Node('dean', 195)
    kristen = Node('kristen', 125)
    kylie = Node('kylie', 135)
    hunter = Node('hunter', 110)
    carol = Node('carol', 150)
    dean.add_child('kylie')
    dean.add_child('hunter')
    carol.add_child('dean')
    carol.add_child('kristen')
    Node.link_up()
    assert kylie.parent() == 'dean'
    assert hunter.parent() == 'dean'
    assert dean.parent() == 'carol'
    assert kristen.parent() == 'carol'
    assert Node.find_roots() == ['carol']
    assert sorted(dean.kid_weights()) == sorted([110, 135])
    

def test_find_root():
    Node.clear()
    tree = '''pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)'''
    assert day7_find_root(tree) == ['tknk']
    assert Node.find_node('xhth').get_weight() == 57
    assert Node.find_node('qoyq').get_weight() == 66
    assert Node.find_node('ugml').get_weight() == 251
    assert Node.find_node('ugml').get_weight() == 251
    assert Node.find_node('tknk').get_weight() == 770
    extra = Node.find_node('tknk').find_extra()[0]
    print(extra)
    assert extra.weight == 68
    assert extra.bweight == -8
    assert extra.name == 'ugml'
    
    