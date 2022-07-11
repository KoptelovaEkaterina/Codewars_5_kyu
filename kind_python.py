
        
#https://stepik.org/lesson/701974/step/6?unit=702075

class Graph:
    LIMIT_Y = [0, 10]
    new_list = []

    def set_data(self, data):
        self.data = data


    def draw(self):
        for num in self.data:
            if num in range(Graph.LIMIT_Y[0],Graph.LIMIT_Y[1]+1):
                Graph.new_list.append(num)
        print(* Graph.new_list)


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()        



# https://stepik.org/lesson/567052/step/8?thread=solutions&unit=561326

def run_perimeter(width, height):
    x = 2 * (width + height)
    print(f'Периметр прямоугольника, равен {x}')

# args
run_perimeter(*map(int, input().split()))
