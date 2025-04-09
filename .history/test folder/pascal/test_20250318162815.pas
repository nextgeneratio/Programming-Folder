program Calculator;
var
  a, b: real;
  op: char;
begin
  write('Enter first number: ');
  readln(a);
  write('Enter operator (+, -, *, /): ');
  readln(op);
  write('Enter second number: ');
  readln(b);
  case op of
    '+': writeln('Result: ', a + b);
    '-': writeln('Result: ', a - b);
    '*': writeln('Result: ', a * b);
    '/': if b <> 0 then
           writeln('Result: ', a / b)
         else
           writeln('Cannot divide by zero!');
  else
    writeln('Invalid operator!');
  end;
end.
