from treelib import Tree

cmds = ["ls", "cd"]
specIds = ["/", ".."]
class Token:
    def __init__(self, tokenStr):
        self.value = tokenStr
        self.type = Token.getTokenType(tokenStr)
    
    @staticmethod
    def getTokenType(tokenStr):
        if(tokenStr == "$"):
            return "cmdstart"
        elif(tokenStr.isdigit()):
            return "num"
        elif(tokenStr == "dir"):
            return "dirid"
        elif(tokenStr in cmds):
            return "cmd"
        elif(tokenStr in specIds):
            return "specid"
        else:
            return "id"

def navigate(currPath, token):
    results = {}

    if(token.type == "specid" and token.value != "/"):
        results["path"] = currPath[:currPath.rfind("/")]
        results["node"] = tree.get_node(currNode.bpointer)
    elif(token.type == "specid"):
        results["path"] = "/"
        results["node"] = tree.get_node("/")
    else:
        path = f"{currPath}/{token.value}"
        results["path"] = path
        results["node"] = tree.get_node(path)

    return results

lines = [line.strip() for line in open("..\input.txt", "r")]

tree = Tree()
tree.create_node("/", "/", data={ "type": "dir", "size": 0 })
currNode = tree.get_node("/")
currPath = "/"

idx = -1
while idx < len(lines) - 1:
    idx = idx + 1
    line = lines[idx]
    tokens = [Token(t) for t in line.split(" ")]
    if tokens[1].value == "cd":
        results = navigate(currPath, tokens[2])
        currPath = results["path"]
        currNode = results["node"]
        continue
    
    if tokens[0].type != "cmdstart":
        if tokens[0].type == "num":
            data = { "type": "file", "size": int(tokens[0].value) }
        else:
            data = { "type": "dir", "size": 0 }
        tree.create_node(tokens[1].value, f"{currPath}/{tokens[1].value}", currPath, data=data)
        backNode = currNode
        while(backNode.bpointer is not None):
            size = sum(x.data["size"] for x in tree.children(backNode.identifier))
            backNode.data["size"] = size
            backNode = tree.get_node(backNode.bpointer)

nodes = tree.filter_nodes(lambda x: x.data["type"] == "dir" and x.data["size"] < 100000)

numFiles = 0
sumBytes = 0
for node in nodes:
    print(f"processing node {node.identifier}, size: {node.data['size']}")
    numFiles = numFiles + 1
    sumBytes = sumBytes + node.data["size"]
print(f"found {numFiles} files totaling {sumBytes} bytes")