from typing import List
from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base

class Hero(Base):
    __tablename__ = "heroes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    about_me = Column(String)
    biography = Column(String)
    image_url = Column(String)

    abilities: Mapped[List["Abilities"]] = relationship(
        back_populates="hero", cascade="all, delete-orphan")
    
    relationships: Mapped[List["Relationships"]] = relationship(
        back_populates="hero", cascade="all, delete-orphan")
    
    def __repr__(self) -> str:
        return f"Hero(id={self.id!r}, name={self.name!r}, about_me{self.about_me!r}, biography={self.biography!r}, image_url)"
    
class Ability(Base):
    __tablename__ = "abilities"

    id: Mapped[str] = mapped_column(primary_key=True, index=True)
    ability_type_id: Mapped[int] = mapped_column(ForeignKey("ability_types.id"))
    hero_id: Mapped[int] = mapped_column(ForeignKey("heroes.id"))

    def __repr__(self) -> str:
        return f"Ability(id={self.id!r}, ability_type_id={self.ability_type_id!r}, hero_id={self.hero_id!r})"
    
class Relationships(Base):
    __tablename__ = "relationships"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    hero1_id: Mapped[int] = mapped_column(ForeignKey("heroes.id"))
    hero2_id: Mapped[int] = mapped_column(ForeignKey("heroes.id"))
    relationship_type_id: Mapped[int] = mapped_column(ForeignKey("relationship_types.id"))

    def __repr__(self) -> str:
        return f"Relationship(id={self.id!r}, hero1_id={self.hero1_id!r}, hero2_id={self.hero2_id!r}, relationship_type_id={self.relationship_type_id!r})"
    
class AbilityType(Base):
    __tablename__ = "ability_types"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"AbilityType(id={self.id!r}, name={self.name!r})"
    
class RelationshipType (Base):
    __tablename__ = "relationship_types"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"RelationshipType(id={self.id!r}, name={self.name!r})"
    