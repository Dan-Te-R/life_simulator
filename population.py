"""
Модуль population.py
Класс Population управляет группой организмов одного вида.
"""

from organism import Organism


class Population:
    """Популяция организмов определённого вида."""

    def __init__(self, species_name: str, members: list[Organism]) -> None:
        self.species = species_name
        self.members = members

    def add_organism(self, organism: Organism) -> None:
        """Добавить организм в популяцию."""
        self.members.append(organism)

    def remove_dead(self) -> None:
        """Удалить всех мёртвых организмов (энергия <= 0)."""
        self.members = [org for org in self.members if org.is_alive()]

    def size(self) -> int:
        """Количество живых организмов."""
        return len(self.members)

    def __str__(self) -> str:
        return f"Популяция {self.species}: {self.size()} особей"