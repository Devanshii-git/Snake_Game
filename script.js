const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

const box = 20; // Size of the snake and food
let snake = [{ x: 9 * box, y: 9 * box }];
let direction = 'RIGHT';
let food = {
    x: Math.floor(Math.random() * 20) * box,
    y: Math.floor(Math.random() * 20) * box
};
let score = 0;


document.addEventListener('keydown', changeDirection);

function changeDirection(event) {
    if (event.keyCode === 37 && direction !== 'RIGHT') {
        direction = 'LEFT';
    } else if (event.keyCode === 38 && direction !== 'DOWN') {
        direction = 'UP';
    } else if (event.keyCode === 39 && direction !== 'LEFT') {
        direction = 'RIGHT';
    } else if (event.keyCode === 40 && direction !== 'UP') {
        direction = 'DOWN';
    }
}

function collision(head, array) {
    for (let i = 0; i < array.length; i++) {
        if (head.x === array[i].x && head.y === array[i].y) {
            return true;
        }
    }
    return false;
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Draw the snake
    for (let i = 0; i < snake.length; i++) {
        ctx.fillStyle = (i === 0) ? 'green' : 'lightgreen';
        ctx.fillRect(snake[i].x, snake[i].y, box, box);
        ctx.strokeStyle = 'darkgreen';
        ctx.strokeRect(snake[i].x, snake[i].y, box, box);
    }

    // Draw the food
    ctx.fillStyle = 'red';
    ctx.fillRect(food.x, food.y, box, box);

    // Old head position
    let snakeX = snake[0].x;
    let snakeY = snake[0].y;

    // Move the snake
    if (direction === 'LEFT') snakeX -= box;
    if (direction === 'UP') snakeY -= box;
    if (direction === 'RIGHT') snakeX += box;
    if (direction === 'DOWN') snakeY += box;

    // Check if the snake eats the food
    if (snakeX === food.x && snakeY === food.y) {
        score++;
        document.getElementById('score').innerText = 'Score: ' + score;
        food = {
            x: Math.floor(Math.random() * 20) * box,
            y: Math.floor(Math.random() * 20) * box
        };
    } else {
        // Remove the tail
        snake.pop();
    }

    // Add new head
    const newHead = { x: snakeX, y: snakeY };

    // Game over conditions
    if (snakeX < 0 || snakeY < 0 || snakeX >= canvas.width || snakeY >= canvas.height || collision(newHead, snake)) {
        clearInterval(game);
        alert('Game Over! Your score: ' + score);
    }

    snake.unshift(newHead);
}

// Call draw function every 100 ms
const game = setInterval(draw, 100);
//sound effects
const eatSound = new Audio('/static/eat.mp3');
const turnSound = new Audio('/static/turn.mp3');
const gameOverSound = new Audio('/static/gameover.mp3');
const startSound = new Audio('/static/start.mp3');
let started = false;

function gameLoop() {
    fetch('/state')
        .then(res => res.json())
        .then(state => {
            if (!started) {
                startSound.play();
                started = true;
            }
            draw(state);
            if (!state.game_over) {
                setTimeout(gameLoop, 200);
            }
        });
}
turnSound.play();
document.addEventListener('keydown', (e) => {
    const keyMap = {
        ArrowLeft: 'LEFT',
        ArrowUp: 'UP',
        ArrowRight: 'RIGHT',
        ArrowDown: 'DOWN'
    };
    const direction = keyMap[e.key];
    if (direction) {
        turnSound.play();
        fetch('/move', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ direction })
        }).then(res => res.json()).then(draw);
    }
});

let lastScore = 0;

function draw(state) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = 'green';
    state.snake.forEach(([x, y]) => {
        ctx.fillRect(x * box, y * box, box, box);
    });

    ctx.fillStyle = 'red';
    const [fx, fy] = state.food;
    ctx.fillRect(fx * box, fy * box, box, box);

    if (state.score > lastScore) {
        eatSound.play();
        lastScore = state.score;
    }

    document.getElementById('score').innerText = 'Score: ' + state.score;

    if (state.game_over) {
        gameOverSound.play();
        setTimeout(() => {
            alert('Game Over! Your score: ' + state.score);
        }, 200);
    }
}
