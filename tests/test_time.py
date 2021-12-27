"""
https://www.epochconverter.com/
"""

from libdev.time import get_date, parse_time, format_delta


def test_get_date():
    assert get_date(1633427647.018819) == '20211005'
    assert get_date(1633427647.018819, '%d.%m.%Y %H:%M:%S') == '05.10.2021 12:54:07'

def test_parse_time():
    assert parse_time('7.10.1998 7:00:00') == 907743600
    assert parse_time('7 октября 1998 года 12:00:00', tz=5) == 907743600
    assert parse_time('🕒 пн, 20 дек. 2021 г., 00:32:44 MSK') == 1639949564

def test_format_delta():
    assert format_delta(0) == '0 секунд'
    assert format_delta(30) == '30 секунд'
    assert format_delta(31) == '31 секунда'
    assert format_delta(59) == '59 секунд'
    assert format_delta(60) == '60 секунд'
    assert format_delta(180) == '180 секунд'
    assert format_delta(181) == '3 минуты'
    assert format_delta(300) == '5 минут'
    assert format_delta(10799) == '180 минут'
    assert format_delta(10800) == '3 часа'
    assert format_delta(12345) == '3 часа'
    assert format_delta(259200) == '3 дня'
    assert format_delta(259201) == '3 дня'
    assert format_delta(1036800) == '12 дней'
    assert format_delta(8726400) == '101 день'
    assert format_delta(-1) == '-1 секунда'
    assert format_delta(-181) == '-3 минуты'
    assert format_delta(-432000) == '-5 дней'

def test_format_delta_short():
    assert format_delta(0, short=True) == '0 сек'
    assert format_delta(1, short=True) == '1 сек'
    assert format_delta(180, short=True) == '180 сек'
    assert format_delta(181, short=True) == '3 мин'
    assert format_delta(18000, short=True) == '5 ч'
    assert format_delta(1814400, short=True) == '21 д'
