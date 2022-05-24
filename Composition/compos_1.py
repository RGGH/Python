from dataclasses import dataclass

@dataclass
class Employee:
    age: int
    name: str
    height: str


class Company:
    """Compostion Example"""

    def __init__(self, compname) -> None:
        self.compname = compname
        self.emp = Employee(33, "Bob", 170)

    def __str__(self):
        return f"{self.compname} - {self.emp}"


hp = Company("HP")
print(hp)
