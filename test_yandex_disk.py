import pytest
import requests

TOKEN = "..."

BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"
HEADERS = {
    "Authorization": f"OAuth {TOKEN}"
}


def create_folder(path):
    return requests.put(BASE_URL, headers=HEADERS, params={"path": path})


def delete_folder(path):
    return requests.delete(BASE_URL, headers=HEADERS, params={"path": path})


def get_folder_info(path):
    return requests.get(BASE_URL, headers=HEADERS, params={"path": path})


@pytest.mark.parametrize("folder_name", [
    "test_folder_1",
    "test_folder_2",
    "test_folder_3",
])
def test_create_folder_success(folder_name):
    delete_folder(folder_name)
    response = create_folder(folder_name)
    assert response.status_code == 201

    info = get_folder_info(folder_name)
    assert info.status_code == 200

    delete_folder(folder_name)


def test_create_folder_conflict():
    folder_name = "test_conflict_folder"
    delete_folder(folder_name)

    response_first = create_folder(folder_name)
    assert response_first.status_code == 201

    response_second = create_folder(folder_name)
    assert response_second.status_code == 409

    delete_folder(folder_name)


def test_create_folder_unauthorized():
    response = requests.put(
        BASE_URL,
        headers={"Authorization": "OAuth invalid_token"},
        params={"path": "test_unauthorized"}
    )
    assert response.status_code == 401


def test_create_folder_not_found():
    response = requests.put(
        BASE_URL,
        headers=HEADERS,
        params={"path": "nonexistent_parent/subfolder"}
    )
    assert response.status_code in (404, 409)