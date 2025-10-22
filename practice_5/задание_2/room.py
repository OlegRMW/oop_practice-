from wallboard import WallBoard

class Room:
    
    def __init__(self, height, width, length) -> None:
        self.__wall_boards = []
        self.__height = height
        self.__width = width
        self.__length = length
        
    def add_board(self, board: WallBoard) -> None:
        self.__wall_boards.append(board)

    def get_area_to_cover(self) -> float:
        total_board_square = sum([board.width * board.height for board in self.__wall_boards])
        total_wall_square = self.height * self.width * 2 + self.length * self.height * 2
        return total_wall_square - total_board_square
    
    def get_fabric_meters(self, fabric_width: float) -> float:
        drap_square = self.get_area_to_cover()
        return  drap_square / fabric_width
        
    
    @property
    def width(self):
        return self.__width
    @property
    def height(self):
        return self.__height
    @property
    def length(self):
        return self.__length
    
    
room_1 = Room(3, 4, 5)
room_2 = Room(3, 5, 6)
room_3 = Room(3, 6, 7)

board = WallBoard(0.2, 1)

room_1.add_board(board)
room_1.add_board(board)
room_1.add_board(board)
room_1.add_board(board)
room_1.add_board(board)

room_2.add_board(board)
room_2.add_board(board)
room_2.add_board(board)

room_3.add_board(board)
room_3.add_board(board)


room_width = float(input('Введите ширину комнаты:'))
room_length = float(input('Введите длину комнаты:'))
room_height = float(input('Введите высоту комнаты:'))
cloth_width = float(input('Введите ширину ткани:'))

room = Room(room_height, room_width, room_length)

room.add_board(board)
room.add_board(board)

print(room.get_area_to_cover())
print(room.get_fabric_meters(cloth_width))