from typing import List, Dict, Any
from constant import OPENAI_API_KEY

from langchain.output_parsers import PydanticOutputParser
from langchain.pydantic_v1 import BaseModel, Field
import os

os.environ['OPENAI_AI_KEY'] = OPENAI_API_KEY

class InterestItem(BaseModel):
    Topic_of_Interest: str
    Justification: str
    Supporting_Evidence: str
    Potential_Engagement: str


class Summary(BaseModel):
    Summary: str = Field(description="Summary of about the person")

    def ans(self) -> Dict[str, Any]:
        return {'summary': self.Summary}


class Facts(BaseModel):
    Facts: List[str] = Field(description="Facts about the Person")

    def ans(self) -> Dict[str, Any]:
        return {'facts': self.Facts}


class Background(BaseModel):
    Background: List[str] = Field(description="Person's Background including Education and Work experience")

    def ans(self) -> Dict[str, Any]:
        return {'background': self.Background}


class Interest(BaseModel):
    Interest: List[InterestItem] = Field(description="Topic of Interest of that particular person!")

    def ans(self) -> Dict[str, Any]:
        return {'Interest': [item.dict() for item in self.Interest]}

class IceBreaker(BaseModel):
    IceBreaker: List[str] = Field(
        description="Icebreakers for particular person based on the topic of Interest or Background")

    def ans(self) -> Dict[str, Any]:
        return {'icebreaker': self.IceBreaker}


SummaryParser = PydanticOutputParser(pydantic_object=Summary)
FactsParser = PydanticOutputParser(pydantic_object=Facts)
BackgroundParser = PydanticOutputParser(pydantic_object=Background)
InterestParser = PydanticOutputParser(pydantic_object=Interest)
IceBreakerParser = PydanticOutputParser(pydantic_object=IceBreaker)