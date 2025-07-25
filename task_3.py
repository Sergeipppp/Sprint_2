class PointsForPlace:
    points = 0
    @staticmethod
    def get_points_for_place(place):
        if int(place) > 100:
            print('Баллы начисляются только первым 100 участникам')
            points = 0
        elif int(place) < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
            points = 0
        else:
            points = 101 - place
        return int(points)

class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters):
        if int(meters) < 0:
            print('Количество метров не может быть отрицательным')
            points = 0
        else:
            points = meters * 0.5     
        return int(points)


class TotalPoints(PointsForPlace, PointsForMeters):
    def get_total_points(self, meters, place):
        total = self.get_points_for_place(place) + self.get_points_for_meters(meters)
        return int(total)
    
points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))