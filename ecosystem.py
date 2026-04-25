"""
Модуль ecosystem.py
Управляет взаимодействием популяций в течение одного дня.
"""

from population import Population
from organism import Plant, Herbivore, Carnivore


class Ecosystem:
    """Экосистема, содержащая несколько популяций и симулирующая их жизнь."""

    def __init__(self) -> None:
        self.populations: dict[str, Population] = {}

    def add_population(self, population: Population) -> None:
        """Добавить популяцию в экосистему."""
        self.populations[population.species] = population

    def simulate_day(self) -> None:
        """Один шаг симуляции: фотосинтез, питание, охота, удаление мёртвых."""
        # Растения фотосинтезируют
        if "Растения" in self.populations:
            for plant in self.populations["Растения"].members:
                plant.photosynthesize()

        # Травоядные поедают первое доступное растение
        if "Растения" in self.populations and "Травоядные" in self.populations:
            plants_pop = self.populations["Растения"]
            for herb in self.populations["Травоядные"].members:
                if plants_pop.members:
                    herb.eat_plant(plants_pop.members[0])

        # Хищники охотятся на первое доступное травоядное
        if "Травоядные" in self.populations and "Хищники" in self.populations:
            herb_pop = self.populations["Травоядные"]
            for carn in self.populations["Хищники"].members:
                if herb_pop.members:
                    carn.hunt(herb_pop.members[0])

        # Удаление мёртвых
        for pop in self.populations.values():
            pop.remove_dead()

    def print_state(self) -> None:
        """Вывод текущего состояния экосистемы."""
        print("=== Состояние экосистемы ===")
        for pop in self.populations.values():
            print(pop)
            for org in pop.members:
                print(f"  {org}")
        print("=" * 30)

    def all_dead(self) -> bool:
        """True, если во всех популяциях нет живых организмов."""
        return all(pop.size() == 0 for pop in self.populations.values())