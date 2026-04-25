"""
Точка входа в симулятор экосистемы.
"""

from ecosystem import Ecosystem
from population import Population
from organism import Plant, Herbivore, Carnivore


def create_initial_ecosystem() -> Ecosystem:
    """Создаёт начальную экосистему с тремя популяциями."""
    eco = Ecosystem()

    plants = Population("Растения", [
        Plant("Трава", 10),
        Plant("Куст", 15),
    ])
    herbivores = Population("Травоядные", [
        Herbivore("Заяц", 20),
    ])
    carnivores = Population("Хищники", [
        Carnivore("Лиса", 35),
    ])

    eco.add_population(plants)
    eco.add_population(herbivores)
    eco.add_population(carnivores)

    return eco


def main() -> None:
    """Основной цикл симуляции."""
    eco = create_initial_ecosystem()
    days = 5
    for day in range(1, days + 1):
        print(f"\n--- День {day} ---")
        eco.simulate_day()
        eco.print_state()
        if eco.all_dead():
            print("Все популяции вымерли. Симуляция остановлена.")
            break


if __name__ == "__main__":
    main()