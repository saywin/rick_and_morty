import requests
from django.conf import settings
from django.db import IntegrityError

from characters.models import Character


def scrapper_characters() -> list[Character]:
    next_url_to_scrapper = settings.RICK_AND_MORTY_API_CHARACTERS_URL

    characters = []

    while next_url_to_scrapper is not None:
        characters_response = requests.get(next_url_to_scrapper).json()

        for character_dict in characters_response["results"]:
            characters.append(
                Character(
                    name=character_dict["name"],
                    id_api=character_dict["id"],
                    status=character_dict["status"],
                    species=character_dict["species"],
                    gender=character_dict["gender"],
                    image=character_dict["image"],
                )
            )
        next_url_to_scrapper = characters_response["info"]["next"]
    return characters


def save_characters(characters: list[Character]) -> None:
    for character in characters:
        try:
            character.save()
        except IntegrityError:
            print(f"Character with 'id_api': {character.id_api} already exist in DB!")


def sync_characters_wit_api() -> None:
    characters = scrapper_characters()
    save_characters(characters)
