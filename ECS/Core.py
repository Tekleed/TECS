Current_Entity: int = 0

def Entity() -> int:
    global Current_Entity
    Current_Entity += 1
    return Current_Entity

def Add(Entity: int, Component: str) -> ...:
    ...

def Get(Entity: int, Component: str) -> ...:
    ...


