class Dog:
    def __init__(self, health_points, weight, attack_power, speed, defense):
        self.health_points = health_points
        self.weight = weight
        self.attack_power = attack_power
        self.speed = speed
        self.defense = defense

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
        return f"Dog(HP: {self.health_points}, Weight: {self.weight}, Attack: {self.attack_power}, Speed: {self.speed}, Defense: {self.defense})"

    def __repr__(self):
        return f"Dog(health_points={self.health_points}, weight={self.weight}, attack_power={self.attack_power}, speed={self.speed}, defense={self.defense})"
