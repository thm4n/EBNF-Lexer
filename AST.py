from enum import Enum

class ASTNodeTypes(Enum):
	NonTerminal = "NoneTerminal"
	Terminal    = "Terminal"
	Optional    = "Optional"
	Sequence    = "Sequence"
	Choice      = "Choice"
	Rep         = "Rep"

class AST:
	def __init__(self):
		self.root = None

class __ASTNode:
	def __init__(self, node_type: ASTNodeTypes):
		self.node_type = node_type
		self.children = []

class TerminalNode(__ASTNode):
	def __init__(self, value: str):
		super().__init__(ASTNodeTypes.Terminal)
		self.value = value

class NonTerminalNode(__ASTNode):
	def __init__(self, name: str):
		super().__init__(ASTNodeTypes.NonTerminal)
		self.name = name

class SeqNode(__ASTNode):
	def __init__(self):
		super().__init__(ASTNodeTypes.Sequence)

class ChoiceNode(__ASTNode):
	def __init__(self):
		super().__init__(ASTNodeTypes.Choice)

class RepNode(__ASTNode):
	def __init__(self):
		super().__init__(ASTNodeTypes.Rep)

class OptionalNode(__ASTNode):
	def __init__(self):
		super().__init__(ASTNodeTypes.Optional)
