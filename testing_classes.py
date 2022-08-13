from classes import Television


class Test:
    def setup(self):
        self.tv = Television()

    def tear_down(self):
        del self.tv

    def test_power(self):
        """
        - Switch TV on/off
        - Assert it's status has changed
        """
        assert self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
        self.tv.power()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0"

    def test_channel_changing(self):

        """
        - Check if channel changes when TV is off
        """
        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"

        """
        - Check if channel up works
        """
        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 1, Volume = 0"
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0"

        """
        - Check if channel down works
        """
        self.tv.channel_down()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 3, Volume = 0"
        self.tv.channel_up()

    def test_volume_changing(self):
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0"
        self.tv.volume_up()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 1"
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_up()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 2"
        self.tv.volume_down()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 1"
        self.tv.volume_down()
        self.tv.volume_down()
        self.tv.volume_down()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0"
