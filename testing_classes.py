from classes import Television

tv = Television()

def tear_down():
    del tv

def test_power():
    """
    - Switch TV on/off
    - Assert it's status has changed
    """
    assert tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
    tv.power()
    assert tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0"

def test_channel_changing():

    """
    - Check if channel changes when TV is off
    """
    tv.power()
    tv.channel_up()
    assert tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"

    """
    - Check if channel up works
    """
    tv.power()
    tv.channel_up()
    assert tv.__str__() == "TV status: Is on = True, Channel = 1, Volume = 0"
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0"

    """
    - Check if channel down works
    """
    tv.channel_down()
    assert tv.__str__() == "TV status: Is on = True, Channel = 3, Volume = 0"
    tv.channel_up()

def test_volume_changing():
    assert tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0"
    tv.volume_up()
    assert tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 1"
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()
    assert tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 2"
    tv.volume_down()
    assert tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 1"
    tv.volume_down()
    tv.volume_down()
    tv.volume_down()
    assert tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0"
