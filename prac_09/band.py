class Band:
    def __init__(self, name):
        self.name = name
        self.members = []

    def __str__(self):
        """Return string representation of band object"""
        return f"{self.name} ({self.members})"

    def add(self, member):
        """Add a member to the band."""
        self.members.append(member)

    def play(self):
        """Return a string showing the instruments each member is playing or indicating they need an instrument."""
        for member in self.members:
            return member.play()



