"""
Модуль organism.py
Базовые классы организмов: растения, травоядные, хищники.
"""


class Organism:
    """Базовый организм, обладающий именем и энергией."""

    def __init__(self, name: str, energy: float) -> None:
        self.name = name
        self.energy = energy

    def eat(self, food_energy: float) -> None:
        """Потребление пищи, увеличивающее энергию."""
        self.energy += food_energy
        print(f"{self.name} съел {food_energy} энергии.")

    def is_alive(self) -> bool:
        """Проверка жизнеспособности (энергия > 0)."""
        return self.energy > 0

    def __str__(self) -> str:
        return f"{self.name}(энергия={self.energy})"


class Plant(Organism):
    """Растение: восстанавливает энергию с помощью фотосинтеза."""

    def photosynthesize(self) -> None:
        """Получение энергии от солнца."""
        self.eat(5)
        print(f"{self.name} фотосинтезирует.")


class Herbivore(Organism):
    """Травоядное: питается растениями."""

    def eat_plant(self, plant: Plant) -> None:
        """Съесть растение, забрав его энергию (но не более 15)."""
        if not plant.is_alive():
            print(f"{plant.name} уже мёртв.")
            return
        eaten_energy = min(plant.energy, 15)
        plant.energy -= eaten_energy
        self.eat(eaten_energy)
        print(f"{self.name} съел растение {plant.name}.")


class Carnivore(Organism):
    """Хищник: охотится на травоядных."""

    def hunt(self, prey: Herbivore) -> None:
        """Охота на травоядное. Успех, если энергия хищника больше."""
        if not prey.is_alive():
            print(f"{prey.name} уже мёртв.")
            return
        if self.energy > prey.energy:
            eaten_energy = prey.energy
            prey.energy = 0
            self.eat(eaten_energy)
            print(f"{self.name} поймал {prey.name}!")
        else:
            print(f"{prey.name} убежал от {self.name}.")