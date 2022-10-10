const taskInput = document.querySelector("input");
const add = document.querySelector(".add-task-button");
const todoList = document.querySelector(".todos-list");
const deleteAll = document.querySelector(".delete-all-btn");

let todos = JSON.parse(localStorage.getItem("todos")) || [];

window.addEventListener("DOMContentLoaded", showAllTodos);
function getRandomId() {
  return Math.random().toString(36).substring(2, 7);
}

function addToDo(taskInput) {
  let task = {
    id: getRandomId(),
    task: taskInput.value.trim(),
    date: new Date().toLocaleString(),
    // completed: false,
  };
  todos.push(task);
}

taskInput.addEventListener("keyup", (e) => {
  if (e.key === "Enter" && taskInput.value.length > 0) {
    addToDo(taskInput);
    save();
    taskInput.value = "";
    showAllTodos();
  }
});

add.addEventListener("click", () => {
  if (taskInput.value !== "") {
    addToDo(taskInput);
    save();
    showAllTodos();
    taskInput.value = "";
  }
});

deleteAll.addEventListener("click", clearAllTodos);

//show all todos
function showAllTodos() {
  todoList.innerHTML = "";
  todos.forEach((todo) => {
    todoList.innerHTML += `
            <li class="todo-item" id="${todo.id}">
                <p class="task-body" id="${todo.id}">
                  <input style="width: 16px; height: 16px" type="checkbox" onclick="completeTodo('${todo.id}')">
                  ${todo.task}
                  <br>
                  <span style="font-size:15px">${todo.date}</span>
                </p>
                <div class="todo-actions">
                    <button class="btn btn-success" onclick="editTodo('${todo.id}')">
                        <i class="bx bx-edit-alt bx-sm"></i>    
                    </button>
                    <button class="btn btn-error" onclick="deleteTodo('${todo.id}')">
                        <i class="bx bx-trash bx-sm"></i>
                    </button>
                </div>
            </li>
        `;
  });
}

//save todos to local storage
function save() {
  localStorage.setItem("todos", JSON.stringify(todos));
}

//delete todo
function deleteTodo(id) {
  todos = todos.filter((todo) => todo.id !== id);
  save();
  showAllTodos();
}

// complete todo
function completeTodo(id) {
  const paragraph = document.getElementById(id).children[0];
  const checkBox = paragraph.children[0];

  checkBox.addEventListener("change", (e) => {
    if (e.target.checked === true) {
      paragraph.classList.add("completed");
    }
    if (e.target.checked === false) {
      paragraph.classList.remove("completed");
    }
  });
}

//edit todo
function editTodo(id) {
  let todo = todos.find((todo) => todo.id === id);
  taskInput.value = todo.task;
  todos = todos.filter((todo) => todo.id !== id);
  add.innerHTML = "<i class='bx bx-check bx-sm'></i>";
  save();
  add.addEventListener("click", () => {
    add.innerHTML = "<i class='bx bx-plus bx-sm'></i>";
  });
}

//clear all todos
function clearAllTodos() {
  if (todos.length > 0) {
    todos = [];
    save();
    showAllTodos();
  }
}
