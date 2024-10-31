#include "Bat.h"
#include <sstream>
#include <cstdlib>
#include <SFML/Graphics.hpp>
#include "Ball.h"

int main()
{
    // Create a video mode object
    VideoMode vm(1920, 1080);
    // Create and open a window for the game
    RenderWindow window(vm, "Pong");
    int score = 0;
    int lives = 3;
    // Create a bat at the bottom center of the screen
    Bat bat(1920 / 2, 1080 - 20);
    // Create a ball at the center of the screen
    Ball ball(1920 / 2, 0);

    // Create a Text object called HUD
    Text hud;
    // Load the font for the HUD
    Font font;
    font.loadFromFile("fonts/DS-DIGIT.ttf");
    hud.setFont(font);
    hud.setCharacterSize(75);
    hud.setFillColor(Color::White);
    hud.setPosition(20, 20);

    // Clock for timing
    Clock clock;

    while (window.isOpen())
    {
        // Handle player input
        Event event;
        while (window.pollEvent(event))
        {
            if (event.type == Event::Closed)
                window.close();
        }

        if (Keyboard::isKeyPressed(Keyboard::Escape))
        {
            window.close();
        }

        if (Keyboard::isKeyPressed(Keyboard::Left))
        {
            bat.moveLeft();
        }
        else
        {
            bat.stopLeft();
        }

        if (Keyboard::isKeyPressed(Keyboard::Right))
        {
            bat.moveRight();
        }
        else
        {
            bat.stopRight();
        }

        // Update the bat, ball, and HUD
        Time dt = clock.restart();
        bat.update(dt);
        ball.update(dt);

        std::stringstream ss;
        ss << "Score: " << score << "  Lives: " << lives;
        hud.setString(ss.str());

        // Handle ball hitting the bottom of the screen
        if (ball.getPosition().top + ball.getPosition().height > window.getSize().y)
        {
            ball.reboundBottom();
            lives--;
            ball.endgame();

            // Check for zero lives
            if (lives < 1) {
                score = 0;
                lives = 3;
            }
        }

        // Handle ball hitting the top of the window
        if (ball.getPosition().top < 0)
        {
            ball.reboundBatOrTop();
        }

        // Handle ball hitting the sides of the window
        if (ball.getPosition().left < 0 ||
            ball.getPosition().left + ball.getPosition().width > window.getSize().x)
        {
            ball.reboundSides();
        }

        // Check if the ball hits the bat
        if (ball.getPosition().intersects(bat.getPosition()))
        {
            ball.reboundBatOrTop();
            score++;
        }

        // Draw everything
        window.clear();
        window.draw(hud);
        window.draw(bat.getShape());
        window.draw(ball.getShape());
        window.display();
    }

    return 0;
}
