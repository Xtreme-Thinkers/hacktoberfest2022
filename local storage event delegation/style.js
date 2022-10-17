const additem =document.querySelector('add-items');
const itemslist=document.querySelector('.plates');
const item=JSON.parse(localStorage.getItem('items'))||[];
const items=[];
function addItem(e){
  e.preventDefault();
  const text=(this.querySelector('[name*item]')).value;
  const item={
    text,
    done:false,
  };
  items.push(item);
  populateList(items,itemslist);
  localStorage.setItem('items',JSON.stringify(items));
  this.reset();
}
function populateList(plates=[],platesList){
  platesList.innerHTML=plates.map((plate,i)=>{
    return `
    <li>
    <input type="checkbox" data-index=${i} id="item${i}" ${plate.done?'checked':''}/>
    <label for="item${i}">${plate.text}</label>
    </li>`;
  }).join('');
}
function toggleDone(e)
{
  if(!e.target.matches('input'))return;
  consol.log(e.target); 
}
populateList(items,itemslist);
additem.addEventListener('submit',addItem);
const checkBoxes=document.querySelectorAll('input');
checkBoxes.forEach(input=>input.addEventListener('click',()=>alert('hi')));






 


