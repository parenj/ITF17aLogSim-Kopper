
__version__ = '2.0'
__author__ = 'Alexander Kopper'


class OrGate:
    """
    This class calculates the logical OR function.
    """

    def __init__(self):
        self.__Input0 = False
        self.__Input1 = False
        self.__Output = False
        self.__Name = "KoOrGate"

        def __get_input0(self):
            """
            Returns the value of the first input signal.
            :return: Input0
            """
            return self.__Input0

        def __get_input1(self):
            """
            Returns the value of the second input signal.
            :return: Input1
            """
            return self.__Input1

        def __get_output(self):
            """
            Returns the value of the output signal.
            :return: Output
            """
            return self.__Output

        def __get_name(self):
            """
            Returns the value of the name property.
            :return: Name
            """
            return self.__Name

        def __set_input0(self, value):
            """
            Sets the value of the first input signal
            :param value: (bool) new value
            :return: None
            """
            isinstance(value, bool)
            self.__Input0 = value

        def __set_input1(self, value):
            """
            Sets the value of the second input signal
            :param value: (bool) new value
            :return: None
            """
            isinstance(value, bool)
            self.__Input1 = value

        def __set_output(self, value):
            """
            Sets the value of the output signal
            :param value: (bool) new value
            :return: None
            """
            isinstance(value, bool)
            self.__Output = value

        def __set_name(self, value):
            """
            Sets the value of the name property
            :param value: (string) new value
            :return: None
            """
            isinstance(value, str)
            self.__Name = value

        Name = property(__get_name, __set_name)
        Input0 = property(__get_input0, __set_input0)
        Input1 = property(__get_input1, __set_input1)
        Output = property(__get_output, None)

    def execute(self):
        """
        Computes the result of the logical connection of the two inputs.
        :return: None
        """
        self.Output = True
        if False == self.Input0:
            if False == self.Input1:
                self.Output = False
        # else:
        #     # self.Output = True

    def __str__(self):
        """
        Converts the status of the object to a string. The function will be called
        implicitly when you try to convert the object in a string.
        :return: Printable string of the status.
        """
        cwidth = 50
        first_last = ''.ljust(cwidth, '-')
        format_string = "-- {{0:10}}: {{1:{0}}} --".format(cwidth - 18)

        return_string = first_last
        return_string = return_string + "\n" + format_string.format("Name", self.Name)
        return_string = return_string + "\n" + format_string.format("Type", type(self).__name__)
        return_string = return_string + "\n" + format_string.format("Input0", str(self.__Input0))
        return_string = return_string + "\n" + format_string.format("Input1", str(self.__Input1))
        return_string = return_string + "\n" + format_string.format("Output", str(self.__Output))
        return_string = return_string + "\n" + first_last
        return return_string

    def show(self):
        """
        Shows the value of each property of the class and the class name.
        :return: None
        """
        print(self.__str__())
