
from Models import Summary, Facts, Interest, IceBreaker, Background
from typing import List, Tuple

from linkedin_Rapid import get_linkedin_information
from CustomChain import SummaryChain, FactsChain, InterstChain, BackgroundChain,IceBreakerChain
from tool import get_social_profile_url

linkedin_pattern = r'https:\/\/(?:\w+\.)?linkedin\.com\/(?:in|pub)\/[\w-]+\/?'

def FinalCall(Name:str,CompanyName:str)->Tuple[Summary,Facts,Interest,IceBreaker,Background,str]:
    Username=get_social_profile_url(Name,CompanyName,"LinkedIn",linkedin_pattern)
    ProfileData,PostData=get_linkedin_information(Username)

    summary_chain=SummaryChain()
    summ:Summary=summary_chain.invoke(
        input={'information':ProfileData},
    )

    facts_chain=FactsChain()
    facts:Facts=facts_chain.invoke(
        input={'information':ProfileData},
    )

    interst_chain=InterstChain()
    inter:Interest=interst_chain.invoke(
        input={'information':ProfileData},
    )

    background=BackgroundChain()
    back:Background=background.invoke(
        input={'information':ProfileData},
    )

    icebreaker=IceBreakerChain()
    ice:IceBreaker=icebreaker.invoke(
        input={'information':ProfileData},
    )

    profile_url=ProfileData['data']['profile_image_url']


    return (
        summ,
        facts,
        inter,
        back,
        ice,
        profile_url,
    )

if __name__ == "__main__":
    print(FinalCall("Karan Rai","Lauch Ventures"))