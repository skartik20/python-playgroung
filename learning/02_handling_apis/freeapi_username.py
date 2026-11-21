import requests

def fetch_random_usesr_freeapi():
    url = 'https://prod-main-api-704464-00tre1p1erm.compute.instacloud-edge.com/api/v1/public/randomusers/user/random'

    response = requests.get(url)
    data = response.json()

    if data['success']  and "data" in data:
        user_data = data['data']
        username = user_data['login']['username']
        country = user_data['location']['country']
        return username, country
    else:
        raise Exception("Failed to fetch user data from the API.")

def main():
    try:
        username, country = fetch_random_usesr_freeapi()
        print(f"Username: {username}, Country: {country}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()