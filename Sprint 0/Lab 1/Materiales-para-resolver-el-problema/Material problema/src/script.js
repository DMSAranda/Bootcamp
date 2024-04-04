// Pon a prueba tus conocimientos sobre JavaScript aqui

var tasks = []       // array que almacena tareas

var x = 0   //var

const taskTree = document.querySelector('.task-list');

const taskList = taskTree.querySelectorAll("li");

const form = document.querySelector('#taskInput');

const addTaskButton = document.querySelector('#addTaskButton')

deleteUl()



function deleteUl() {

    taskTree.innerHTML = ''
}    
      

addTaskButton.addEventListener('click', () => {
	
    const newTask = form.value

    if (newTask.trim() && newTask !== null){

        addTask(newTask)

    }else{

        alert("Please, check your task!")

    }     
})


function addTask(newTask) {

    let task = {}   //let  con id, name y completed 
    
    task.id = x + 1    //id (numero)             
                                      
   // task.completed = li.querySelector('.task-checkbox').checked     //booleano
 
    const newLi = document.createElement('li')
    const newArticle = document.createElement('article')
    const newCheckBox = document.createElement('input')
    const newSpan = document.createElement('span')
    const newI = document.createElement('i')

    newCheckBox.type = "checkbox"
	newCheckBox.classList.add('task-checkbox')
    task.completed = false
    newCheckBox.addEventListener('change', ()=>{
        if(newCheckBox.checked){
           task.completed = true  
        }else{
           task.completed = false 
        }
    })
    
	newSpan.classList.add('task-text')
    newSpan.innerHTML = newTask
    task.name = newTask       //nombre cadena

	
    newI.classList.add('fa', 'fa-trash')
    newI.addEventListener('click', () => {
        delTask(task, newLi)
    })

   /* newI.addEventListener('click', () => {
        delTask()
    })
    */

	newArticle.appendChild(newCheckBox)
    newArticle.appendChild(newSpan)

    newLi.appendChild(newArticle)
    newLi.appendChild(newI)

    taskTree.appendChild(newLi)

    //al añadir borrar input
    form.value = ''

    tasks.push(task)
    x++  

    console.log(tasks)
}



function delTask(task, newLi) {

    let newTasks = []
    taskTree.removeChild(newLi)

    for(let i = 0; i < tasks.length; i++){
       if(task !== tasks[i]){
          newTasks.push(task)
       }  
    }

    tasks = newTasks 
}