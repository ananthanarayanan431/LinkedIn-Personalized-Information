from langchain_core.runnables import RunnableSequence
from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from constant import OPENAI_API_KEY
import os

from Models import SummaryParser, FactsParser, BackgroundParser, InterestParser, IceBreakerParser

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
llm_creative = ChatOpenAI(temperature=0.8, model="gpt-4o-mini")


def SummaryChain() -> RunnableSequence:
    template = """
    Using the Detailed information from LinkedIn {information} and {information1} Generate a compressive summary and try give detailed summary.
    It should be well crafted and written properly.
    Procedure: Extract detailed data from the LinkedIn profile, analyze it to identify patterns and highlights,and compose a concise, engaging summary. 
    Identify and explain standout quality of that person that highlight's the person's unique attributes.

    Output: A well-crafted summary paragraph
    \n{format_instructions}
    """

    summary = PromptTemplate(
        input_variables=['information','information1'],
        template=template,
        partial_variables={'format_instructions': SummaryParser.get_format_instructions()}
    )

    return summary | llm | SummaryParser


def FactsChain() -> RunnableSequence:
    template = """
    Given comprehensive LinkedIn {information} and {information1}, identify three facts about that interest a person based on their professional background, skills, and personal interests. 
    Procedure: Extract detailed data from their LinkedIn profile, analyze it to identify relevant patterns and highlights, and 
    identify topics of interest based on professional, personal, and networking aspects. 

     Output: Provide detailed topics of interest, each with an explanation of its relevance.
     \n{format_instructions}
     """

    facts = PromptTemplate(
        input_variables=['information','information1'],
        template=template,
        partial_variables={'format_instructions': FactsParser.get_format_instructions()}
    )

    return facts | llm | FactsParser


def BackgroundChain() -> RunnableSequence:
    template = """
    Given comprehensive information {information} and {information1}, Identify the background of the person like Education and work Experience over the years.
    Specify the about Company Name and Education institute name as well, Include other important information regarding Courses and Certificates as well

    Output: Provide details Background information, each with an explained of its relevance.
    /n {format_instructions}
    """

    Background = PromptTemplate(
        input_variables=['information','information1'],
        template=template,
        partial_variables={'format_instructions': BackgroundParser.get_format_instructions()}
    )

    return Background | llm | BackgroundParser


def InterstChain() -> RunnableSequence:
    template = """
    Given a comprehensive LinkedIn profile {information} and {information1}, analyze the professional background, skills, and personal interests of the individual. Identify three potential topics or domains that are likely to interest this person. For each topic, provide a detailed explanation that includes:
    Topic of Interest: Clearly state the area or domain of interest.
    Justification: Explain why this topic is relevant based on the person's career trajectory, skills, and stated interests.
    Supporting Evidence: Cite specific experiences, roles, achievements, or personal activities that suggest a strong interest in this domain.
    Potential Engagement: Describe how this interest might manifest in their professional or personal life, such as involvement in specific projects, pursuing further education, or participating in relevant events or communities.
    
    Output:
    Provide three detailed topics of interest, each accompanied by a thorough explanation of its relevance, supported by evidence from the individual's profile
    /n {format_instructions}
    """

    Interst = PromptTemplate(
        input_variables=['information','information1'],
        template=template,
        partial_variables={'format_instructions': InterestParser.get_format_instructions()}
    )

    return Interst | llm | InterestParser


def IceBreakerChain() -> RunnableSequence:
    template = """
    Given comprehensive LinkedIn {information} and {information1}, create two creative ice breakers derived from the person's activity. 
    Requirements: Analyze their posts, shared articles, comments, group activities, followed pages, endorsements, and recommendations. 
    Ensure ice breakers are relevant to their activity, engaging, and positive to spark meaningful conversations. 
    Procedure: Extract and analyze detailed LinkedIn activity data to understand their interests and professional focus, identify notable patterns or themes, 
    and develop personalized ice breakers based on this analysis. 

    Output: Provide two detailed and personalized ice breakers with explanations of their relevance and connection to the person's LinkedIn engagements.
    \n{format_instructions}
    """

    IceBreaker = PromptTemplate(
        input_variables=['information','information1'],
        template=template,
        partial_variables={'format_instructions': IceBreakerParser.get_format_instructions()}
    )

    return IceBreaker | llm | IceBreakerParser