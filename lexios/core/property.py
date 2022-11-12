from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Optional

import lexios.core.law as law
from lexios.unit import Unit
from lexios import matter
from lexios.utils import camel_to_snake


class PropertyData(dict): pass

class _BaseProperty:
    def __init__(self):
        self.abrv: Optional[str] = None
        self.unit: Optional[Unit] = None
        self._data: PropertyData = PropertyData()
        self._laws: Dict[str, law.Law] = dict()
        self._matter: Optional[matter.Matter] = None
    
    @classmethod
    def class_name(cls) -> str:
        return camel_to_snake(cls.__name__)
    
    @property
    def laws(self) -> Dict[str, law.Law]:
        return self._laws
    
    def add_law(self, law: law.Law):
        assert isinstance(law, law), f"Expected law to be a Law, got {type(law)}"
        
        name = law.class_name()
        if self._laws and not name in self._laws:
            self._laws[name] = law

    def remove_law(self, name: str):
        """
        Docstring.remove_law(self, name: str
        """
        pass
    
    @property
    def matter(self) -> Optional[matter.Matter]:
        """An property can't exists without matter."""
        return self._matter
    
    @matter.setter
    def matter(self, matter: matter.Matter):
        assert isinstance(matter, matter), f"Expected matter to be a Matter, but got {type(matter)}"
        self._matter = matter

class Property(_BaseProperty):
    pass

class Mass(Property):
    """Mass Property"""
    def __init__(self):
        super().__init__()
        self.abrv = 'm'
        self.unit = Unit.MASS

class Mole(Property):
    """Mole Property"""
    def __init__(self):
        super().__init__()
        self.abrv = 'n'
        self.unit = Unit.MOLE

class Force(Property):
    """Force Property"""
    def __init__(self):
        super().__init__()
        self.abrv = 'F'
        self.unit = Unit.FORCE

class Acceleration(Property):
    """Acceleration Property"""
    def __init__(self):
        super().__init__()
        self.abrv = 'a'
        self.unit = Unit.ACCELERATION