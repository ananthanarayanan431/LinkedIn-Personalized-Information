
from langchain_core.runnables import RunnableSequence
from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from constant import OPENAI_API_KEY
import os 

from Models import SummaryParser,FactsParser,BackgroundParser,InterestParser, IceBreakerParser

os.environ['OPENAI_API_KEY']=OPENAI_API_KEY

llm=ChatOpenAI(temperature=0,model="gpt-4o-mini")
llm_creatie=ChatOpenAI(temperature=0.8,model="gpt-4o-mini")

def SummaryChain()->RunnableSequence:
    template="""
    Using the Detailed information from LinkedIn {information} Generate a compresenive summary and try give detailed summary.
    It should be well crafted and written properly.
    Procedure: Extract detailed data from the LinkedIn profile, analyze it to identify patterns and highlights,and compose a concise, engaging summary. 
    dentify and explain standout qaluity of that person that highlight's the person's unique attributes.
    
    Output: A well-crafted summary paragraph
    \n{format_instructions}
    """

    summary=PromptTemplate(
        input_variables=['information'],
        template=template,
        partial_variables={'format_instructions': SummaryParser.get_format_instructions()}
    )

    return summary |llm | SummaryParser

def FactsChain()->RunnableSequence:
    template="""
    Given comprehensive LinkedIn {information}, identify three facts about that interest a person based on their professional background, skills, and personal interests. 
    Procedure: Extract detailed data from their LinkedIn profile, analyze it to identify relevant patterns and highlights, and 
    identify topics of interest based on professional, personal, and networking aspects. 
    
     Output: Provide detailed topics of interest, each with an explanation of its relevance.
     \n{format_instructions}
     """
    
    facts=PromptTemplate(
        input_variables=['information'],
        template=template,
        partial_variables={'format_instructions':FactsParser.get_format_instructions()}
    )

    return facts|llm|FactsParser

def BackgroundChain()->RunnableSequence:
    template="""
    Given comprehensive information {information}, Identify the background of the person like Education and work Experience over the years.
    Specify the about Company Name and Education institute name as well, Include other important information reagarding Courses and Certificates as well
    
    Output: Provide details Background information, each with an explained of its relevance.
    /n {format_instructions}
    """

    Background=PromptTemplate(
        input_variables=['information'],
        template=template,
        partial_variables={'format_instructions':BackgroundParser.get_format_instructions()}
    )

    return Background | llm | BackgroundParser

def InterstChain()->RunnableSequence:
    template="""
     Given comprehensive LinkedIn {information}, identify three topics that might interest a person based on their professional background, skills, and personal interests. 
    Requirements: For professional interests, focus on industry trends, career development, and technical skills. 
    For personal interests, consider hobbies, volunteering, and personal development. 
    For networking, look at industry events, thought leaders, and professional associations. 
    Procedure: Extract detailed data from their LinkedIn profile, analyze it to identify relevant patterns and highlights, and identify topics of interest based on professional, personal, and networking aspects. 
    
    Output: Provide detailed topics of interest, each with an explanation of its relevance.
    /n{format_instructions}
    """

    Interst=PromptTemplate(
        input_variables=['information'],
        template=template,
        partial_variables={'format_instructions':InterestParser.get_format_instructions()}
    )

    return Interst | llm | InterestParser

def IceBreakerChain()->RunnableSequence:
    template="""
     Given comprehensive LinkedIn {information}, create two creative ice breakers derived from the person's activity. 
    Requirements: Analyze their posts, shared articles, comments, group activities, followed pages, endorsements, and recommendations. 
    Ensure ice breakers are relevant to their activity, engaging, and positive to spark meaningful conversations. 
    Procedure: Extract and analyze detailed LinkedIn activity data to understand their interests and professional focus, identify notable patterns or themes, 
    and develop personalized ice breakers based on this analysis. 
        
    Output: Provide two detailed and personalized ice breakers with explanations of their relevance and connection to the person's LinkedIn engagements.
    \n{format_instructions}
    """

    IceBreaker=PromptTemplate(
        input_variables=['information'],
        template=template,
        partial_variables={'format_instructions':IceBreakerParser.get_format_instructions()}
    )

    return IceBreaker | llm | IceBreakerParser