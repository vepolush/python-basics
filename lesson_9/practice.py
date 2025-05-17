import requests


def get_url() -> str:
    return "https://dummyjson.com/"


def get_data(endpoint: str = "posts") -> list[dict]:
    url = get_url() + endpoint
    params = {"limit": 300}
    response = requests.get(url, params=params)
    response_json = response.json()
    data = response_json[endpoint]
    return data


def get_username() -> str:
    name = input("Username: ")
    return name


def get_user_search_text():
    user_text = ""
    while len(user_text) < 3:
        user_text = input("Введіть слово для пошуку в постах: ").strip()
        if len(user_text) >= 3:
            return user_text


def get_posts_bodies(search_text: str, posts_data: list[dict]) -> list[dict[int, str]]:
    # result = []
    # for post in posts_data:
    #     body: str = post["body"].lower()
    #     if search_text.lower() in body:
    #         result.append({post["id"]: body})
    #

    # result = (
    #     {post["id"]: post["body"]}
    #     for post in posts_data
    #     if search_text.lower() in post["body"].lower()
    # )

    filtered = filter(
        lambda post: search_text.lower() in post["body"].lower(), posts_data
    )
    mapped = map(lambda post: {post["id"]: post["body"]}, filtered)

    return list(mapped)


def main():
    name = get_username()
    print(f"Hello, {name}")
    search_text = get_user_search_text()
    data = get_data()
    relevant_data = get_posts_bodies(search_text, data)
    for post in relevant_data:
        print(post)


if __name__ == "__main__":
    main()
