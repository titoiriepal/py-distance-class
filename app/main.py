class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers"

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance") -> "Distance":
        return Distance(self.km + other.km)


distance = Distance(5)
distance2 = Distance(10)
distance3 = distance + distance2
print(distance3)
