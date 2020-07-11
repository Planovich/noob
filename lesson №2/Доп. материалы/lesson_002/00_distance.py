#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

Moscow = sites['Moscow']
London = sites['London']
Paris = sites['Paris']


moscow_london = (((Moscow[0] - London[0]) ** 2) + ((Moscow[1] - London[1]) ** 2)) ** 0.5
london_paris = (((London[0] - Paris[0]) ** 2) + ((London[1] - Paris[1]) ** 2)) ** 0.5
paris_moscow = (((Paris[0] - Moscow[0]) ** 2) + ((London[1] - Paris[1]) ** 2)) ** 0.5

distances = {}

distances[Moscow] = {}
distances[Moscow][London] = moscow_london
distances[Moscow][Paris] = paris_moscow
distances[London] = {}
distances[London][Paris] = london_paris
distances[London][Moscow] = moscow_london
distances[Paris] = {}
distances[Paris][Moscow] = paris_moscow
distances[Paris][London] = london_paris



print(distances[Moscow][London])
print(distances[London][Paris])
print(distances[Paris][Moscow])




