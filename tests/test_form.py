import pytest
from src.form import Form


def test_form_initialization():
    form = Form()
    assert form.data == {
        "Firstname": "",
        "Lastname": "",
        "Email": "",
        "Reason of contact": "",
        "Urgency": None,
    }


def test_form_completion():
    form = Form()
    form.data = {
        "Firstname": "Jan",
        "Lastname": "Kowalski",
        "Email": "jan@example.com",
        "Reason of contact": "Problem z hasłem",
        "Urgency": 5,
    }
    assert form.is_complete() is True


def test_form_update_data():
    form = Form()
    update = {"Firstname": "Anna", "Urgency": 7}
    form.update_data(update)
    assert form.data["Firstname"] == "Anna"
    assert form.data["Urgency"] == 7
