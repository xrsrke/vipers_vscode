from __future__ import annotations

from typing import List

import pytest

import lexios.core.law as law
import lexios.core.property as prop
import lexios.matter as matter
import lexios.system as system
from lexios.physics.newton import NewtonFirstLaw


class MatterWithoutLaw(matter.MacroMatter):
    def __init__(self):
        super().__init__()

class MatterWithLawList(matter.MacroMatter):
    def __init__(self):
        super().__init__()
        self.laws = law.LawList([NewtonFirstLaw])

class MatterWithLaw(matter.MacroMatter):
    def __init__(self):
        super().__init__()
        self.laws = [NewtonFirstLaw]
        for law in self.laws:
            name = law.class_name()
            self.add_law(name, law)

@pytest.fixture
def mass():
    return prop.Mass()

@pytest.fixture
def matter_without_law():
    return MatterWithoutLaw()

@pytest.fixture
def matter_with_lawlist():
    return MatterWithLawList()

@pytest.fixture
def matter_with_law():
    return MatterWithLaw()

@pytest.fixture
def system():
    return system.System()
