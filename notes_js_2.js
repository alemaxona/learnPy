// IF

// Можно писать в одну строку, если тело состоит из одной операции:
var i = 1
if (i == 1) alert(i)

// Но лучше всегда с телом
var userName = prompt('Yor name?', '')
if (userName == 'Max') {
    alert('Yeaaaah!')
} else if (userName == 'Den') {
    alert('Ops')
} else {
    alert('Baddd')
}

if (1) {
    // Всегда выполнится! Как в python: if True: ...
}

// '?', но лучше всегда использовать if else!
// --------------
var age = prompt('возраст?', 18);

var message = (age < 3) ? 'Здравствуй, малыш!' :
  (age < 18) ? 'Привет!' :
  (age < 100) ? 'Здравствуйте!' :
  'Какой необычный возраст!';

alert( message );

// Тоже самое:
var age = prompt('возраст?', 18);

if (age < 3) {
  message = 'Здравствуй, малыш!';
} else if (age < 18) {
  message = 'Привет!';
} else if (age < 100) {
  message = 'Здравствуйте!';
} else {
  message = 'Какой необычный возраст!';
}
// --------------

var company = prompt('Какая компания создала JavaScript?', '');

(company == 'Netscape') ?
   alert('Да, верно') : alert('Неправильно');


// Или - ||
alert( true || true ); // true
alert( false || true ); // true
alert( true || false ); // true
alert( false || false ); // false

// оператор ИЛИ вычисляет ровно столько значений, сколько необходимо – до первого true
var x;
true || (x = 1);
alert(x); // undefined, x не присвоен
// А в примере ниже первый аргумент – false, так что ИЛИ попытается вычислить второй, запустив тем самым присваивание:

var x;
false || (x = 1);
alert(x); // 1


var hour = 9, isWeekend = true;
if (hour < 10 || hour > 18 || isWeekend) {
    alert('Upssss.')
}

// И - &&
// Итак, оператор && вычисляет операнды слева направо до первого «ложного» и возвращает его, а если все истинные – то последнее значение.
alert( true && true ); // true
alert( false && true ); // false
alert( true && false ); // false
alert( false && false ); // false

var hour = 12,
  minute = 30;
if (hour == 12 && minute == 30) {
  alert( 'Время 12:30' );
}

if (1 && 0) { // вычислится как true && false
    alert( 'не сработает, т.к. условие ложно' );
  }

// Приоритет у && больше, чем у ||
// Приоритет оператора И && больше, чем ИЛИ ||, так что он выполняется раньше.
 alert( 5 || 1 && 0 ); // 5

// НЕ - !
alert(!true)  // false

// Преобразование типов
+'1' //  FUCKING FUCK
// 1
alert(String(null) == 'null')  // String с большой буквы
// true
alert( "123" + undefined );
// "123undefined"
alert(Number('123'))  // Number с большой буквы
// 123
var a = +"123"; // 123
// ==
var a = Number("123"); //123

// Циклы
var a = 1;
while (a < 3) {
    alert(a);
    a++;
}

// Бесконечный цикл
while (true) {
    alert('Infinity')
}

// Условие в скобках интерпретируется как логическое значение, поэтому вместо while (i!=0) обычно пишут while (i):
while (i) { // при i, равном 0, значение в скобках будет false и цикл остановится.

// do while

var i = 0;
do {
    alert(i);
    i++
} while (i <3);
// Синтаксис do..while редко используется, т.к. обычный while нагляднее – в нём не приходится искать глазами условие и ломать голову, почему оно проверяется именно в конце.

// Цикл for
// Чаще всего применяется цикл for. Выглядит он так:
// Пример цикла, который выполняет alert(i) для i от 0 до 2 включительно (до 3):
var i;
for (i = 0; i < 3; i++) {
  alert( i );
}
// Здесь:
// Начало: i=0.
// Условие: i<3.
// Шаг: i++.
// Тело: alert(i), т.е. код внутри фигурных скобок (они не обязательны, если только одна операция)

// В цикле также можно определить переменную:
for (var i = 0; i < 3; i++) {
  alert(i); // 0, 1, 2
}

// Пропуск частей:
var i = 0;

for (; i < 3; i++) {  // ';' - обязательны
  alert( i ); // 0, 1, 2
}
// Можно убрать и шаг:

var i = 0;

for (; i < 3;) {
  alert( i );
  i++;
  // цикл превратился в аналог while (i<3)
}

// Бесконечный цикл
for (;;) {
  // будет выполняться вечно
}


// Прерывание цикла: break
var sum = 0;

while (true) {

  var value = +prompt("Введите число", '');

  if (!value) break; // Выход из цикла

  sum += value;

}
alert( 'Сумма: ' + sum );


// Прерываение Continue
for (var i = 0; i < 10; i++) {

  if (i % 2 == 0) continue; // Если остаток от деления равен 0 - прерываем цикл и начинаем следующий проход цикла, если он есть! 
  alert(i);
}
// ==
for (var i = 0; i < 10; i++) {

  if (i % 2) {  // Так как if 0 - false
    alert( i );
  }
}