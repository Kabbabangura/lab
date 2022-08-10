from classes import Television

tv = Television()

def test_power():
    """
    - Switch TV on/off
    - Assert it's status has changed
    """
    status = tv.get_status()
    tv.power()
    assert tv.get_status() != status

def test_change_channel_while_off():
    """
    - Check if channel changes when TV is off
    - Assert it does not change
    """
    if tv.get_status():
        tv.power()
    channel = tv.get_channel()
    tv.channel_up()
    assert tv.get_channel() == channel

def test_channel_up():
    """
    - Check if channel up works
    - Assert it changes
    """
    if not tv.get_status():
        tv.power()
    channel_nxt = tv.get_channel() + 1
    if channel_nxt > tv.MAX_CHANNEL:
        channel_nxt = tv.MIN_CHANNEL
    tv.channel_up()
    assert tv.get_channel() == channel_nxt

def test_channel_down():
    """
    - Check if channel down works
    - Assert it changes
    """
    if not tv.get_status():
        tv.power()
    channel_prvs = tv.get_channel() - 1
    if channel_prvs < tv.MIN_CHANNEL:
        channel_prvs = tv.MAX_CHANNEL
    tv.channel_down()
    assert tv.get_channel() == channel_prvs

def test_volume_up():    
    if not tv.get_status():
        tv.power()
    volume_nxt = tv.get_volume()
    if volume_nxt != tv.MAX_VOLUME:
        volume_nxt += 1
    tv.volume_up()
    assert tv.get_volume() == volume_nxt

def test_volume_down():    
    if not tv.get_status():
        tv.power()
    volume_prvs = tv.get_volume()
    if volume_prvs != tv.MIN_VOLUME:
        volume_prvs -= 1
    tv.volume_down()
    assert tv.get_volume() == volume_prvs