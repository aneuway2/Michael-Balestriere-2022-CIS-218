"""
Michael Balestriere
CIS-218 Final Lab
"""
# pylint: disable=too-many-arguments


class Power:
    """Power class"""

    def __init__(self, name=0, megawatts=0, age=0, lifespan=60):
        """set variables"""
        self.name = name
        self.megawatts = megawatts
        self.age = age
        self.lifespan = lifespan

    def capacity(self):
        """calculate electricity"""
        return round(
            (abs(self.megawatts - (self.megawatts / self.lifespan * self.age)))
        )

    def available(self):
        """available power"""
        return bool(self.capacity() > 0)

    def __str__(self):
        """str"""
        return str(self.name) + " (" + str(self.capacity()) + " MW)"

    def __repr__(self):
        """repr"""
        return (
            "Power(name='"
            + str(self.name)
            + "', megawatts="
            + str(self.megawatts)
            + ", age="
            + str(self.age)
            + ", lifespan="
            + str(self.lifespan)
            + ")"
        )


class Wind(Power):
    """Wind class"""

    def __init__(self, name=0, megawatts=0, age=0, lifespan=25):
        """set variables"""
        super().__init__()
        self.name = name
        self.megawatts = megawatts
        self.age = age
        self.lifespan = lifespan

    def capacity(self):
        """calculate electricity"""
        return round(
            (abs(self.megawatts - (self.megawatts / self.lifespan * self.age)))
        )

    def available(self):
        """available power"""
        return bool(self.capacity() > 0)

    def __str__(self):
        """str"""
        return str(self.name) + " (" + str(self.capacity()) + " MW)"

    def __repr__(self):
        """repr"""
        return (
            "Power(name='"
            + str(self.name)
            + "', megawatts="
            + str(self.megawatts)
            + ", age="
            + str(self.age)
            + ", lifespan="
            + str(self.lifespan)
            + ")"
        )


class Nuclear(Power):
    """nuclear class"""

    def __init__(self, name=0, megawatts=0, age=0, lifespan=60, cooling_towers=0):
        """set variables"""
        super().__init__()
        self.name = name
        self.megawatts = megawatts
        self.age = age
        self.lifespan = lifespan
        self.__cooling_towers = cooling_towers

    def capacity(self):
        """calculate electricity"""
        return round(
            (abs(self.megawatts - (self.megawatts / self.lifespan * self.age)))
        )

    def available(self):
        """available power"""
        return bool(round((abs(self.capacity() >= self.__cooling_towers * 100))))

    def __str__(self):
        """str"""
        return str(self.name) + " (" + str(self.capacity()) + ")"

    def __repr__(self):
        """repr"""
        return (
            "Power(name='"
            + str(self.name)
            + "', megawatts="
            + str(self.megawatts)
            + ", age="
            + str(self.age)
            + ", lifespan="
            + str(self.lifespan)
            + ")"
        )


def test_method():
    """test function"""
    # test Wind class
    test = Wind(megawatts=100, age=10)
    assert test.capacity() == 60
    assert test.available() is True
    # test Nuclear class
    test = Nuclear(megawatts=600, age=10, cooling_towers=10)
    assert test.capacity() == 500
    assert test.available() is False
    # test wind str method
    test = Wind(megawatts=100, name="Test Wind Plant", age=0)
    assert str(test) == "Test Wind Plant (100 MW)"
    # test nuclear repr method
    test = Nuclear(megawatts=100, name="Test Nuclear Plant", age=0)
    assert (
        repr(test)
        == "Power(name='Test Nuclear Plant', megawatts=100, age=0, lifespan=60)"
    )
    print("All Checks and Tests Sucessful!\n")


test_method()


if __name__ == "__main__":
    power_plants = [
        Wind(name="Alta Wind Energy", megawatts=1320, age=12),
        Wind(name="Roscoe Wind Farm", megawatts=781, age=10),
        Wind(name="Shepherds Flat Wind Farm", megawatts=845, age=13),
        Nuclear(name="Palo Verde", megawatts=3942, age=36, cooling_towers=3),
        Nuclear(name="Browns Ferry", megawatts=3300, age=48, cooling_towers=6),
        Nuclear(name="South Texas", megawatts=2560, age=34, cooling_towers=0),
    ]
    available = [_ for _ in power_plants if _.available()]
    order = sorted(available, reverse=True, key=lambda plant: plant.capacity())
    named_list = [str(_) for _ in order]
    print(named_list)
