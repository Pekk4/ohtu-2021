from statistics import Statistics
from player_reader import PlayerReader
from matchers import All, And, HasAtLeast, HasFewerThan, PlaysIn, Not, Or

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher3 = Or(
        HasAtLeast(30, "goals"),
        HasAtLeast(50, "assists")
    )

    matcher2 = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(5, "assists"),
        PlaysIn("PHI")
    )

    matcher = And(
        HasAtLeast(40, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("NYI"),
            PlaysIn("BOS")
        )
    )

    #matcher = PlaysIn("CHI")

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()