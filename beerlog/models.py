
# # brewdog = Beer(name="Brewdog", style="NEIPA", flavor=6, image=8, cost=8)
# # # apos criar uma instância da classe, pode ir no terminal dentro do projeto e informar o caminho de models:
# # # python -i beerlog/models.py e assim temos acesso a esse objego: Beer, brewdog, brewdog.cost
# # # ipython -i beerlog/models.py
# # ***********************************************************************************************************************
# UTILIZANDO dataclass
# from dataclasses import dataclass

# @dataclass
# class Beer:
#     name: str
#     style: str
#     flavor: int
#     image: int
#     cost: int

# # criação de um objeto
# brewdog = Beer(name='Brewdog', style="NEIPA", flavor=6, image=8, cost=8)
#
#
#
# UTILIZANDO sqlmodel
from typing import Optional
from sqlmodel import SQLModel, Field
from sqlmodel import select
from pydantic import validator
from statistics import mean
from datetime import datetime

class Beer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0
    date: datetime = Field(default_factory=datetime.now)
    
    @validator('flavor', 'image', 'cost')
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f'{field.name} must be between 1 and 10')
        return v
    
    @validator('rate', always=True)
    def calculate_rate(cls, v, values):
        rate = mean(
            [
                values['flavor'],
                values['image'],
                values['cost']
            ]
        )
        return int(rate)
    
# try:
brewdog = Beer(name='Brewdog', style="NEIPA", flavor=6, image=8, cost=8)
# print('Adicionando com sucesso!!')
# except RuntimeError:
#     print('Zika demais!!')

# PAREI EM 1:32