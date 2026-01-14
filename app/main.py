class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers"

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km + other.km)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += other.km
        return self

    def __mul__(self, factor: int) -> Distance:
        return Distance(self.km * factor)

    def __truediv__(self, divisor: int) -> Distance:
        return Distance(round(self.km / divisor, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < other.km

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > other.km

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == other.km

    def __le__(self, other: Distance | int | float) -> bool:
        return self.km <= other.km

    def __ge__(self, other: Distance | int | float) -> bool:
        return self.km >= other.km


distance = Distance(30)
distance2 = Distance(23)
print(distance > distance2)  # True
