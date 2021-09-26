"""
This is part of the group project from discrete math.
"""
import copy


def zvyaznist(graph: dict) -> list:
    """
    This function finds out if the graph is connected.
    """
    lst_tops = list()
    counter = 0
    while graph != {}:
        set_tops = set()
        for element in graph:
            set_tops.add(element)
            while True:
                for top in graph[element]:
                    set_tops.add(top)
                help_set = copy.deepcopy(set_tops)
                for top in help_set:
                    if top in graph:
                        for each_top in graph[top]:
                            set_tops.add(each_top)
                if help_set == set_tops:
                    break
            lst_tops.append(set_tops)
            break
        for top in lst_tops[counter]:
            graph.pop(top)
        counter += 1
    return [min(top) for top in lst_tops]


if __name__ == "__main__":
    print(zvyaznist({5: {1}, 2: {1}, 4: {3}, 1: {2, 5, 8},
                     3: {4}, 8: {9, 5}, 9: {8}, 10: {20}, 20: {10}, 13: set()}))
