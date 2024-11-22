// Получаем элементы из DOM
const addTaskBtn = document.getElementById('addTaskBtn');
const taskInput = document.getElementById('taskInput');
const taskList = document.getElementById('taskList');

// Функция добавления задачи
function addTask() {
    const taskText = taskInput.value.trim();
    if (taskText === '') return;

    // Создаем элементы задачи
    const li = document.createElement('li');
    li.classList.add('task-item');

    const span = document.createElement('span');
    span.classList.add('task-text');
    span.textContent = taskText;

    const deleteBtn = document.createElement('button');
    deleteBtn.classList.add('delete-btn');
    deleteBtn.innerHTML = '&times;';

    // Добавляем события
    span.addEventListener('click', () => {
        li.classList.toggle('completed');
    });

    deleteBtn.addEventListener('click', () => {
        taskList.removeChild(li);
    });

    // Составляем структуру
    li.appendChild(span);
    li.appendChild(deleteBtn);
    taskList.appendChild(li);

    // Очищаем поле ввода
    taskInput.value = '';
}

// Добавляем задачу по клику
addTaskBtn.addEventListener('click', addTask);

// Добавляем задачу по нажатию Enter
taskInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        addTask();
    }
});