from __future__ import annotations 

class Node: 
    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        self.value = val
        self.next = next

    def __str__(self) -> str:
        if self is None:
            return "None"
        else:
            rest: str = str(self.next)
            return f"{self.value} -> {rest}"
        
    def value_at(head: Node | None, index: int) -> int:
        raise IndexError("Index is out of bounds on the list.")
    
    def max(head: Node | None) -> int:
        raise ValueError("Cannot call max with None")
    
    def linkify(items: list[int]) -> Node | None:
        return None
    
    def scale(head: Node | None, factor: int) -> Node | None:
        return None


two: Node = Node(2, None)
one: Node = Node(1, two)