"""
Модуль тестирования базовой логики экосистемы.
"""

from ecosystem import Ecosystem
from population import Population
from organism import Plant, Herbivore, Carnivore


def test_plant_photosynthesis() -> None:
    plant = Plant("Одуванчик", 5)
    plant.photosynthesize()
    assert plant.energy == 10, "Фотосинтез должен добавить 5 энергии"
    print("test_plant_photosynthesis passed")


def test_herbivore_eating() -> None:
    plant = Plant("Трава", 10)
    rabbit = Herbivore("Кролик", 5)
    rabbit.eat_plant(plant)
    assert rabbit.energy == 15, "Кролик должен получить 10 энергии"
    assert plant.energy == 0, "Растение полностью съедено"
    print("test_herbivore_eating passed")


def test_carnivore_hunt_success() -> None:
    rabbit = Herbivore("Кролик", 10)
    fox = Carnivore("Лиса", 20)
    fox.hunt(rabbit)
    assert not rabbit.is_alive(), "Кролик должен умереть"
    assert fox.energy == 30, "Лиса получает энергию кролика"
    print("test_carnivore_hunt_success passed")


def test_carnivore_hunt_fail() -> None:
    rabbit = Herbivore("Кролик", 30)
    fox = Carnivore("Лиса", 20)
    fox.hunt(rabbit)
    assert rabbit.is_alive(), "Кролик должен выжить"
    assert fox.energy == 20, "Энергия лисы не изменилась"
    print("test_carnivore_hunt_fail passed")


def test_ecosystem_simulation_day() -> None:
    eco = Ecosystem()
    plants = Population("Растения", [Plant("Трава", 10)])
    herbivores = Population("Травоядные", [Herbivore("Заяц", 5)])
    carnivores = Population("Хищники", [Carnivore("Лиса", 20)])
    eco.add_population(plants)
    eco.add_population(herbivores)
    eco.add_population(carnivores)
    eco.simulate_day()
    assert plants.size() == 1, "Растение живое"
    assert herbivores.size() == 1, "Травоядное живо"
    assert carnivores.size() == 1, "Хищник жив"
    print("test_ecosystem_simulation_day passed")


def run_all_tests() -> None:
    test_plant_photosynthesis()
    test_herbivore_eating()
    test_carnivore_hunt_success()
    test_carnivore_hunt_fail()
    test_ecosystem_simulation_day()
    print("\nВсе тесты пройдены.")


if __name__ == "__main__":
    run_all_tests()