"""EX08 - Linked Lists!"""

from __future__ import annotations 

__author__ = "730661469"


class Node: 
    """Class to create Node of linked list."""
    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        """Initialize new Node object."""
        self.value = val
        self.next = next

    def __str__(self) -> str:
        """Magic method to convert Node to printable string."""
        if self is None:
            return "None"
        else:
            rest: str = str(self.next)
            return f"{self.value} -> {rest}"


def value_at(head: Node | None, index: int) -> int:
    """Return value of Node stored at given index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0: 
        return head.value 
    return value_at(head.next, index - 1) # recursive call


def max(head: Node | None) -> int:
    """Return int value of max value Node in linked list."""
    if head is None: 
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.value
    next_max = max(head.next) # recursive call 
    if head.value > next_max:
        next_max = head.value
    return next_max    
    

def linkify(items: list[int]) -> Node | None:
    """Slice list of integers and link together in linked list."""
    if len(items) == 0:
        return None
    return Node(items[0], linkify(items[1:])) # recursive call
    

def scale(head: Node | None, factor: int) -> Node | None:
    """For every Node in linked list, multiply Node value by factor."""
    if head is None:
        return None
    if head.next is None:
        return Node(head.value * factor, None)
    return Node(head.value * factor, scale(head.next, factor)) # recursive call 
