import random
import curses
from curses import textpad

class Ground():
    def __init__(self, sh,sw, stdscr):
        self.box = [[3,3], [sh-3, sw-3]]
        textpad.rectangle(stdscr, self.box[0][0], self.box[0][1], self.box[1][0], self.box[1][1])

    def get_food(self, snake):
        food = None
        while food is None:
            food = [random.randint(self.box[0][0]+1, self.box[1][0]-1),
            random.randint(self.box[0][1]+1, self.box[1][1]-1)]
            if food in snake:
                food=None
        return food
    def screen_print(self, stdscr, y, x, text):
        stdscr.addstr(y, x, text)
    def display_snake(self, stdscr, snake):
        for y,x in snake:
            self.screen_print(stdscr, y, x, '#')


class Snake():
    def __init__(self, sh, sw):
        self.body = [[sh//2,sw//2 +1], [sh//2,sw//2 ], [sh//2,sw//2 -1]]
        self.direction = curses.KEY_RIGHT

    def move(self, stdscr, key, ground):
        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            self.direction = key
        head = self.body[0]
        if self.direction == curses.KEY_RIGHT:
            new_head = [head[0], head[1]+1]
        elif self.direction == curses.KEY_LEFT:
            new_head = [head[0], head[1]-1]
        elif self.direction == curses.KEY_UP:
            new_head = [head[0]-1, head[1]]
        elif self.direction == curses.KEY_DOWN:
            new_head = [head[0]+1, head[1]]
        self.body.insert(0, new_head)
        ground.screen_print(stdscr, new_head[0], new_head[1], '#')

    def is_alive(self, box):
        head = self.body[0]
        if head in self.body[1:]:
            return False
        if (head[0] in [box[0][0], box[1][0]]) or (head[1] in [box[0][1], box[1][1]]):
            return False
        return True

    def ate_food(self, food):
        return self.body[0] == food


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    sh, sw =stdscr.getmaxyx()
    ground = Ground(sh, sw, stdscr)
    snake = Snake(sh, sw)
    food = ground.get_food(snake.body)
    ground.screen_print(stdscr, food[0], food[1], '@')
    ground.display_snake(stdscr, snake.body)
    score = 0
    score_text = 'Score: '+str(score)
    ground.screen_print(stdscr, 1, sw//2 -len(score_text)//2, score_text)
    while 1:
        key = stdscr.getch()
        snake.move(stdscr, key, ground)
        if snake.ate_food(food):
            food = ground.get_food(snake.body)
            ground.screen_print(stdscr, food[0], food[1], '@')
            score += 1
            score_text = 'Score: '+str(score)
            ground.screen_print(stdscr, 1, sw//2 -len(score_text)//2, score_text)
        else:
            ground.screen_print(stdscr, snake.body[-1][0], snake.body[-1][1], ' ')
            snake.body.pop()
        if not snake.is_alive(ground.box):
            over = "Game Over!"
            ground.screen_print(stdscr, sh//2, sw//2 -len(over)//2, over)
            stdscr.nodelay(0)
            stdscr.getch()
            break

if __name__ == "__main__":
    curses.wrapper(main)
