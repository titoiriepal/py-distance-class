class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers"

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance") -> "Distance":
        return Distance(self.km + other.km)

    def __iadd__(self, other: "Distance") -> "Distance":
        self.km += other.km
        return self

    def __mul__(self, factor: int) -> "Distance":
        return Distance(self.km * factor)

    def __truediv__(self, divisor: int) -> "Distance":
        return Distance(round(self.km / divisor, 2))


distance = Distance(30)
distance2 = distance / 6
print(distance2)
