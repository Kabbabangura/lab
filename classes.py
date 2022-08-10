class Television:
    MIN_CHANNEL : int = 0     # Minimum TV channel
    MAX_CHANNEL : int = 3     # Maximum TV channel

    MIN_VOLUME : int = 0      # Minimum TV volume
    MAX_VOLUME : int = 2      # Maximum TV volume

    def __init__(self):
        """
        - Create a private variable to store the TV channel. It should be set to the minimum TV channel by default.
        - Create a private variable to store the TV volume. It should be set to the minimum TV volume by default.
        - Create a private variable to store the TV status. The TV should start when it is off.
        """
        self.__channel = self.MIN_CHANNEL
        self.__volume = self.MIN_VOLUME
        self.__status = False

    def power(self):
        """
        - This method should be used to turn the TV on/off.
        - If called on a TV object that is off, the TV object should be turned on.
        - If called on a TV object that is on, the TV object should be turned off.
        """
        if self.__status == True:
            self.__status = False
        else:
            self.__status = True

    def channel_up(self):
        """
        - This method should be used to adjust the TV channel by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_CHANNEL, it should take the TV channel back to the MIN_CHANNEL.
        """
        #check if TV is on
        if self.__status == True:
            #if channel is set to max channel
            if self.__channel == self.MAX_CHANNEL:
                #set channel to min channel
                self.__channel = self.MIN_CHANNEL
            #otherwise increase channel number
            else:
                self.__channel = self.__channel + 1

    def channel_down(self):
        """
        - This method should be used to adjust the TV channel by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_CHANNEL, it should take the TV channel back to the MAX_CHANNEL.
        """
        #check if TV is on
        if self.__status == True:
            #if channel is set to min channel
            if self.__channel == self.MIN_CHANNEL:
                #set channel to to max channel
                self.__channel = self.MAX_CHANNEL
            #otherwise decrease channel numbera
            else:
                self.__channel = self.__channel - 1

    def volume_up(self):
        """
        - This method should be used to adjust the TV volume by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_VOLUME, the volume should not be adjusted.
        """
        #check if TV is on 
        if self.__status == True:
            #if volume if set to max
            if self.__volume != self.MAX_VOLUME:
                self.__volume = self.__volume + 1

    def volume_down(self):
        """
        - This method should be used to adjust the TV volume by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_VOLUME, the volume should not be adjusted.
        """
        #check if TV is on 
        if self.__status == True:
            #if volume is set to minimum
            if self.__volume != self.MIN_VOLUME:
                self.__volume = self.__volume - 1

    def __str__(self) -> str:
        """
        - This method should be used to return the TV status using the format shown in the comments of main.py
        """
        return "TV status: Is on = " + str(self.__status) + ", Channel = " + str(self.__channel)  + ", Volume = " + str(self.__volume)
        