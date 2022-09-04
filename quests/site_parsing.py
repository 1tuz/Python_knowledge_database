import pytest
import requests
from pydantic import BaseModel, validator, ValidationError
from pydantic.dataclasses import dataclass


# Суть задачи : запарсить ответ при открытии ссылки и провалидировать json + ответ
# Стек : pydantic, requests, pytest
@dataclass
class LinkValidation:
    link: str


def test_func():
    link = "https://www.wildberries.ru/catalog/0/search.aspx?sort=popular&search=iphone+11"
    r = requests.get(link)
    assert r.status_code != 404
    body = r
    try:
        json = body.parse_raw
    except ValidationError as e:
        print(e.json())
