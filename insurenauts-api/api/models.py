from pydantic import BaseModel


class UserAnswer(BaseModel):
    """Answer to a question"""

    question_id: str
    message: str


class InsurancePackage(BaseModel):
    """Insure package definition"""

    name: str
    price: int
    description: str
    covered_items: list[str]


class Option(BaseModel):
    """Option to answer a question"""

    id: int
    description: str
    price: int


class GeneratedQuestion(BaseModel):
    """Question that is sent to a user"""

    id: str
    question: str
    options: list[Option]


class RecommendationResult(BaseModel):
    """Product recommendations"""

    recommendations: list[str]


class EmailBody(BaseModel):
    """Email definition"""

    to: str
    subject: str
    message: str


class CompletionResult(BaseModel):
    """Information provided for agent once user completes game."""

    name: str
    email: str
    suggested_insurance_packages: list[str]
    relevant_attributes: list[str]



class Node(BaseModel):
    id: str = ""


class EventNode(Node):
    """Definition of Nodes for the Events"""

    insurance: str = ""
    costs: int = 0
    text: str = ""
    additional_information: str = ""
    next_node: type[Node] = Node()


class DoorNode(Node):
    """Definition of the DoorNodes."""
    
    options: list[type[Node]] = [Node()]
    text: str = ""


class ChapterNode(Node):
    """Definition of the Nodes of the buying phase and follow up story"""

    options: list[type[Node]] = [Node()]
    text: str = ""
    insurance: str = ""




class Story(Node):

    """Definition of the Basestory"""
    root_node: type[Node]

    def next(idx=None):
        if root_node.isinstance(EventNode):
            root_node = root_node.next_node
        else:
            root_node = root_node.options[idx]