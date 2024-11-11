// Данные о играх
const games = [
    {
        title: "Cyberpunk 2077",
        price: "2999 ₽",
        image: "https://via.placeholder.com/300x200"
    },
    {
        title: "Red Dead Redemption 2",
        price: "2499 ₽",
        image: "https://via.placeholder.com/300x200"
    },
    {
        title: "The Witcher 3",
        price: "1499 ₽",
        image: "https://via.placeholder.com/300x200"
    },
    {
        title: "God of War",
        price: "3999 ₽",
        image: "https://via.placeholder.com/300x200"
    },
    {
        title: "Elden Ring",
        price: "3499 ₽",
        image: "https://via.placeholder.com/300x200"
    },
    {
        title: "Spider-Man",
        price: "2999 ₽",
        image: "https://via.placeholder.com/300x200"
    }
];

// Отображение игр
function displayGames() {
    const grid = document.getElementById('gamesGrid');
    grid.innerHTML = '';

    games.forEach(game => {
        const card = document.createElement('div');
        card.className = 'game-card';
        card.innerHTML =
            <img src="${game.image}" class="game-image" alt="${game.title}">
            <div class="game-info">
                <h3 class="game-title">${game.title}</h3>
                <div class="game-price">${game.price}</div>
            </div>
        ;
        grid.appendChild(card);
    });
}

// Настройки темы
let isPanelOpen = false;

document.querySelector('.theme-toggle').addEventListener('click', () => {
    isPanelOpen = !isPanelOpen;
    document.getElementById('themePanel').style.right = isPanelOpen ? '0' : '-300px';
});

// Обработчики изменения темы
document.getElementById('primaryColor').addEventListener('input', (e) => {
    document.documentElement.style.setProperty('--primary-color', e.target.value);
});

document.getElementById('backgroundColor').addEventListener('input', (e) => {
    document.documentElement.style.setProperty('--background-color', e.target.value);
});

document.getElementById('accentColor').addEventListener('input', (e) => {
    document.documentElement.style.setProperty('--accent-color', e.target.value);
});

document.getElementById('borderRadius').addEventListener('input', (e) => {
    document.documentElement.style.setProperty('--border-radius', e.target.value + 'px');
});

document.getElementById('cardSize').addEventListener('input', (e) => {
    document.documentElement.style.setProperty('--card-size', e.target.value + 'px');
});

// Инициализация
document.addEventListener('DOMContentLoaded', () => {
    displayGames();

    // Установка начальных значений для инпутов
    document.getElementById('primaryColor').value = '#2a2a2a';
    document.getElementById('backgroundColor').value = '#f5f5f5';
    document.getElementById('accentColor').value = '#ff4757';
    document.getElementById('borderRadius').value = 10;
    document.getElementById('cardSize').value = 300;
});

// Анимация для категорий
document.querySelectorAll('.category-card').forEach(card => {
    card.addEventListener('click', () => {
        card.style.transform = 'scale(0.95)';
        setTimeout(() => {
            card.style.transform = 'scale(1)';
        }, 100);
    });
});
