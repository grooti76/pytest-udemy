from main import get_weather

def test_get_weather():
    assert get_weather(25) == "hot"
    assert get_weather(15) == "cold"
    assert get_weather(20) == "cold"
    assert get_weather(21) == "cold"  # This will fail, indicating a boundary case issue