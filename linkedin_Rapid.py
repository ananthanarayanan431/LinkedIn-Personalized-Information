from constant import X_RAPIDAPI_KEY
import os
import requests

# Set environment variable for X-RapidAPI-Key
os.environ['X_RAPIDAPI_KEY'] = X_RAPIDAPI_KEY

def get_linkedin_information(linkedin_url):
    linkedin_profile_response = ""
    linkedin_posts_response = ""

    try:
        # Set headers for RapidAPI
        headers = {
            "X-RapidAPI-Key": X_RAPIDAPI_KEY,
            "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
        }

        # Fetch LinkedIn profile data
        linkedin_profile_url = "https://fresh-linkedin-profile-data.p.rapidapi.com/get-linkedin-profile"
        profile_querystring = {
            "linkedin_url": linkedin_url,
            "include_skills": "true",
            "include_certifications": "true",
            "include_publications": "true",
            "include_honors": "true",
            "include_volunteers": "true",
            "include_projects": "true",
            "include_patents": "true",
            "include_courses": "true",
            "include_organizations": "true"
        }
        profile_response = requests.get(linkedin_profile_url, headers=headers, params=profile_querystring)
        linkedin_profile_response = profile_response.json()

        # Fetch LinkedIn posts data
        linkedin_posts_url = "https://fresh-linkedin-profile-data.p.rapidapi.com/get-profile-posts"
        posts_querystring = {"linkedin_url": linkedin_url, "type": "posts"}
        posts_response = requests.get(linkedin_posts_url, headers=headers, params=posts_querystring)
        linkedin_posts_response = posts_response.json()


    except Exception as e:
        print(f"Error fetching LinkedIn information: {e}")

    return linkedin_profile_response,linkedin_posts_response

if __name__=="__main__":
    ans1,ans2=get_linkedin_information("https://www.linkedin.com/in/rananthanarayananofficial/")
    # print(ans[0]['data']['profile_image_url'])
    print("First Response---")
    print(ans1)