from __future__ import annotations

from abc import ABC, abstractclassmethod
from typing import TYPE_CHECKING, Dict, List, NoReturn, Optional

import lexios.matter
from lexios.utils import camel_to_snake

if TYPE_CHECKING:
    from lexios.core.property import Property


class _BaseLaw(ABC):
    def __init__(self) -> None:
        self._props: Dict[str, Property] = dict()
        self._matter: Optional[lexios.matter.Matter] = None
    
    @property
    def props(self) -> Dict[str, Property]:
        return self._props
    
    @props.setter
    def props(self, props: Dict):
        """Set a list of properties that belong to this law"""
        self._props = props
        
    def get_prop(self, name: str) -> Optional[Property]:
        assert isinstance(name, str), f"Expected str to be a string, got {type(name)}"
        name = name.lower()
        
        """Return the property of this law"""
        for prop in self.props:
            if prop['prop'].class_name() == name:
                return prop
    
    def add_props_to_matter(self, matter: lexios.matter.Matter):
        """Add all properties that belongs to this law to the matter

        Args:
            matter (_type_): Matter
        """
        
        assert isinstance(matter, lexios.matter.Matter), f"Expected matter to be a Matter, got {type(matter)}"
        
        if not self.props:
            for prop in self.props:
                matter.add_prop(prop)
    
    def add_law_to_matter(self, matter: lexios.matter.Matter):
        """Add this law to the matter

        Args:
            matter (_type_): Matter
        """
        assert isinstance(matter, lexios.matter.Matter), f"Expected matter to be Matter, got {type(matter)}"
        matter.add_law(self)
        self.add_props_to_matter(matter)
    
    @property
    def matter(self):
        return self._matter
    
    @matter.setter
    def matter(self, matter: lexios.matter.Matter):
        """Set which matter this law belongs to"""
        assert isinstance(matter, lexios.matter.Matter), f"Expected matter to be a Matter, got {type(matter)}"
        self._matter = matter
    
    @classmethod
    def class_name(cls) -> str:  # return the snake style name
        return camel_to_snake(cls.__name__)
    
    @abstractclassmethod
    def expr(self):
        raise NotImplemented("You need to implement the relation between properties for this law")


class Law(_BaseLaw): pass