class Dog:
    def __init__(self, health_points, weight, attack_power, speed, defense, x=0, y=0):
        self.health_points = health_points
        self.weight = weight
        self.attack_power = attack_power
        self.speed = speed
        self.defense = defense
        self.x = x
        self.y = y

    def is_alive(self):
        return self.health_points > 0

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.health_points -= actual_damage
        if self.health_points < 0:
            self.health_points = 0

    def attack(self, target):
        if self.is_alive():
            target.take_damage(self.attack_power)

    def __str__(self):
        return f"Dog(HP: {self.health_points}, Weight: {self.weight}, Attack: {self.attack_power}, Speed: {self.speed}, Defense: {self.defense}, Pos: ({self.x}, {self.y}))"

    def __repr__(self):
        return f"Dog(health_points={self.health_points}, weight={self.weight}, attack_power={self.attack_power}, speed={self.speed}, defense={self.defense}, x={self.x}, y={self.y})"


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = {}

    def is_valid_position(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def is_position_occupied(self, x, y):
        return (x, y) in self.grid

    def add_dog(self, dog, x, y):
        if not self.is_valid_position(x, y):
            raise ValueError(f"Position ({x}, {y}) is out of bounds")
        if self.is_position_occupied(x, y):
            raise ValueError(f"Position ({x}, {y}) is already occupied")
        self.grid[(x, y)] = dog
        dog.x = x
        dog.y = y

    def remove_dog(self, x, y):
        if not self.is_position_occupied(x, y):
            raise ValueError(f"No dog at position ({x}, {y})")
        dog = self.grid.pop((x, y))
        return dog

    def move_dog(self, from_x, from_y, to_x, to_y):
        if not self.is_valid_position(to_x, to_y):
            raise ValueError(f"Position ({to_x}, {to_y}) is out of bounds")
        if not self.is_position_occupied(from_x, from_y):
            raise ValueError(f"No dog at position ({from_x}, {from_y})")
        if self.is_position_occupied(to_x, to_y):
            raise ValueError(f"Position ({to_x}, {to_y}) is already occupied")
        dog = self.grid.pop((from_x, from_y))
        self.grid[(to_x, to_y)] = dog
        dog.x = to_x
        dog.y = to_y

    def get_dog_at(self, x, y):
        return self.grid.get((x, y))

    def get_all_dogs(self):
        return list(self.grid.values())

    def __str__(self):
        return f"Grid({self.width}x{self.height}, {len(self.grid)} dogs)"

    def __repr__(self):
        return f"Grid(width={self.width}, height={self.height}, dogs={len(self.grid)})"
