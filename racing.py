import random
import os
import time
import keyboard


def draw_car(track_width, car_position):
    """绘制赛车"""
    car = '🚗'
    track = '□' * track_width
    return track[:car_position] + car + track[car_position + 1:]


def draw_obstacle(track_width, obstacle_position):
    """绘制障碍物"""
    obstacle = '█'
    track = '□' * track_width
    return track[:obstacle_position] + obstacle + track[obstacle_position + 1:]


def update_screen(track_width, car_position, obstacle_position, score):
    """更新屏幕"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Press 'Q' to quit.")
    print(draw_car(track_width, car_position))
    print(draw_obstacle(track_width, obstacle_position))
    print(f"Score: {score}")


def car_game():
    """赛车游戏主函数"""
    track_width = 20
    car_position = track_width // 2
    obstacle_position = random.randint(0, track_width - 1)
    score = 0

    print("Welcome to the Car Racing Game!")
    print("Use 'A' and 'D' to move the car left and right.")
    print("Try to avoid obstacles!")

    while True:
        update_screen(track_width, car_position, obstacle_position, score)

        if keyboard.is_pressed('q'):
            print("Game over!")
            break

        if keyboard.is_pressed('a'):
            car_position = max(0, car_position - 1)
        elif keyboard.is_pressed('d'):
            car_position = min(track_width - 1, car_position + 1)

        obstacle_position = (obstacle_position + random.randint(-1, 1)) % track_width
        score += 1

        if car_position == obstacle_position:
            print("Game over!")
            break

        time.sleep(0.1)


def main():
    car_game()


if __name__ == "__main__":
    main()
