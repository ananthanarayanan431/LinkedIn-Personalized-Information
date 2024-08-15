
import os
import requests
from constant import PROXYCURL_API_KEY

os.environ['PROXYCURL_API_KEY']=PROXYCURL_API_KEY


def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""

    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
    response = requests.get(
        api_endpoint,
        params={"url": linkedin_profile_url},
        headers=header_dic,
        timeout=30,
    )

    data = response.json()

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], " ", "", None)
        and k
        not in [
            "people_also_viewed",
            "similarly_named_profiles",
            "certifications",
            "inferred_salary",
            "connections",
        ]
    }

    # for k,v in data.items():
    #     if k=="groups":
    #         print(data.get("groups")[0])

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/rananthanarayananofficial/",
        )
    )