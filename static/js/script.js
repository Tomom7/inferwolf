// 参考サイト様：https://noveblo.com/javascript-create-input/

let numberForms = document.querySelectorAll('input');

function calc() {
  let result = 0;
  const total = document.getElementById('total');

  numberForms.forEach(numberForm => {
     result += Number(numberForm.value);
  });

  total.textContent = '合計：' + result;
}

numberForms.forEach(numberForm => {
  numberForm.addEventListener('input', calc);
});

document.querySelector('button').addEventListener('click', () => {
  const newForm = document.createElement('input');
  newForm.type = 'number';

  const plus = document.createElement('p');
  plus.textContent = '+';

  const div = document.querySelector('div');
  div.appendChild(plus);
  div.appendChild(newForm);

  numberForms = document.querySelectorAll('input');
  numberForms.forEach(numberForm => {
    numberForm.addEventListener('input', calc);
  });
});